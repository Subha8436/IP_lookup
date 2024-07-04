from flask import Flask, request, render_template
import requests

app = Flask(__name__)

IPINFO_ACCESS_TOKEN = 'your_ipinfo_access_token'
GOOGLE_MAPS_API_KEY = 'your_google_maps_api_key'
ADSENSE_CLIENT_ID = 'your_adsense_client_id'
ADSENSE_AD_SLOT = 'your_adsense_ad_slot'

@app.route('/')
def home():
    return render_template('index.html', adsense_client_id=ADSENSE_CLIENT_ID, adsense_ad_slot=ADSENSE_AD_SLOT)

@app.route('/lookup', methods=['POST'])
def lookup():
    ip = request.form['ip']
    response = requests.get(f'http://ipinfo.io/{ip}?token={IPINFO_ACCESS_TOKEN}')
    
    if response.status_code == 200:
        data = response.json()
        lat, lon = map(float, data['loc'].split(','))
        return render_template('result.html', data=data, lat=lat, lon=lon, google_maps_api_key=GOOGLE_MAPS_API_KEY, adsense_client_id=ADSENSE_CLIENT_ID, adsense_ad_slot=ADSENSE_AD_SLOT)
    else:
        return render_template('error.html', message='Invalid IP address or API request failed')

if __name__ == '__main__':
    app.run(debug=True)

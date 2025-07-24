from flask import Flask
import folium
import requests
import os

app = Flask(__name__)

@app.route('/')
def serve_world_map():

    response = requests.get("http://api.open-notify.org/iss-now.json")
    lat = response.json()['iss_position']['latitude']
    lon = response.json()['iss_position']['longitude']

    m = folium.Map(location=[0, 0], zoom_start=2)
    folium.Marker([lat, lon], popup="ISS Location").add_to(m)

    html_path = os.path.join(os.path.dirname(__file__), 'world_map.html')
    m.save(html_path)

    with open(html_path, 'r') as file:
        html_content = file.read()
    print (lat, lon, "\n")
    return html_content

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 8000)
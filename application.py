import flask
from flask import Flask, request
import jsonify
import api_to_file
import geo
import json
from datetime import datetime

application = Flask(__name__)

# update the stations stats on cold start (optional)
api_to_file.get_station_stats()
stats_dict = api_to_file.read_stations_stats()

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/compute", methods=["POST"])
def compute():
    stations_dict = api_to_file.read_stations()
    device_data = request.get_json(force=True)
    print(device_data)

    cur_lat = device_data.get('latitude')
    cur_long = device_data.get('longitude')
    cur_bearing = device_data.get('heading')
    distance_km = device_data.get('distance_km')

    ad_lat, ad_long = geo.destination_point(cur_lat, cur_long, distance_km, cur_bearing)

    closest_name = 'empty'
    closest_distance = 0
    station_counter = 0
    closest_url = None

    for x in stations_dict:
        station_lat = x.get('geo_lat')
        station_long = x.get('geo_long')
        station_name = x.get("name")
        station_url = x.get('url')

        if api_to_file.is_number(station_lat) is False or api_to_file.is_number(station_long) is False:
            continue

        station_counter += 1
        this_distance = geo.haversine_distance(ad_lat, ad_long, station_lat, station_long)

        if station_counter == 1 or this_distance < closest_distance:
            closest_distance = this_distance
            closest_name = station_name
            closest_url = station_url

    print('Geo-located stations:', station_counter)
    print('Closest station:', closest_name, 'url:', closest_url)

    return jsonify(status="ok", closest_name=closest_name, closest_url=closest_url, received=device_data)

if __name__ == '__main__':
    application.run(host='0.0.0.0')

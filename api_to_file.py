import json
import requests

def get_stations():

    radio_api = "https://de1.api.radio-browser.info/json/stations?limit=100000"
    station_file = 'stations.json'
    working = 1

    try:
        response = requests.get(radio_api)
        response_json = response.json()
        response_str = json.dumps(response_json, ensure_ascii=False, indent=2)
        print ()
        print ("API data successfully received\n")
    except Exception as e:
        print ("API data retrival failed. here is the error message : ",e,'\n')
        working = 0
    try:
        myfile = open (station_file, 'w')
        myfile.write (response_str)
        myfile.close
        print ("new API data written to file\n")
    except Exception as e:
        print ("Could not write to the local stations file: here is the error message : ",e,'\n')
        working = 0
    return working

def read_stations():
    station_file = 'stations.json'
    try:
        with open(station_file, "r", encoding="utf-8") as f:
            data = json.load(f) 
    except Exception as e:
        print ("Could not read the stations file. Here is the error message : ",e,'\n')
    return data

def get_station_stats():
    stat_api = 'https://de1.api.radio-browser.info/json/stats'
    stats_file = 'stats.json'
    working = 0

    try:
        response = requests.get(stat_api)
        response_json = response.json()
        response_str = json.dumps(response_json, ensure_ascii=False, indent=2)
        print ()
        print ("Stats data successfully received\n")
    except Exception as e:
        print ("Stats data retrival failed. here is the error message : ",e,'\n')
        working = 0
    try:
        myfile = open (stats_file, 'w')
        myfile.write (response_str)
        myfile.close
        print ("New stats data written to file\n")
    except Exception as e:
        print ("Could not write to the local stats file: here is the error message : ",e,'\n')
        working = 0
    return working

def read_stations_stats():
    stats_file = 'stats.json'
    try:
        with open(stats_file, "r", encoding="utf-8") as f:
            data = json.load(f) 
    except Exception as e:
        print ("Could not read the stats file. Here is the error message : ",e,'\n')
    return data

def is_number(x):
    try:
        float(x)
        return True
    except (TypeError, ValueError):
        return False
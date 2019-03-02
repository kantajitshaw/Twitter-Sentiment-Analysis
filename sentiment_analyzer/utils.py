import requests
import json
from sentiment.analyzer import  *


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_coords_from_ip(ipaddr=""):
    url = "http://ip-api.com/json/"
    req = requests.get(url+ipaddr)
    if req.status_code == 200:
        resp_json = req.json()
        if resp_json['status'] == 'success':
            return resp_json['lat'], resp_json['lon']

    return None, None


def get_woeid_from_coords(lat, long):
    if lat is None or long is None:
        return None
    location_json = api.trends_closest(lat, long)
    return location_json[0]['woeid']


def get_trends_list_from_woeid(woeid):
    if woeid is None:
        return None
    trends_json = api.trends_place(woeid)

    return [trend["name"].replace('#','') for trend in trends_json[0]["trends"] if trend["name"].startswith('#')]


def get_trends_list_from_ip(ipaddr=""):
    lat, long = get_coords_from_ip(ipaddr)
    return get_trends_list_from_woeid(get_woeid_from_coords(lat, long))[:5]

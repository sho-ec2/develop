from django.shortcuts import render

import requests


def Index(request):

    datas = getPlaceInfo()

    return render(request, 'randomSelect/index.html', {'datas': datas})


def getPlaceInfo():
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    q = { 'location': '34.7055051, 135.4983028',
          'keyword': '公園',
          # 'type': 'food',
          # 'language': 'ja',
          'radius': '500',
          'key': 'AIzaSyD33jnUmNEXE9REuedHsjRTivdoratQ8fk'}
    s = requests.Session()
    r = s.get(url, params=q)
    json_o = r.json()
    results = json_o['results']

    return results

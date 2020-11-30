from django.shortcuts import render

from randomSelect.forms import getInfoForm

import requests, random

# 初期表示
def Index(request):
    form = getInfoForm
    content = {'form' : form}
    return render(request, 'randomSelect/index.html', content)

# お店のランダム取得
def returnResult(request):
    if request.method == 'POST':
        form = getInfoForm(request.POST)
        if form.is_valid():
            station = form.cleaned_data['station']
            category = form.cleaned_data['category']
            radius = form.cleaned_data['radius']
            form = getInfoForm(initial={'station': station, 'category': category, 'radius': radius})
            targetInfo = getPlaceInfo(station, category, radius)
            # ランダムな数字を取得し、情報を1つに絞る
            inf = targetInfo[random.randrange(len(targetInfo))]
            name = inf['name']
            open = inf['opening_hours']['open_now']
            url = inf['photos'][0]['html_attributions'][0]
            level = inf['price_level']
            content = {'name': name, 'open':open, 'url': url, 'level': level}
            return render(request, 'randomSelect/selectedItem.html', content)
        else:
            form = getInfoForm
            content = {'form': form}
    else:
        form = getInfoForm
        content = {'form': form}
    return render(request, 'randomSelect/index.html', content)

# googleMapAPIから情報を取得する
def getPlaceInfo(station, category, radius):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    q = { 'location': '34.7055051, 135.4983028',
          'type': category,
          'language': 'ja',
          'radius': radius,
          'key': 'AIzaSyD33jnUmNEXE9REuedHsjRTivdoratQ8fk'}
    s = requests.Session()
    r = s.get(url, params=q)
    json_o = r.json()
    results = json_o['results']

    return results

from django.shortcuts import render

from randomSelect.forms import getInfoForm

import requests, random
import json



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
            line = form.cleaned_data['line']
            keyword = form.cleaned_data['keyword']
            if keyword == 'followUs':
                location = getLocation(line, station)
                lat = location['x']
                lon = location['y']
                targetInfo = getPlaceInfo(category, radius, lat, lon)
                if bool(targetInfo):
                    # ランダムな数字を取得し、情報を1つに絞る
                    content = selectItem(targetInfo)
                else:
                    message = '利用可能なお店はありません'
                    content = {'message': message}
                    return render(request, 'randomSelect/index.html', content)
                return render(request, 'randomSelect/selectedItem.html', content)
            else:
                content = {'form': form, 'message' : 'キーワードが異なります'}
                return render(request, 'randomSelect/index.html', content)
        else:
            form = getInfoForm
            message = '有効な値を選択してください'
            content = {'form': form, 'message': message}
    else:
        form = getInfoForm
        message = '有効な情報を選択してください。'
        content = {'form': form, 'message': message}
    return render(request, 'randomSelect/index.html', content)

# アイテムを取得し、利用可能なアイテムを返す
def selectItem(targetInfo):
    i = 0
    content = {}
    open = 'False'
    count = len(targetInfo)
    while i < count:
        inf = targetInfo[random.randrange(0,count)]
        print('--------------------------++++++++++++++++++++++++++')
        print(inf)
        print('--------------------------++++++++++++++++++++++++++')
        if 'opening_hours' in inf.keys():
            if 'open_now' in inf['opening_hours'].keys():
                open = str(inf['opening_hours']['open_now'])
        else:
            open = 'notSure'
        if open == 'True':
            name = inf['name']
            lat = str(inf['geometry']['location']['lat'])
            lon = str(inf['geometry']['location']['lng'])
            coordinate = lat + ',' + lon
            url = 'https://www.google.com/maps/search/?api=1&query=' + name + '&center=' + coordinate
            print(url)
            content = {'name': name, 'open':open, 'url': url}
            if 'price_level' in inf.keys():
                level = inf['price_level']
                content['level'] = level
            break
        elif open == 'notSure':
            name = inf['name']
            lat = str(inf['geometry']['location']['lat'])
            lon = str(inf['geometry']['location']['lng'])
            coordinate = lat + ',' + lon
            url = 'https://www.google.com/maps/search/?api=1&query=' + name + '&center=' + coordinate
            message = '開いているかわからないけど。。。'
            content = {'name': name, 'open':open, 'url': url, 'message': message}
            if 'price_level' in inf.keys():
                level = inf['price_level']
                content['level'] = level
        else:
            if not bool(content):
                message = '周辺に利用可能なお店はありませんでした。'
                content ={'message': message}
        i += 1
        print('------------------------')
        print(open)
        print('No' + str(i))
        print('------------------------')
    return content

# 開発用メソッド
def demoSelectItem(targetInfo):
    count = len(targetInfo)
    if(count != '' or count > 0):
        inf = targetInfo[random.randrange(len(targetInfo))]
        # open_nowがない場合があるので、コメントアウト
        #open = inf['opening_hours']['open_now']
        open = True
        name = inf['name']
        #place_id = inf['place_id']
        # url = 'https://www.google.com/maps/place/?q=place_id:' + place_id
        url = 'https://www.google.com/maps/place/?query=' + name
        # price_levelがない場合があるので、コメントアウト
        #level = inf['price_level']
        level = '0'
        content = {'name': name, 'open':open, 'url': url, 'level': level}
    else:
        message = '利用可能なお店はありません。'
        content = {'message': message}
    return content

# googleMapAPIから情報を取得する
def getPlaceInfo(category, radius, lat, lon):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    key = getKeyinfo()
    items = []
    items.append(category) 
    q = { 'location': str(lon) + ', ' + str(lat),
          'types': items,
          'language': 'ja',
          'radius': radius,
          'key': key}
    s = requests.Session()
    r = s.get(url, params=q)
    json_o = r.json()
    results = json_o['results']

    return results

def getLocation(line, name):
    url = 'http://express.heartrails.com/api/json?method=getStations&line='+line+'&name='+name
    s = requests.Session()
    response = s.get(url)
    res_o = response.json()
    result = res_o['response']['station'][0]
    return result

def emptyResult(category, radius, lat, lon):
    result = {}
    return result


def getKeyinfo():
    json_open = open('randomSelect/secret.json', 'r')
    json_load = json.load(json_open)
    key = json_load['googleapi']
    return key
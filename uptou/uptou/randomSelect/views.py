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
            location = getLocation(line, station)
            lat = location['x']
            lon = location['y']
            targetInfo = getPlaceInfo(category, radius, lat, lon)
            print('---------------------')
            print(targetInfo)
            print('---------------------')
            if bool(targetInfo):
                # ランダムな数字を取得し、情報を1つに絞る
                content = demoSelectItem(targetInfo)
            else:
                message = '利用可能なお店はありません'
                content = {'message': message}
                return render(request, 'randomSelect/index.html', content)
            return render(request, 'randomSelect/selectedItem.html', content)
        else:
            form = getInfoForm
            content = {'form': form}
    else:
        form = getInfoForm
        message = '有効な情報を選択してください。'
        content = {'form': form, 'message': message}
    return render(request, 'randomSelect/index.html', content)

# アイテムを取得し、利用可能なアイテムを返す
def selectItem(targetInfo):
    open = False
    i = 1
    while open == False:
        count = len(targetInfo)
        if(count != '' or count > 0):
            inf = targetInfo[random.randrange(len(targetInfo))]
            open = inf['opening_hours']['open_now']
            if open == True:
                name = inf['name']
                url = inf['photos'][0]['html_attributions'][0]
                level = inf['price_level']
                content = {'name': name, 'open':open, 'url': url, 'level': level}
                break
            i+=1
            if i > 15:
                message = '周辺に利用可能なお店はありませんでした。'
                content ={'message': message}
                break
        else:
            message = '利用可能なお店はありません。'
            content = {'message': message}
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
        place_id = inf['place_id']
        url = 'https://www.google.com/maps/place/?q=place_id:' + place_id
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
    q = { 'location': str(lon) + ', ' + str(lat),
          'type': category,
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

def demoMethod(category, radius, lat, lon):
    result = [
            {'business_status': 'OPERATIONAL', 
            'geometry': {'location': {'lat': 34.7071056, 'lng': 135.4991451}, 'viewport': {'northeast': {'lat': 34.7084735802915, 'lng': 135.5005426802915}, 'southwest': {'lat': 34.7057756197085, 'lng': 135.4978447197085}}},
            'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png', 
            'name': 'ビランチャ 梅田店', 
            'opening_hours': {'open_now': True}, 
            'photos': [{'height': 2640, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/113091371275696856641">ビランチャ 梅田店</a>'], 'photo_reference': 'ATtYBwL2hM6TNGEUaOsZsBy0sGCltVGl92YLDp9Noxv3H9hN-FdSC6V0k5N--uaM5j9fR6VbrLvHxhuzz3O1AqhGgzyFjaJvjYn1T3XYbEmchuircjDpk-TZQYTyD-5gkwiuV3W-hCgdgEIDB4eSsL5FpS0Sd3y4otQ81pOVqqSe_mJHRy4O', 'width': 3960}], 
            'place_id': 'ChIJK974ppHmAGAR0SjOxht3Tu8', 
            'plus_code': {'compound_code': 'PF4X+RM 日本、大阪府大阪市', 'global_code': '8Q6QPF4X+RM'}, 
            'price_level': 2, 
            'rating': 3.6, 
            'reference': 'ChIJK974ppHmAGAR0SjOxht3Tu8', 
            'scope': 'GOOGLE', 
            'types': ['meal_takeaway', 'cafe', 'restaurant', 'food', 'point_of_interest', 'establishment'], 
            'user_ratings_total': 58, 
            'vicinity': '大阪市北区茶屋町１０−１２ ＮＵ茶屋町8F'}
            ]
    return result

def emptyResult(category, radius, lat, lon):
    result = {}
    return result


def getKeyinfo():
    json_open = open('randomSelect/secret.json', 'r')
    json_load = json.load(json_open)
    key = json_load['googleapi']

    print(key)
    return key
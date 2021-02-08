import requests

response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode=Хабаровск&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][0]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"])


response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode=Уфа&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][0]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"])


response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode=Нижний,+Новгород&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][0]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"])


response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode= Калининград&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][0]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"])


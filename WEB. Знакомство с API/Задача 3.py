import requests

response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode=Барнаул&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][1]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"])


response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode=Мелеуз&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][1]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"])


response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode=Йошкар-Ола&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][1]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"])
import requests

response = requests.get('https://geocode-maps.yandex.ru/1.x?geocode=Москва,+Петровка,+38&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json')

json = response.json()["response"]["GeoObjectCollection"]['featureMember'][0]["GeoObject"]
print(json["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["AdministrativeArea"]["Locality"]["Thoroughfare"]["Premise"]["PostalCode"]["PostalCodeNumber"])
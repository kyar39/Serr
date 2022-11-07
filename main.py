import phonenumbers
import opencage
import folium
from myphone import number


from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber,"zh")
print(location)


from phonenumbers import  carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,'en'))

# opencase add project
from opencage.geocoder import OpenCageGeocode
key='493169327d474d4dbccd896be3a3c881'

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
# print(results)

lat=results[0]['geometry']['lat']
lan=results[0]['geometry']['lng']
print(lat,lan)

# folium

myMap=folium.Map(location=[lat,lan],zoom_start=9)
folium.Marker([lat,lan],popup=location).add_to(myMap)
myMap.save('MyLocation.html')
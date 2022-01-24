import geocoder
import folium

g = geocoder.ip("me")
my_address = g.latlng
my_map = folium.map(location = my_address = zoom_start = 12)



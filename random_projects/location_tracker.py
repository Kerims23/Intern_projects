#some errors with this, need to come back too

import geocoder
import folium

g = geocoder.ip("me")
my_address = g.latlng
my_map = folium.map(location = my_address, zoom_start = 12)


my_map.save("my_map.html")
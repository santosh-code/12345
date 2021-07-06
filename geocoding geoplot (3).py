import pandas as pd
import geopy
pip install geocoder
import geocoder
from geopy import Nominatim
locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Champ de Mars, Paris, France")
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
df = pd.read_csv("E:\\360DigitMG\\LMC\\sa.csv",encoding= 'unicode_escape')
df.head()
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
# 2- - create location column
df['Address'] = df[['Address1', 'Address2', 'Address3']].apply(lambda x: ', '.join(x), axis=1)
df['location'] = df['Address'].apply(geocode)
# 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
# 4 - split point column into latitude, longitude and altitude columns
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df.to_csv(r'E:/360DigitMG/LMC/filename.csv')
####################################### map
import pandas as pd
import requests
from xml.etree import ElementTree
import numpy as np
import folium
df1=pd.read_csv(r"E:/360DigitMG/LMC/lat.csv")
locations = df1[['latitude', 'longitude']]
locationlist = locations.values.tolist()
len(locationlist)
locationlist[12]
import folium
map = folium.Map(location=[29.7558655,-95.0897994], zoom_start=12)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=df['Row ID'][point]).add_to(map)
map

import pandas as pd
import geopy
import geocoder
from geopy import Nominatim
locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Champ de Mars, Paris, France")
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
df = pd.read_csv("F:\Data Sets\Sample - Superstore.csv")
df.head()
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
# 2- - create location column

df['location'] = df['Address'].apply(geocode)
# 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
# 4 - split point column into latitude, longitude and altitude columns
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df.to_csv(r'C:\Users\VISHNU MANOHAR\Desktop/filename.csv')

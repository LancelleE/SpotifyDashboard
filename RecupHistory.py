import pandas as pd
import json
import pickle

"""
LIBRARY UPLOAD
"""

PATH = "DATA/my_spotify_data/MyData/"
with open(PATH + 'YourLibrary.json', 'rb') as f:
    lib = json.load(f)

library = pd.DataFrame(lib['tracks'])

library.rename(index=str, columns={
    "artist": "Artist",
    "album": "Album",
    "track": "Track"
}, inplace=True)

"""
STREAMINGHISTORY UPLOAD
"""
df_final = pickle.load(open("DATA/df_final.p", "rb"))

"""
MERGE TO GET ALBUMS
"""

full_data = pd.merge(df_final, library, how="left", on=['Track', 'Artist'])
full_data['Date'] = pd.to_datetime(full_data['Date'], format='%Y-%m-%d %H:%M')
full_data.insert(value=full_data['Date'].dt.hour, loc=5, column="Hour")

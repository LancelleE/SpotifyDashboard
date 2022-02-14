import pandas as pd
import json
import glob

"""
LIBRARY UPLOAD
"""

PATH = "DATA/my_spotify_data/MyData/"


def import_streaming_history(filepath):
    with open(filepath, 'rb') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df['endTime'] = pd.to_datetime(df['endTime']).dt.strftime('%Y-%m-%d %i:%m')
    df['msPlayed'] = df['msPlayed'] / 1000
    return df


def import_all_streaming_history_files():
    file_list = glob.glob(PATH + "StreamingHistory**.json")
    doc_list = []
    for i in file_list:
        doc_list.append(import_streaming_history(i))

    full_df = pd.concat(doc_list, axis=0)

    full_df.rename(index=str, columns={
        "endTime": "Date",
        "artistName": "Artist",
        "trackName": "Track",
        "msPlayed": "Duration"
    }, inplace=True)

    return full_df


def import_library():
    with open(PATH + 'YourLibrary.json', 'rb') as f:
        lib = json.load(f)

    library = pd.DataFrame(lib['tracks'])

    library.rename(index=str, columns={
        "artist": "Artist",
        "album": "Album",
        "track": "Track"
    }, inplace=True)

    return library


def import_all():
    streaming_history = import_all_streaming_history_files()
    library = import_library
    return streaming_history, library

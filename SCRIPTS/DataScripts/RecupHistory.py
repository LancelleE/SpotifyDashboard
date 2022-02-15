import pandas as pd
import json
import glob

global PATH


def import_streaming_history(filepath):
    with open(filepath, 'rb') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df['endTime'] = pd.to_datetime(df['endTime']).dt.strftime('%Y-%m-%d %H:%m')
    df['msPlayed'] = df['msPlayed'] / 1000
    return df


def import_all_streaming_history_files(PATH):
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


def import_library(PATH):
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
    PATH = "DATA/my_spotify_data/MyData/"

    streaming_history = import_all_streaming_history_files(PATH)
    library = import_library(PATH)
    full_data = pd.merge(streaming_history, library, how="left", on=['Track', 'Artist'])
    full_data['Date'] = pd.to_datetime(full_data['Date'], format='%Y-%m-%d %H:%M')
    full_data.insert(value=full_data['Date'].dt.hour, loc=5, column="Hour")

    return full_data

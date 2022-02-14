# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:28:21 2021

@author: etien
"""

"""
The aim of this script is to create functions that will help us to create rankings.

"""
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import glob
import json
import pandas as pd
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

"""

j'ai fait les modifs dans mon spotify donc ce sera bon pour le prochain upload.

"""


def filter_hour(df, h_min, h_max):
    if h_min < h_max:
        df_filter = df[(df.Hour >= h_min) & (df.Hour < h_max)]
    elif h_min == h_max:
        df_filter = df
    elif h_min > h_max:
        df_part1 = df[(df.Hour >= h_min) & (df.Hour < 24)]
        df_part2 = df[(df.Hour >= 0) & (df.Hour < h_max)]
        df_filter = pd.concat([df_part1, df_part2], axis=0)
    return (df_filter)


def filter_date(df, date_min, date_max):
    mini = min(date_min, date_max)
    maxi = max(date_min, date_max)
    df_filter = df[(df.Date >= mini) & (df.Date < maxi)]
    return (df_filter)


def seconds_to_format(value):
    sec = timedelta(seconds=value)
    d = datetime(1, 1, 1) + sec
    chain = "%dj %dh %dm %ds" % (d.day - 1, d.hour, d.minute, d.second)
    return (chain)


def seconds_to_format2(value):
    sec = timedelta(seconds=value)
    d = datetime(1, 1, 1) + sec
    chain = "%dh %dm %ds" % (d.hour, d.minute, d.second)
    return (chain)


"""
GLOBAL RANKINGS
"""


def artiste_ranking(df, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)

    new_df = df_final_filtered.groupby(['Artist'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format)
    final_rank.insert(loc=0, column="Rank", value=range(1, 21))
    return (final_rank)


artiste_ranking(full_data, 0, 23, '2019-01-01', '2022-08-16')


def album_ranking(df, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)

    new_df = df_final_filtered.groupby(['Album', 'Artist'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format)
    final_rank.insert(loc=0, column="Rank", value=range(1, 21))
    return (final_rank)


album_ranking(full_data, 0, 23, '2019-01-01', '2022-08-16')


def song_ranking(df, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)

    new_df = df_final_filtered.groupby(['Track', 'Album', 'Artist'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format)
    final_rank.insert(loc=0, column="Rank", value=range(1, 21))
    return (final_rank)


song_ranking(full_data, 0, 23, '2019-01-01', '2022-08-16')

"""
FOCUS ON AN ARTIST
"""


def artist_song_ranking(df, artist, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)
    df_artist = df_final_filtered[df_final_filtered["Artist"] == artist]

    new_df = df_artist.groupby(['Track', 'Album'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format2)
    return (final_rank)


# artist_song_ranking(full_data,"Niska",0,23,'2019-01-01','2022-08-16')


def artist_song_ranking(df, artist, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)
    df_artist = df_final_filtered[df_final_filtered["Artist"] == artist].fillna("Album Inconnu")

    new_df = df_artist.groupby(['Track', 'Album'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format2)
    return (final_rank)


# artist_song_ranking(full_data,"Angèle",0,23,'2019-01-01','2022-08-16')


def artist_through_time(df, artist, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)
    df_artist = df_final_filtered[df_final_filtered["Artist"] == artist]

    df_artist.insert(loc=0, column="Date1", value=pd.to_datetime(df_artist['Date']).dt.date)

    new_df = df_artist.groupby(['Date1'])["Duration"].sum().reset_index()
    new_df.columns = ['Date', 'Duration']
    new_df.Date = new_df["Date"].astype(str)

    left_table = pd.DataFrame({"Date": pd.date_range(start=date_min, end=date_max).astype(str)})

    final_table = pd.merge(left=left_table, right=new_df, how="left", on=['Date'])

    final_table.fillna(0, inplace=True)
    final_table["DurationStyle"] = final_table["Duration"].apply(seconds_to_format2)
    return (final_table)


def clock_graph_dataset(df, date_min, date_max):
    df_final = filter_date(df, date_min=date_min, date_max=date_max)

    new_df = df_final.groupby(['Hour'])["Duration"].sum().reset_index()
    new_df["DurationStyle"] = new_df["Duration"].apply(seconds_to_format2)
    new_df["Hour"] = new_df["Hour"].astype(str)
    return (new_df)


test = clock_graph_dataset(full_data, '01-01-2020', '31-12-2020')

fig = go.Figure(go.Barpolar(
    r=test.Duration,
    theta=test.Hour,
    marker_line_color="black",
    marker_line_width=2,
    opacity=0.85,
    hovertemplate="<b>%{theta}h</b><br><i>%{text}</i><extra></extra>",
    text=test.DurationStyle.astype(str)
))

fig.write_html('first_figure.html', auto_open=True)

# test = artist_through_time(full_data,"Liam Gallagher",0,24,'2019-10-01','2021-02-01')

# fig = go.Figure(go.Bar(
#     x = test.Date,
#     y = test.Duration,
#     hovertemplate =
#     "<b>%{x}</b><br><i>%{text}</i><extra></extra>",
#     text = test.DurationStyle.astype(str),
#     showlegend = False))
# fig.write_html('first_figure.html', auto_open=True)


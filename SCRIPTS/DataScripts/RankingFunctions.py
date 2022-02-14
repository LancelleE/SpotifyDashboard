# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:28:21 2021

@author: etienne
"""

from datetime import datetime, timedelta
import pandas as pd


def filter_hour(df, h_min, h_max):
    df_filter = None
    if h_min < h_max:
        df_filter = df[(df.Hour >= h_min) & (df.Hour < h_max)]
    elif h_min == h_max:
        df_filter = df
    elif h_min > h_max:
        df_part1 = df[(df.Hour >= h_min) & (df.Hour < 24)]
        df_part2 = df[(df.Hour >= 0) & (df.Hour < h_max)]
        df_filter = pd.concat([df_part1, df_part2], axis=0)
    return df_filter


def filter_date(df, date_min, date_max):
    mini = min(date_min, date_max)
    maxi = max(date_min, date_max)
    df_filter = df[(df.Date >= mini) & (df.Date < maxi)]
    return df_filter


def seconds_to_format(value):
    sec = timedelta(seconds=value)
    d = datetime(1, 1, 1) + sec

    if value < 60:
        chain = "%ds" % (d.second)
    elif value < 3600:
        chain = "%dm %ds" % (d.minute, d.second)
    elif value < 216000:
        chain = "%dh %dm %ds" % (d.hour, d.minute, d.second)
    else:
        chain = "%dj %dh %dm %ds" % (d.day - 1, d.hour, d.minute, d.second)
    return chain


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
    return final_rank


def album_ranking(df, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)

    new_df = df_final_filtered.groupby(['Album', 'Artist'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format)
    final_rank.insert(loc=0, column="Rank", value=range(1, 21))
    return final_rank


def song_ranking(df, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)

    new_df = df_final_filtered.groupby(['Track', 'Album', 'Artist'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format)
    final_rank.insert(loc=0, column="Rank", value=range(1, 21))
    return final_rank


def artist_song_ranking(df, artist, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)
    df_artist = df_final_filtered[df_final_filtered["Artist"] == artist].fillna("Album Inconnu")

    new_df = df_artist.groupby(['Track', 'Album'], sort=True)["Duration"].sum().reset_index()
    final_rank = new_df.sort_values(by=['Duration'], ascending=[False])[0:20]

    final_rank["Duration"] = final_rank["Duration"].apply(seconds_to_format)
    return final_rank


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
    final_table["DurationStyle"] = final_table["Duration"].apply(seconds_to_format)
    return final_table


def clock_graph_dataset(df, date_min, date_max):
    df_final = filter_date(df, date_min=date_min, date_max=date_max)

    new_df = df_final.groupby(['Hour'])["Duration"].sum().reset_index()
    new_df["DurationStyle"] = new_df["Duration"].apply(seconds_to_format)
    new_df["Hour"] = new_df["Hour"].astype(str)
    return new_df

from SCRIPTS.DataScripts.RankingFunctions import filter_date, filter_hour


def get_nb_songs(df, h_min, h_max, date_min, date_max):
    df_filter = filter_hour(df=df, h_min=h_min, h_max=h_max)
    df_final_filtered = filter_date(df_filter, date_min=date_min, date_max=date_max)
    output = len(set(df_final_filtered['Song']))
    return output

import pandas as pd
import math
import numpy as np


def rename_dataframe_columns(df: pd.DataFrame, old_names: list, new_names: list):
    for (old_name, new_name) in zip(old_names, new_names):
        df.rename({old_name: new_name}, inplace=True)
    return df


def groupby_and_split(df: pd.DataFrame, groupby: list):
    agg = df.groupby(groupby)
    data = list()
    for a in agg:
        data.append(a[1].to_dict('records'))
    return data


def delete_columns(df: pd.DataFrame, deleted_columns: list):
    for column in deleted_columns:
        df.drop(column, axis=1, inplace=True)


def split_data(data_list: list, pieces: int):
    return np.array_split(data_list, pieces)


def add_default_shape_settings(df):
    df['shape_type'] = 'Ellipse'
    df['ticks'] = 60
    df['outline_width'] = 0
    df_length = df['shape_type'].size
    df['fill_color'] = [(255, 255, 255, 255)] * df_length
    df['outline_fill'] = [(255, 255, 255, 255)] * df_length
    df['percentage'] = 0.005


def longitude_to_point(longitude, image_width):
    return math.ceil((image_width / 360) * (180 + longitude))


def latitude_to_point(latitude, image_height):
    return math.ceil((image_height / 180) * (90 - latitude))

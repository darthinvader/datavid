import math

import numpy as np
import pandas as pd

from datavid.BasicFrameItems.ShapeFrameItem import ShapeFrameItem


def rename_dataframe_columns(df: pd.DataFrame, old_names: list, new_names: list):
    """
        Renames dataframe columns.
    """
    for (old_name, new_name) in zip(old_names, new_names):
        df.rename({old_name: new_name}, inplace=True)
    return df


def groupby_and_split(df: pd.DataFrame, groupby: list):
    """
        Groups and then splits a dataframe into lists of dicts.
    """
    agg = df.groupby(groupby)
    data = list()
    for a in agg:
        data.append(a[1].to_dict('records'))
    return data


def delete_columns(df: pd.DataFrame, deleted_columns: list):
    """
        Deletes columns from dataframe.
    """
    for column in deleted_columns:
        df.drop(column, axis=1, inplace=True)


def split_data(data_list: list, num_of_pieces: int):
    """
        Splits @data_list to @num_of_pieces pieces.
        @param data_list: our list we want to split
        @param num_of_pieces: the amount of pieces we want to split our @data_list
        @return: the split up list
    """
    return np.array_split(data_list, num_of_pieces)


def add_default_shape_settings(df):
    """
        These are default values for most MapView rendering runs.
    """

    df['frames_to_live'] = 60
    df['percentage'] = 0.005
    df_length = df['ticks'].size
    df['effects'] = [[] for x in range(0, df_length)]
    df['shape'] = ["Circle" for x in range(0, df_length)]


def longitude_to_point(longitude, image_width):
    return math.ceil((image_width / 360) * (180 + longitude))


def latitude_to_point(latitude, image_height):
    return math.ceil((image_height / 180) * (90 - latitude))

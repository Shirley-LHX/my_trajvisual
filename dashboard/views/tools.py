import random
from turtle import color
import movingpandas as mpd
import pandas as pd
from geopandas import GeoDataFrame, read_file
from dashboard.models import Elephant
from shapely.geometry import Point, LineString, Polygon
from django_pandas.io import read_frame

import warnings
warnings.simplefilter("ignore")


# 获取模型list
def get_objecet_list(df, model):
    df_list = []
    for e in df.T.to_dict().values():
        df_list.append(model(**e))
    return df_list


# 上传文件
def upload_data(df, model):
    df = df[['event', 'id', 'lon', 'lat', 'datetime']]
    # df.rename(columns={'event-id': 'event'}, inplace=True)
    df['event'] = pd.to_numeric(df['event'])
    model.objects.bulk_create(get_objecet_list(df, model))


# 获取gdf数据
def get_gdf(df):
    # df.rename(columns={'event-id': 'event'}, inplace=True)
    df[['event', 'lon', 'lat']] = df[[
        'event', 'lon', 'lat']].apply(pd.to_numeric)

    geometry = [Point(xy) for xy in zip(df.lon, df.lat)]
    gdf = GeoDataFrame(df, geometry=geometry)
    gdf = gdf[['event', 'id', 'lon', 'lat', 'datetime', 'geometry']]
    gdf['timestamp'] = gdf['datetime']
    return gdf


# 获取随机颜色
def randomcolor():
    colorArr = ['1', '2', '3', '4', '5', '6', '7',
                '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0, 14)]
    return "#"+color


# 获取color_dict
def get_color(id_list):
    color_dict = dict((id, randomcolor())for id in id_list)
    return color_dict


# 从数据库中获得的querylist变为dataframe
def change_to_df(qs):
    df = read_frame(qs=qs)
    df[['lon', 'lat']] = df[[
        'lon', 'lat']].apply(pd.to_numeric)
    return df

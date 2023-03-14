import pandas as pd
from geopandas import GeoDataFrame, read_file
from shapely.geometry import Point, LineString, Polygon
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import movingpandas as mpd
from pymove import folium, MoveDataFrame
from pymove.query import query
from . import tools


# 数据压缩
def data_generalize(traj, mode, offset):
    if mode == 1:
        generalized = mpd.MinTimeDeltaGeneralizer(traj).generalize(
            tolerance=timedelta(days=offset))
    elif mode == 2:
        generalized = mpd.DouglasPeuckerGeneralizer(
            traj).generalize(tolerance=offset)
    else:
        generalized = mpd.MinDistanceGeneralizer(
            traj).generalize(tolerance=offset)
    return generalized


# 数据过滤
def data_filter(traj, str, value):
    filtered = traj.filter(str, value)
    return filtered


# 过滤掉一些数据少的轨迹
def filter_by_number(traj, id_list, num):
    gdf = traj.to_point_gdf()
    check_list = []
    for i in id_list:
        if len(gdf.loc[gdf['id'] == i]) > num:
            check_list.append(i)
    filtered = data_filter(traj, 'id', check_list)
    return filtered


# 数据分段
def data_split(traj, mode, value):
    if mode == 1:
        splited = mpd.TemporalSplitter(traj).split(mode=value)
    else:
        splited = mpd.ObservationGapSplitter(
            traj).split(gap=timedelta(hours=value))

    return splited


# 数据查询
def data_query(gdf, querylist, mode, offset, type='MEDP'):
    if mode == 1:
        proximity = query.range_query(
            gdf, querylist, min_dist=offset, distance=type)
    else:
        proximity = query.knn_query(
            gdf, querylist, k=offset, distance=type)

    return proximity


# 数据存储
def data_storage(str, model):
    tools.upload_data(str, model)

from email import message
import time
from turtle import color
from django.shortcuts import render
from pymove import folium
from matplotlib.style import context
import movingpandas as mpd
from sympy import li
from dashboard.models import Elephant, Upload_data, Whale
import pandas as pd
import dashboard.views.core as core
from . import tools
import pymove as pm
# Create your views here.


def index(request):
    context = {
    }
    return render(request, 'partials/base.html', context)


def Home(request):
    return render(request, 'dashboard/Home.html')


def Hurricane(request):
    return render(request, 'dashboard/examples/hurricane.html')


def Bowhead_whale(request):
    start1 = time.time()
    qs = Whale.objects.all()
    end1 = time.time()

    start2 = time.time()
    df = tools.change_to_df(qs)
    id_list = df['id'].unique()
    color_dict = tools.get_color(id_list)
    end2 = time.time()

    m = folium.plot_trajectories(
        df, zoom_start=4, tile='OpenStreetMap', color_by_id=color_dict)
    m = m._repr_html_()

    hm = folium.heatmap(
        df, zoom_start=4, tile='OpenStreetMap')
    hm = hm._repr_html_()

    context = {
        'map': m,
        'color_dict': color_dict,
        'heatmap': hm,
    }
    print(end1-start1, end2-start2)
    return render(request, 'dashboard/examples/bowhead_whale.html', context)


def African_elephant(request):
    start1 = time.time()
    qs = Elephant.objects.all()
    end1 = time.time()

    start2 = time.time()
    df = tools.change_to_df(qs)
    id_list = df['id'].unique()
    color_dist = tools.get_color(id_list)
    end2 = time.time()

    m = folium.plot_trajectories(
        df, zoom_start=9, tile='OpenStreetMap', color_by_id=color_dist)
    m = m._repr_html_()

    hm = folium.heatmap(
        df, zoom_start=9, tile='OpenStreetMap')
    hm = hm._repr_html_()

    context = {
        'map': m,
        'color_dist': color_dist,
        'heatmap': hm,
    }
    print(end1-start1, end2-start2)
    return render(request, 'dashboard/examples/african_elephant.html', context)


# 接受上传文件并保存
def data_upload(request):
    myfile = request.FILES.get('upload_file')
    n = myfile.name
    if not n.endswith('.csv'):
        message = '这不是.csv文件！请上传.csv文件！'
    else:
        start1 = time.time()
        df = pd.read_csv(myfile)
        tools.upload_data(df, Upload_data)
        end1 = time.time()
        message = '上传成功！'
    context = {
        'message': message,
    }
    print(f'Time of uploading data is {end1-start1}')
    return render(request, 'dashboard/success.html', context)


def Store(request):
    return render(request, 'dashboard/store.html')


# 查找特定轨迹
def special_query(request):
    dictory = request.POST.get("sellist")
    list = dictory.split(':')
    id = list[0]
    color_dict = {list[0]: list[1]}
    qs = Elephant.objects.filter(id=id)
    df = tools.change_to_df(qs)
    m = folium.plot_trajectories(
        df, zoom_start=9, tile='OpenStreetMap', color_by_id=color_dict)

    m = m._repr_html_()
    context = {
        'id': id,
        'map': m,
    }
    return render(request, 'dashboard/query.html', context)


# 查找相似轨迹
def similar_query(request):
    start2 = time.time()
    id = request.POST.get("sellist")
    way = int(request.POST.get("way"))
    method = request.POST.get("method")
    offset = int(request.POST.get("offset"))
    end2 = time.time()
    print(id, way, method, offset)
    print(f'Time for getting form: {end2-start2}')

    start3 = time.time()
    qs = Elephant.objects.filter(id=id)
    checked_df = tools.change_to_df(qs)

    alist = Elephant.objects.all()
    list_df = tools.change_to_df(alist)
    end3 = time.time()
    print(f'Time for getting data from database: {end3-start3}')

    start1 = time.time()
    proximity = core.data_query(
        checked_df, list_df, mode=way, offset=offset, type=method)
    end1 = time.time()

    print(proximity['id'].unique())

    m = folium.plot_trajectories(
        proximity, zoom_start=9, tile='OpenStreetMap')

    m = m._repr_html_()
    print(f'Time for querying trajectories: {end1-start1}')
    context = {
        'id': id,
        'map': m,
    }
    return render(request, 'dashboard/query.html', context)


'''
    以下为whale的
'''


# 查找特定轨迹
def special_query2(request):
    dictory = request.POST.get("sellist")
    list = dictory.split(':')
    id = list[0]
    color_dict = {list[0]: list[1]}
    qs = Whale.objects.filter(id=id)
    df = tools.change_to_df(qs)

    m = folium.plot_trajectories(
        df, zoom_start=4, tile='OpenStreetMap', color_by_id=color_dict)

    m = m._repr_html_()
    context = {
        'id': id,
        'map': m,
    }
    return render(request, 'dashboard/query.html', context)


# 查找相似轨迹
def similar_query2(request):
    id = request.POST.get("sellist")
    way = int(request.POST.get("way"))
    method = request.POST.get("method")
    offset = int(request.POST.get("offset"))
    print(id, way, method, offset)

    qs = Whale.objects.filter(id=id)
    checked_df = tools.change_to_df(qs)
    # print(checked_df['id'].unique())

    alist = Whale.objects.all()
    list_df = tools.change_to_df(alist)
    # print(list_df['id'].unique())

    start1 = time.time()
    proximity = core.data_query(
        checked_df, list_df, mode=way, offset=offset, type=method)
    end1 = time.time()

    print(proximity['id'].unique())

    m = folium.plot_trajectories(
        proximity, zoom_start=4, tile='OpenStreetMap')

    m = m._repr_html_()
    print(end1-start1)
    context = {
        'id': id,
        'map': m,
    }
    return render(request, 'dashboard/query.html', context)

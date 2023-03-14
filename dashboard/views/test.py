from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import tools
from dashboard.models import Elephant
from django_pandas.io import read_frame
from shapely.geometry import Point, LineString, Polygon
from geopandas import GeoDataFrame, read_file
import pandas as pd
from pymove import folium

num_progress = 0  # 当前的后台进度值（不喜欢全局变量也可以很轻易地换成别的方法代替）

# Create your views here.


def index(request):
    # ob = Elephant.objects.filter(id='175173')
    # df = read_frame(qs=ob)
    # # print(type(df))
    # # print(df.head())
    # df[['lon', 'lat']] = df[[
    #     'lon', 'lat']].apply(pd.to_numeric)

    # m = folium.plot_trajectories(
    #     df, zoom_start=9, tile='OpenStreetMap')

    # m = m._repr_html_()
    context = {
        # 'map': m
    }
    return render(request, 'dashboard/test.html', context)


def t1(request):
    qs = Elephant.objects.all()
    df = tools.change_to_df(qs)
    id_list = df['id'].unique()
    color_dist = tools.get_color(id_list)

    m = folium.plot_trajectories(
        df, zoom_start=9, tile='OpenStreetMap', color_by_id=color_dist)

    m = m._repr_html_()

    return HttpResponse(content=m)


'''
展示界面 UI
'''


def show_progress1(request):
    # return JsonResponse(num_progress, safe=False)
    return render(request, 'datahexun.html')


'''
后台实际处理程序
'''


def process_data(request):
    # ...
    global num_progress

    for i in range(12345666):
        # ... 数据处理业务
        num_progress = i * 100 / 12345666  # 更新后台进度值，因为想返回百分数所以乘100
        # print 'num_progress=' + str(num_progress)
        # time.sleep(1)
        res = num_progress
        # print 'i='+str(i)
        # print 'res----='+str(res)
    return JsonResponse(res, safe=False)


'''
前端JS需要访问此程序来更新数据
'''


def show_progress(request):
    print('show_progress----------'+str(num_progress))
    return JsonResponse(num_progress, safe=False)

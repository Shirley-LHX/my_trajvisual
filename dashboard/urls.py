from django.urls import path
from dashboard.views import index, test

urlpatterns = [
    path('', index.index, name="index"),
    path('Home/', index.Home, name="Home"),
    path('projects/hurricane', index.Hurricane, name="hurricane"),
    path('projects/bowhead_whale', index.Bowhead_whale, name="bowhead_whale"),
    path('projects/african_elephant',
         index.African_elephant, name="african_elephant"),
    path('test/', test.index, name='test'),
    path('tools/store', index.Store, name='store'),
    path('tools/upload', index.data_upload, name='data_upload'),
    path('query/special', index.special_query, name='special_query'),
    path('query/similar', index.similar_query, name='similar_query'),
    path('query/special2', index.special_query2, name='special_query2'),
    path('query/similar2', index.similar_query2, name='similar_query2'),
    path('test/t1', test.t1, name='t1'),

    # path('test/process_data', test.process_data, name='process_data'),
    # path('test/show_process1', test.show_progress1, name='show_progress1'),
    # path('test/show_process', test.show_progress, name='show_progress'),


]

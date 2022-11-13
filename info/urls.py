from django.contrib import admin
from django.urls import path
from info import views

app_name = 'info'
urlpatterns = [
    path('', views.index,name='index'),
    path('groups',views.groups,name='groups'),
    path('add',views.add,name='add'),
    path('creategroup',views.creategroup,name='creategroup'),
    path('post',views.post,name='post'),
    path('good/<int:good_id>',views.good,name='good'),
]

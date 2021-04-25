from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('update_graph_data', views.home, name="chart-test")
    # path('about/', views.about, name='blog-about'),
]
from django.contrib import admin
from django.urls import path, include
from .views import large_csv, index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('download/', large_csv, name='csv')
]

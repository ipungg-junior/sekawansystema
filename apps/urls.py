from django.contrib import admin
from django.urls import path, include
from apps.views import Landing, Demo

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    path('', Landing.as_view(context='')),
    path('demo/pge/', Demo.as_view(context='demo-pge')),
]

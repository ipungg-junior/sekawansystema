from django.contrib import admin
from django.urls import path, include
from apps.views import Landing

urlpatterns = [
    path('', Landing.as_view(context='')),
]

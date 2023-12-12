from django.contrib import admin
from django.urls import path, include
from blog.views import Blog

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    path('', Blog.as_view(context='')),
]

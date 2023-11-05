from django.urls import path
from demo.views import Demo

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    path('<str:client_name>/', Demo.as_view()),
]

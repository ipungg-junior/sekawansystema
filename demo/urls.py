from django.urls import path
from viewer.demo.main import DemoDirect

handler404 = 'apps.views.entry_not_found'

urlpatterns = [
    path('<str:client_name>/', DemoDirect.as_view()),
]

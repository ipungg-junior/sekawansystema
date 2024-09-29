from django.views import View
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR

class DemoDirect(View):

    def get(self, request, *args, **kwargs):
        client_name = kwargs.get("client_name")
        absolute_path = f'{BASE_DIR}/demo/templates/{client_name}/index.html'

        if not os.path.isfile(absolute_path):
            response = render(request, '404.html')
            response.status_code = 404
            return response

        return render(request, absolute_path)

from django.shortcuts import render
from django.views import View

def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)
# Create your views here.
class Demo(View):

    def get(self, request, client_name):
        return render(request, f'{client_name}/index.html')
    

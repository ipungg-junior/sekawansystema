from django.shortcuts import render
from django.views import View

def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)

# Create your views here.
class Landing(View):
    
    context = ''

    def get(self, request):
        return render(request, 'index.html')


class Demo(View):
    
    context = ''

    def get(self, request):
        return render(request, 'client-demo/pge/index.html')
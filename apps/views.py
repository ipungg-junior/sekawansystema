from django.shortcuts import render
from django.views import View

# Create your views here.
class Landing(View):
    
    context = ''

    def get(self, request):
        return render(request, "welcome")

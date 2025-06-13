from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    #  return HttpResponse("It's Done.")
    return render(request, 'home.html')
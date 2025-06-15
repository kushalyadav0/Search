from django.shortcuts import render
from .Zenserp_api import Perform_search 

# Create your views here.
def home(request):
    #  return HttpResponse("It's Done.")
    return render(request, 'home.html')

def search_view(request):
    results = {}
    if 'q' in request.GET:
        query = request.GET.get('q')
        search_type=request.GET.get('type', 'web')
        results = Perform_search(query, search_type)

        return render(request,'search.html', {'results': results})

    return render(request, 'search.html', {'results':results})
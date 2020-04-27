from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Route

def index(request):
    routes_list = Route.objects.order_by('-route_name')
    context = {
        'routes_list': routes_list,
    }
    return render(request, 'routeplanner/index.html', context)

def detail(request, route_name):
    #route = get_object_or_404(Route, pk=route_name)
    return HttpResponse("Route name: %s" % route_name)


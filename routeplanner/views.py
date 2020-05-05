from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import Route, World

def index(request):
    routes_list = Route.objects.order_by('-route_name')
    worlds_list = World.objects.order_by('-world_name')
    context = {
        'worlds_list': worlds_list,
        'routes_list': routes_list,
    }
    return render(request, 'routeplanner/index.html', context)

def detail(request, route_name):
    try:
        route = Route.objects.get(route_name__exact=route_name)
    except Route.DoesNotExist:
        raise Http404("Route does not exist...")

    return render(request, 'routeplanner/detail.html', {'route': route})


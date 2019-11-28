from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .models import Tour, Agent

def home(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    tours = Tour.objects.all()[:3]

    return render(request, 'home.html', context={ 'num_visits': num_visits, 'tours':tours})

def tour_detail(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        raise Http404('Tour not found')
    return render(request, 'tour_detail.html', {'tour': tour})

def agent_detail(request, id):
    try:
        agent = Agent.objects.get(id=id)
    except Agent.DoesNotExist:
        raise Http404('Agent not found or you are not a agent')
    return render(request, 'agent_detail.html', {'agent': agent})

def tours_by_agent(request):
    try:
        agent = Agent.objects.get(agent_username=request.user)
    except Agent.DoesNotExist:
        raise Http404('Agent not found')

    tours_agent = Tour.objects.filter(agent=agent)
    return render(request,'tours_by_agent.html', {'tours_agent': tours_agent})

from django.views import generic

class TourListView(generic.ListView):
    model = Tour
    paginate_by = 10

class AgentListView(generic.ListView):
    model = Agent
    paginate_by = 10


class TourDetailView(generic.DetailView):
    model = Tour


class AgentDetailView(generic.DetailView):
    model = Agent
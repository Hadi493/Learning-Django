from django.shortcuts import render # type: ignore
from .models import agentLists
from django.shortcuts import get_object_or_404 # type: ignore

# Create your views here.
def all_agents(request):
    agents = agentLists.objects.all()
    return render(request, 'all_agents.html', {'agents': agents})


def agent_detail(request, agent_id):
    agent = get_object_or_404(agentLists, pk=agent_id)
    return render(request, 'agent_detail.html', {'agent': agent})

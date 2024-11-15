from django.shortcuts import render # type: ignore

# Create your views here.
def all_agents(request):
    return render(request, 'all_agents.html')
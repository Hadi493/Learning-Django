from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.all_agents, name='all_agents'),
    path('<int:agent_id>', views.agent_detail, name='agent_detail')
]
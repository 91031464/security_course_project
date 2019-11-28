from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tours/', views.TourListView.as_view(), name='tours'),
    path('agents/', views.AgentListView.as_view(), name = 'agents'),
    path('tour/<int:pk>', views.TourDetailView.as_view(), name='tour_detail'),
    path('agent/<int:pk>', views.AgentDetailView.as_view(), name='agent_detail'),
    path('tours_by_agent/', views.tours_by_agent, name = 'tours_by_agent'),
]

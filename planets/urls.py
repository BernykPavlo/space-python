from django.urls import path
from .views import PlanetListView, PlanetDetailView, PlanetCreateView, PlanetUpdateView, PlanetDeleteView

urlpatterns = [
    path('', PlanetListView.as_view(), name='planet_list'),
    path('planets/', PlanetListView.as_view(), name='planet_list'),
    path('planet/<int:pk>/', PlanetDetailView.as_view(), name='planet_detail'),
    path('planet/new/', PlanetCreateView.as_view(), name='planet_new'),
    path('planet/<int:pk>/edit/', PlanetUpdateView.as_view(), name='planet_edit'),
    path('planet/<int:pk>/delete/', PlanetDeleteView.as_view(), name='planet_delete'),
]
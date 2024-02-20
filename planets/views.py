from django.db.models import Avg
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Planet

class PlanetListView(ListView):
    model = Planet
    context_object_name = 'planets'

    def get_context_data(self, **kwargs):
        context = super(PlanetListView, self).get_context_data(**kwargs)
        # Calculate the average of min and max distances for each planet and then the overall average
        avg_min_distance = Planet.objects.aggregate(Avg('min_distance_from_star'))['min_distance_from_star__avg']
        avg_max_distance = Planet.objects.aggregate(Avg('max_distance_from_star'))['max_distance_from_star__avg']
        if avg_min_distance or avg_max_distance:
            context['average_distance'] = (avg_min_distance + avg_max_distance) / 2
        else:
            context['average_distance'] = "Not available"
        # Average radius and orbital period can be directly calculated
        context['average_radius'] = Planet.objects.aggregate(Avg('radius'))['radius__avg']
        context['average_orbital_period'] = Planet.objects.aggregate(Avg('orbital_period'))['orbital_period__avg']
        return context

class PlanetDetailView(DetailView):
    model = Planet

class PlanetCreateView(CreateView):
    model = Planet
    fields = '__all__'
    success_url = reverse_lazy('planet_list')

class PlanetUpdateView(UpdateView):
    model = Planet
    fields = '__all__'
    success_url = reverse_lazy('planet_list')

class PlanetDeleteView(DeleteView):
    model = Planet
    context_object_name = 'planet'
    success_url = reverse_lazy('planet_list')
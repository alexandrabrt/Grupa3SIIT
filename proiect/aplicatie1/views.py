from django.shortcuts import render

# Create your views here.
# ListView => Afisare date
# CreateView => Adaugare date
# UpdateView => Modificare date
# DeleteView => Stergere date
from django.views.generic import ListView

from aplicatie1.models import Location


class HomeIndex(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'
    context_object_name = 'all_locations'

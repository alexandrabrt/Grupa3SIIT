from django.shortcuts import render

# Create your views here.
# ListView => Afisare date
# CreateView => Adaugare date
# UpdateView => Modificare date
# DeleteView => Stergere date
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.models import Location
from django.urls import reverse


class HomeIndex(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'
    context_object_name = 'all_locations'


class CreateIndexView(CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:home')


class UpdateLocationView(UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:home')
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
# ListView => Afisare date
# CreateView => Adaugare date
# UpdateView => Modificare date
# DeleteView => Stergere date
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.forms import LocationForm
from aplicatie1.models import Location
from django.urls import reverse


class HomeIndex(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'
    context_object_name = 'all_locations'


class CreateIndexView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'aplicatie1/location_form.html'

    def get_form_kwargs(self):
        kwargs = super(CreateIndexView, self).get_form_kwargs()
        kwargs.update({'pk': None})
        return kwargs

    def get_success_url(self):
        return reverse('aplicatie1:home')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    # fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'aplicatie1/location_form.html'

    def get_form_kwargs(self):
        kwargs = super(UpdateLocationView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs

    def get_success_url(self):
        return reverse('aplicatie1:home')
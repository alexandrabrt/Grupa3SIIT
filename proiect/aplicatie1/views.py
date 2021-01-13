from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
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

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(HomeIndex, self).get_context_data()
        data['all_locations'] = Location.objects.filter(active=1)
        # data['all_locations'] = Location.objects.exclude(active=0)
        return data


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


@login_required
def remove_location(request):
    data_source = {}
    print(request.GET.get('id_location'))
    # location_instance = Location.objects.get(id=str(request.GET.get('id_location')).split('-')[-1])
    # location_id = location_instance.id
    # location_instance.active = 0
    # location_instance.save()

    Location.objects.filter(id=str(request.GET.get('id_location')).split('-')[-1]).update(active=0)
    location = Location.objects.get(id=str(request.GET.get('id_location')).split('-')[-1], city__icontains='ro')
    # location_instance.delete()
    data_source['location'] = location.id
    data_source['name'] = f"Ai sters orasul {location.city} din tara {location.country}"
    print(data_source)
    return JsonResponse(data_source)
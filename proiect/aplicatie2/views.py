from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
# ListView => Afisare date
# CreateView => Adaugare date
# UpdateView => Modificare date
# DeleteView => Stergere date
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.forms import CompaniesForm
from aplicatie2.models import Companies


class HomeIndex(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'
    # context_object_name = 'all_companies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeIndex, self).get_context_data(**kwargs)
        print(self.request.user.userextend.customer.id)
        context['all_companies'] = Companies.objects.filter(id=self.request.user.userextend.customer.id)
        return context


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    # fields = ['name', 'website', 'type', 'active', 'location']
    form_class = CompaniesForm
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:home')


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    # fields = ['name', 'website', 'type', 'active', 'location']
    form_class = CompaniesForm
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:modificare', kwargs={'pk': self.kwargs['pk']})

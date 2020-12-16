from django import forms
from django.forms import TextInput, Select

from aplicatie2.models import Companies


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['name', 'website', 'type', 'active', 'location']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name of company', 'class': 'form-control'}),
            'website': TextInput(attrs={'placeholder': 'Website', 'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-control'}),
            'location': Select(attrs={'class': 'form-control'})
        }
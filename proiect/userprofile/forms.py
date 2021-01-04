from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First name of user', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name of user', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email of user', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username of user', 'class': 'form-control'}),
        }

    def __init__(self, pk, state, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.pk = pk
        self.state = state

    def clean(self):
        cleaned_data = self.cleaned_data
        email_val = cleaned_data.get('email')
        username_val = cleaned_data.get('username')
        if self.state == 'create':
            if User.objects.filter(email=email_val).exists():
                msg = 'Emailul deja exista, te rugam sa alegi un alt email'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_val).exists():
                msg = 'Username deja exista, te rugam sa alegi un alt email'
                self._errors['username'] = self.error_class([msg])
        elif self.state == 'update':
            if User.objects.filter(email=email_val).exclude(id=self.pk).exists():
                msg = 'Emailul deja exista, te rugam sa alegi un alt email'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_val).exclude(id=self.pk).exists():
                msg = 'Username deja exista, te rugam sa alegi un alt email'
                self._errors['username'] = self.error_class([msg])

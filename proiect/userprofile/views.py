import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from userprofile.models import Pontaj
import datetime
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import UpdateView, CreateView

from userprofile.forms import NewAccountForm
from userprofile.models import UserExtend


class UpdateProfile(LoginRequiredMixin, UpdateView):
    # fields = '__all__'
    form_class = NewAccountForm
    model = UserExtend
    template_name = 'aplicatie1/location_form.html'

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_form_kwargs(self):
        kwargs = super(UpdateProfile, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk'], 'state': 'update'})
        return kwargs

    def get_success_url(self):
        return reverse('aplicatie1:home')


punctuation = '!$%?#@'


class CreateNewUser(CreateView):
    form_class = NewAccountForm
    model = UserExtend
    template_name = 'aplicatie1/location_form.html'

    def get_form_kwargs(self):
        kwargs = super(CreateNewUser, self).get_form_kwargs()
        kwargs.update({'pk': None, 'state': 'create'})
        return kwargs

    def form_valid(self, form):
        print(form.errors)
        if form.is_valid():
            form.save(commit=False)
        return super(CreateNewUser, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateNewUser, self).form_invalid(form)

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + punctuation) for _ in range(8))
        try:
            user_instance = User.objects.get(id=self.object.id)
            user_instance.set_password(psw)
            user_instance.save()
            content_email = f'Your username and password: {user_instance.username} {psw}'
            msg_html = render_to_string('emails/invite_user.html', {'content_email': str(content_email)})
            msg = EmailMultiAlternatives(subject='Invite', body=content_email, from_email='contaxct@test.ro', to=[user_instance.email])
            msg.attach_alternative(msg_html, 'text/html')
            msg.send()
        except Exception:
            pass
        return reverse('login')

@login_required
def newPontaj(request):
    if Pontaj.objects.filter(user_id=request.user.id, end_date=None).exists() is False:
        Pontaj.objects.create(user_id=request.user.id, start_date=datetime.datetime.now())
    return redirect('aplicatie1:home')

@login_required
def stopPontaj(request, pk):
    if Pontaj.objects.filter(user_id=request.user.id, end_date=None).exists() is True:
        Pontaj.objects.filter(end_date=None, user_id=request.user.id).update(end_date=datetime.datetime.now())
    return redirect('aplicatie1:home')

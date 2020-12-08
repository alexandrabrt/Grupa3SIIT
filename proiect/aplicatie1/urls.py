from django.urls import path

from aplicatie1 import views

app_name = 'aplicatie1'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home")
]

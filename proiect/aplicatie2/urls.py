from django.urls import path

from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home"),
    path('add_companies/', views.CreateCompaniesView.as_view(), name="adaugare"),
    path('edit_companies/<int:pk>/', views.UpdateCompaniesView.as_view(), name="modificare"),
]

from django.urls import path

from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home"),
    path('add_companies/', views.CreateCompaniesView.as_view(), name="adaugare"),
    # path('edit_location/<int:pk>/', views.UpdateLocationView.as_view(), name="modificare"),
]

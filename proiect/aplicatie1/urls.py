from django.urls import path

from aplicatie1 import views

app_name = 'aplicatie1'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home"),
    path('add_location/', views.CreateIndexView.as_view(), name="adaugare"),
    path('edit_location/<int:pk>/', views.UpdateLocationView.as_view(), name="modificare"),
]

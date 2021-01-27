# myapi/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('/snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
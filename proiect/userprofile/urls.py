from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('updateprofile/<int:pk>/', views.UpdateProfile.as_view(), name='update_profile'),
    path('stop_pontaj/<int:pk>/', views.stopPontaj, name='stop'),
    path('new_account/', views.CreateNewUser.as_view(), name='new_account'),
    path('new_pontaj/', views.newPontaj, name='pontaj'),

]
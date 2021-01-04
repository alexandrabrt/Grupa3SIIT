from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('updateprofile/<int:pk>/', views.UpdateProfile.as_view(), name='update_profile'),
    path('new_account/', views.CreateNewUser.as_view(), name='new_account'),
]
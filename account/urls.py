from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
        path('registration', views.registration, name='registration'),
        path('details', views.profile_details, name='profile_details'),
]

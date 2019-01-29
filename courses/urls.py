from django.urls import path
from . import views
app_name = 'courses'

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('<slug:slug>', views.course_details, name='course_details'),
]

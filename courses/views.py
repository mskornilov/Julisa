from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.

def courses_list(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses_list.html', context)

def course_details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {'course': course}
    return render(request, 'courses/course_details.html', context)

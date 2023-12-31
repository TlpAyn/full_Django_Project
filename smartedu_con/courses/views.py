from django.shortcuts import render
from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all().order_by('-date')

    context = {
        'courses': courses
    }


    return render(request, 'courses.html', context)

def course_details(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)

    context = {
        'course': course
    }
    return render (request, 'course.html', context)

def category_list(request, category_slug):
    courses = Course.objects.all().filter(category__slug = category_slug)

    context = {
        'courses': courses
    }
    return render (request, 'courses.html', context)

def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug = tag_slug)
    categories = Category.objects.all()

    context = {
        'courses': courses
    }
    return render (request, 'courses.html', context)
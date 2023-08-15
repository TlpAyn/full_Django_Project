from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.course_list, name="courses"),
    path('<slug:category_slug>/<int:course_id>', views.course_details, name="course_detail"),

]

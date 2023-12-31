from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.course_list, name="courses"),
    path('<slug:category_slug>/<int:course_id>', views.course_details, name="course_detail"),
    path('categories/<slug:category_slug>', views.category_list, name="courses_by_category"),
   # path('tags/<slug:category_slug>', views.tag_list, name="courses_by_tag"),

]

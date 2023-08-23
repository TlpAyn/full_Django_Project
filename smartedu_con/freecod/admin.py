from django.contrib import admin
from .models import Freecode

@admin.register(Freecode)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    





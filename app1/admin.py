from django.contrib import admin
from app1.models import course,create

# Register your models here.



@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display = ['id','subjects','duration','fee']



@admin.register(create)
class createAdmin(admin.ModelAdmin):
    list_display = ['id','sname','subject','fee']


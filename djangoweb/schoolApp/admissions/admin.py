from django.contrib import admin
from admissions.models import students
from admissions.models import Teacher

class studentadmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','contact']
# Register your models here.

class Teacheradmin(admin.ModelAdmin):
    list_display=['id','name','exp','subject','contact']
admin.site.register(students,studentadmin)
admin.site.register(Teacher,Teacheradmin)

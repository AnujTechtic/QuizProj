from django.contrib import admin
from .models import Students, Questions, Results, Departments, Quizs
# Register your models here.
admin.site.register(Students)
admin.site.register(Departments)
admin.site.register(Quizs)
admin.site.register(Questions)
admin.site.register(Results)
from django.contrib import admin

# Register your models here.
from  .models import *
admin.site.register(StudentElective)
admin.site.register(Department)
admin.site.register(Scheme)     
admin.site.register(Semester)
admin.site.register(Subject)
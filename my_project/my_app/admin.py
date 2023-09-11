from django.contrib import admin
from .models import Students
from .models import Department

# Register your models here.
admin.site.register(Students)
admin.site.register(Department)

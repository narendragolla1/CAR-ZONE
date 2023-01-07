from django.contrib import admin
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display=('car_title','color','model','year','milage','is_featured')
    
    
    list_editable=('is_featured','milage')

admin.site.register(Car,CarAdmin)
from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:10px" />'.format(object.photo.url))
    thumbnail.short_description='photo'
    list_display=('id','thumbnail','first_name','last_name','designation','create_date')
    list_display_links=('first_name','thumbnail')
    search_fields=('first_name','last_name','designation')
    list_filter=('designation',)

admin.site.register(Team,TeamAdmin)
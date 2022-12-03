from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        html_code = '<img src = "{}" width="40" style="border-radius: 50px;"/>'
        return format_html(html_code.format(object.photo.url))
    
    search_fields = ('first_name', 'last_name', 'designation')
    list_display = ('thumbnail','first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('first_name', 'last_name', 'thumbnail')
    list_filter = ('designation',)
# Register your models here.
admin.site.register(Team, TeamAdmin)

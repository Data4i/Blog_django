from django.contrib import admin

# Register your models here.

from .models import Blog, Email

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title', 'created_on', 'updated_on']
    list_display_links = ['id', 'slug', 'title', 'created_on', 'updated_on']
    
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display= ['email', 'subject']
    
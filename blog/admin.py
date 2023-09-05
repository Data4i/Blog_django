from django.contrib import admin

# Register your models here.

from .models import Blog, Category

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title', 'created_on', 'updated_on']
    list_display_links = ['id', 'slug', 'title', 'created_on', 'updated_on']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug']
    list_display_links = list_display   

    
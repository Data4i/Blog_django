from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(args, kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Blog Title')
    categories = models.ForeignKey(Category, on_delete = models.CASCADE)
    slug = models.SlugField(max_length=300, blank = True)
    content = models.TextField(verbose_name='Blog Content', blank=True)
    view_counts = models.PositiveIntegerField(default = 0) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'My Contents'
        ordering = ['-view_counts','-updated_on']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(args, kwargs)

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Blog Title')
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
    
class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    responded_to = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    
    
    def __str__(self) -> str:
        return f'About: {self.subject}'
    
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Blog Title')
    content = models.TextField(verbose_name='Blog Content', blank=True)
    view_counts = models.PositiveIntegerField(null = True) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'My Contents'
    
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
    
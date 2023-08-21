from django.urls import path
from .views import blog_detail, blog_view, create_blog

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'all_blogs'),
    path('create', create_blog, name = 'create_blog'),
    path('blog_detail/<int:id>/', blog_detail, name='blog_details'),
]

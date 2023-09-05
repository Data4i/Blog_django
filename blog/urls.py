from django.urls import path
from .views import blog_detail, blog_view, create_blog, update_blog, all_categories

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'all_blogs'),
    path('create', create_blog, name = 'create_blog'),
    path('update/<str:slug>/', update_blog, name = 'update_blog'),
    path('blog_detail/<str:slug>/', blog_detail, name='blog_details'),
    path('all_cats/', all_categories, name = 'categories')
]

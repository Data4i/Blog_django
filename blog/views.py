from django.shortcuts import redirect, render

from .forms import BlogForm
from .models import Blog, Category

def blog_view(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, slug):
    blog = Blog.objects.get(slug = slug)
    blog.view_counts += 1
    blog.save()
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_details.html', context)

def all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    
    return render(request, 'blog/categories.html', context)

def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:all_blogs")
    else:
        form = BlogForm()
    
    context = {
        'form': form
    }           
    
    return render(request, 'blog/blog_form.html', context) 

def update_blog(request, slug):
    blog = Blog.objects.get(slug = slug)
    form = BlogForm(instance = blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('blog:all_blogs')
    context = {
        'form': form
    }
    
    return render(request, 'blog/blog_form.html', context)       

def delete_blog(request, slug):
    blog = Blog.objects.get(slug = slug)
    blog.delete()
    return redirect('blog:all_blogs')

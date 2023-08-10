from django.shortcuts import render

def home_view(request):
    return render(request, 'blog/home.html')

def blog_view(request):
    return render(request, 'blog/blog.html')
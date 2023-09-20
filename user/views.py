from django.shortcuts import render, redirect

from user.forms import LoginForm

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:all_blogs')

    context = {
        "form": form,
    }
    
    return render(request, 'user/login.html', context)
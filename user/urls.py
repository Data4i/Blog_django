from django.urls import path

app_name = "accounts"

from .views import login

urlpatterns = [
    path('login/', login, name = 'login'),
    
]

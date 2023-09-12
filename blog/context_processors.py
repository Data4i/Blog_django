from .models import Category

def contexts(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }
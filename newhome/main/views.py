from django.shortcuts import render
from .models import Items, Identity, Category

# Create your views here.


def index(request):
    base_items = Items.objects.all()
    base_category = Category.objects.all()
    base_identity = Identity.objects.all()

    return render(request, 'index.html', context={'items':base_items, 'category':base_category, 'identity':base_identity})
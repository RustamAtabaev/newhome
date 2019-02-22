from django.shortcuts import render
from django.views import generic
from .models import Catalog, CatalogItems, SliderA, News

# Create your views here.


def index(request):
        catalog_category = Catalog.objects.all()
        catalog_category_items = CatalogItems.objects.all()
        sliderA = SliderA.objects.all()
        news = News.objects.all()



        return render(request, 'base.html', context={
                'catalog_category': catalog_category, 
                'catalog_category_items': catalog_category_items, 
                'sliderA': sliderA,
                'news': news,
                
                })

from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.


def index(request):
        catalog_category = Catalog.objects.all()
        catalog_category_items = CatalogItems.objects.all()
        sliderA = SliderA.objects.all()
        news = News.objects.all()
        foto = Foto.objects.all()
        recomend = Recomend.objects.all()
        working_time = WorkingTime.objects.all()
        adress = Adress.objects.all()
        hmenu = Hmenu.objects.all()[:5]
        hmenu_items = HmenuItems.objects.all()



        return render(request, 'base.html', context={
                'catalog_category': catalog_category, 
                'catalog_category_items': catalog_category_items, 
                'sliderA': sliderA,
                'news': news,
                'foto': foto,
                'recomend': recomend,
                'working_time': working_time,
                'adress': adress,
                'hmenu': hmenu,
                'hmenu_items': hmenu_items,
                })

def index1(request):
        catalog_category = Catalog.objects.all()
        catalog_category_items = CatalogItems.objects.all()
        sliderA = SliderA.objects.all()
        news = News.objects.all()
        foto = Foto.objects.all()
        recomend = Recomend.objects.all()
        working_time = WorkingTime.objects.all()
        adress = Adress.objects.all()
        hmenu = Hmenu.objects.all()[:5]
        hmenu_items = HmenuItems.objects.all()



        return render(request, 'base.html', context={
                'catalog_category': catalog_category, 
                'catalog_category_items': catalog_category_items, 
                'sliderA': sliderA,
                'news': news,
                'foto': foto,
                'recomend': recomend,
                'working_time': working_time,
                'adress': adress,
                'hmenu': hmenu,
                'hmenu_items': hmenu_items,
                })

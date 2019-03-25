from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.


def index(request, slug_name=''):
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


def show_detail_catalog(request, slug_cat, slug_sub_cat):
        catalog_get = Catalog.objects.get(slug=slug_cat)
        catalog_category_items = CatalogItems.objects.filter(catalog_same=catalog_get.id)

        catalog_sub_get = CatalogItems.objects.get(slug=slug_sub_cat)
        cards = Detail_Items.objects.filter(detail_cat=catalog_sub_get.id)
        
        news = News.objects.all()
        foto = Foto.objects.all()
        recomend = Recomend.objects.all()
        working_time = WorkingTime.objects.all()
        adress = Adress.objects.all()
        hmenu = Hmenu.objects.all()[:5]
        hmenu_items = HmenuItems.objects.all()

        return render(request, 'detail_catalog.html', context={
                'slug_cat': slug_cat,
                'slug_sub_cat': slug_sub_cat,
                'catalog_category_items': catalog_category_items,
                'cards': cards,

                'news': news,
                'foto': foto,
                'recomend': recomend,
                'working_time': working_time,
                'adress': adress,
                'hmenu': hmenu,
                'hmenu_items': hmenu_items,
        })


def show_detail_item(request, slug_cat, slug_sub_cat, slug_item):
        item_fields = Detail_Items.objects.get(slug=slug_item)
        
        news = News.objects.all()
        foto = Foto.objects.all()
        recomend = Recomend.objects.all()
        working_time = WorkingTime.objects.all()
        adress = Adress.objects.all()
        hmenu = Hmenu.objects.all()[:5]
        hmenu_items = HmenuItems.objects.all()

        return render(request, 'detail_view.html', context={

                'item_fields': item_fields,

                'news': news,
                'foto': foto,
                'recomend': recomend,
                'working_time': working_time,
                'adress': adress,
                'hmenu': hmenu,
                'hmenu_items': hmenu_items,
        })
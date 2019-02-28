from django.contrib import admin
from django.db import models
from .models import Catalog, CatalogItems, SliderA, News, Foto, Recomend, MyInlineModel

# Register your models here.
# @admin.register(Items)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'amount')
#     list_filter = ('title', 'description', )
#     list_per_page = 2

# @admin.register(Catalog)
# class CatalogAdmin(admin.ModelAdmin):
#     list_display = ('catalog_title', 'catalog_icon')

@admin.register(CatalogItems)
class CatalogItemsAdmin(admin.ModelAdmin):
    pass

@admin.register(SliderA)
class SliderAAdmin(admin.ModelAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    pass

@admin.register(Recomend)
class RecomendAdmin(admin.ModelAdmin):
    pass

@admin.register(Catalog)
class ModelOptions(admin.ModelAdmin):
    fieldsets = (
        ('11', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('catalog_title',),
        }),
        ('Flags', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ('catalog_icon',),
        }),
    )
    ordering = ('catalog_title',)








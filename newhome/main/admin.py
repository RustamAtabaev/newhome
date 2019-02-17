from django.contrib import admin
from .models import Catalog, CatalogItems

# Register your models here.
# @admin.register(Items)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'amount')
#     list_filter = ('title', 'description', )
#     list_per_page = 2

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('catalog_title', 'catalog_icon')

@admin.register(CatalogItems)
class CatalogItemsAdmin(admin.ModelAdmin):
    pass



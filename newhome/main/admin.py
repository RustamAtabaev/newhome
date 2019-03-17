from django.contrib import admin
from django.db import models
from adminsortable2.admin import SortableAdminMixin
from .models import *

# Register your models here.
# @admin.register(Items)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'amount')
#     list_filter = ('title', 'description', )
#     list_per_page = 2

@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
    list_display = ('header_info_title',)
    fieldsets = (
        (WorkingTime.week_header, {
            'fields':[('wk_start_week', 'wk_end_week')]
        }),
        (WorkingTime.sat_header, {
            'fields':[('sat_start_week', 'sat_end_week')]
        }),
        (WorkingTime.sun_header, {
            'fields':[('sun_start_week', 'sun_end_week')]
        }),
    )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    # list_display = ('header_info_title',)
    fieldsets = (
        ('', {
            'fields':['common_header',]
        }),
        (Adress.first_header, {
            'fields':['first_adress_header', ('first_number', 'first_email')]
        }),
        (Adress.second_header, {
            'fields':['second_adress_header', ('second_number', 'second_email')]
        }),
    )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Hmenu)
class HmenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('hmenu_title', 'hmenu_order',)

@admin.register(HmenuItems)
class HmenuItemsAdmin(admin.ModelAdmin):
    pass


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
class CatalogOptions(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('catalog_title', 'catalog_icon', 'catalog_order',)








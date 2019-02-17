from django.contrib import admin
from .models import Items, Category, Identity

# Register your models here.
@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount')
    list_filter = ('title', 'description', )
    list_per_page = 2

@admin.register(Category)
class IteamCategory(admin.ModelAdmin):
    pass

@admin.register(Identity)
class IdentityAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Items, ItemAdmin)



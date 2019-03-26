from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainViews.index, name='index',),
    path('<slug:slug_cat>/<slug:slug_sub_cat>/', MainViews.show_detail_catalog, name='category'),
    path('<slug:slug_cat>/<slug:slug_sub_cat>/<slug:slug_item>', MainViews.show_detail_item, name='detail'),
]




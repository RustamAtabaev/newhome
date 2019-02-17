from django.urls import path, include
from .views import index
# from .views import index

urlpatterns = [
    path('', index, name='index',)
]
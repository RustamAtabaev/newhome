from django import template

# Импортируем нужные нам модели.
from main.models import Catalog, CatalogItems, SliderA, HmenuItems

# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()

# регистрируем наш тег, который будет выводить шаблон menu.html
# В кавычках вводите путь до шаблона! он может быть у каждого свой!


@register.simple_tag
def database_filter(value):
  res = CatalogItems.objects.filter(
      catalog_same__catalog_title=value.catalog_title)
  return res

@register.simple_tag
def hmenu_filter(value):
  res = HmenuItems.objects.filter(
      hmenu_same__hmenu_title=value.hmenu_title)
  return res

@register.filter
def cut_ext(value: str):
  cut: str = value[:-4:]
  res: str = cut + "-resized.jpg"
  return res


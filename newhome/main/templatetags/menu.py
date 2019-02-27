from django import template

from main.models import Catalog, CatalogItems #Импортируем нужные нам модели.

# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()

# регистрируем наш тег, который будет выводить шаблон menu.html
 #В кавычках вводите путь до шаблона! он может быть у каждого свой!

@register.simple_tag
def database_filter(value):
  res = CatalogItems.objects.filter(catalog_same__catalog_title=value.catalog_title)
  return res
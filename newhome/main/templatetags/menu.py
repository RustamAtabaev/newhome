from django import template

from main.models import Catalog, CatalogItems #Импортируем нужные нам модели.

# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()

# регистрируем наш тег, который будет выводить шаблон menu.html
 #В кавычках вводите путь до шаблона! он может быть у каждого свой!

# Создаем сам тег!
def test_menu():
  widgets = RightSidebarWidgets.objects.all() # Делаем выборку из БД
  return {'widgets': widgets} # Возвращаем контекст

@register.simple_tag
def hello(value):
  res = CatalogItems.objects.filter(catalog_same__catalog_title=value.catalog_title)
  return res
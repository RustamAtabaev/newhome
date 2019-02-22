from django.db import models
from django.forms import forms

# Create your models here.

class Catalog(models.Model):
    class Meta:
        verbose_name = u"Категории"
        verbose_name_plural = u"Категории"
    catalog_title = models.CharField(max_length=200, help_text="Название категории")
    catalog_title.verbose_name = u"Название категории"
    catalog_icon = models.CharField(max_length=200, help_text="Класс иконки. Пример: fas fa-stream")
    catalog_icon.verbose_name = u"Иконка категории"

    def __str__(self):
        return self.catalog_title

class CatalogItems(models.Model):
    class Meta:
        verbose_name = u"ПодКатегории"
        verbose_name_plural = u"ПодКатегории"
    catalog_same = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True)
    item_title = models.CharField(max_length=200, help_text="Название подкатегории")
    item_title.verbose_name = u"Название подкатегории"
    
    def __str__(self):
        return self.item_title

class SliderA(models.Model):
    class Meta:
        verbose_name = u"Слайдер"
        verbose_name_plural = u"Слайдер"
    slider_title_needed = models.BooleanField(u"Нужна ли подпись к слайду?")
    slider_title = models.CharField(max_length=200, help_text="Заголовок акции")
    slider_img_path = models.ImageField()
    
    def __str__(self):
        return self.slider_title

from django.db import models
from django_thumbs.fields import ImageThumbsField

# Create your models here.


class WorkingTime(models.Model):
    class Meta:
        verbose_name = u"Время работы"
        verbose_name_plural = u"Время работы"
    header_info_title = "Время работы"
    week_header = "Время работы по будням"
    sat_header = "Время работы по субботам"
    sun_header = "Время работы по воскресеньям"
    wk_start_week = models.TimeField(
        verbose_name='Время начала рабочего дня:', auto_now=False, auto_now_add=False, blank=True)
    wk_end_week = models.TimeField(
        verbose_name='Время завершения рабочего дня:', auto_now=False, auto_now_add=False, blank=True)
    sat_start_week = models.TimeField(
        verbose_name='Время начала рабочего дня:', auto_now=False, auto_now_add=False, blank=True)
    sat_end_week = models.TimeField(
        verbose_name='Время завершения рабочего дня:', auto_now=False, auto_now_add=False, blank=True)
    sun_start_week = models.TimeField(
        verbose_name='Время начала рабочего дня:', auto_now=False, auto_now_add=False, blank=True)
    sun_end_week = models.TimeField(
        verbose_name='Время завершения рабочего дня:', auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.header_info_title


class Adress(models.Model):
    class Meta:
        verbose_name = u"Адреса магазинов"
        verbose_name_plural = u"Адреса магазинов"
    header_info_adress = "Адреса магазинов"
    first_header = "Первый адрес"
    second_header = "Второй адрес"
    common_header = models.CharField(
        verbose_name='Общий заголовок:', max_length=200,)
    
    first_adress_header = models.CharField(
        verbose_name='Первый адрес:', max_length=200,)
    first_number = models.CharField(
        verbose_name='Первый номер:', max_length=200,)
    first_email = models.EmailField(
        verbose_name='Первый email:', max_length=200,)
   
    second_adress_header = models.CharField(
        verbose_name='Второй адрес:', max_length=200,)
    second_number = models.CharField(
        verbose_name='Второй номер:', max_length=200,)
    second_email = models.EmailField(
        verbose_name='Второй email:', max_length=200,)

    def __str__(self):
        return self.header_info_adress

class Hmenu(models.Model):
    class Meta(object):
        verbose_name = u"Меню"
        verbose_name_plural = u"Меню"
        ordering = ['hmenu_order']
    hmenu_title = models.CharField(
        max_length=200,)
    hmenu_title.verbose_name = u"Название пункта меню"
    hmenu_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.hmenu_title

class HmenuItems(models.Model):
    class Meta:
        verbose_name = u"Пункты меню"
        verbose_name_plural = u"Пункты меню"
    hmenu_same = models.ForeignKey(
        Hmenu, on_delete=models.SET_NULL, null=True)
    item_title = models.CharField(
        max_length=200, help_text="Название пункта меню")
    item_title.verbose_name = u"Название пункта меню"

    def __str__(self):
        return self.item_title

class Catalog(models.Model):
    class Meta(object):
        verbose_name = u"Категории"
        verbose_name_plural = u"Категории"
        ordering = ['catalog_order']
    catalog_title = models.CharField(
        max_length=200, help_text="Название категории")
    catalog_title.verbose_name = u"Название категории"
    catalog_icon = models.CharField(
        max_length=200, help_text="Класс иконки. Пример: fas fa-stream")
    catalog_icon.verbose_name = u"Иконка категории"
    catalog_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    def __str__(self):
        return self.catalog_title


class CatalogItems(models.Model):
    class Meta:
        verbose_name = u"ПодКатегории"
        verbose_name_plural = u"ПодКатегории"
    catalog_same = models.ForeignKey(
        Catalog, on_delete=models.SET_NULL, null=True)
    item_title = models.CharField(
        max_length=200, help_text="Название подкатегории")
    item_title.verbose_name = u"Название подкатегории"

    def __str__(self):
        return self.item_title


class SliderA(models.Model):

    SIZES = (
        {'code': 'resized', 'wxh': '800x400', 'resize': 'crop'},
    )

    class Meta:
        verbose_name = u"Слайдер"
        verbose_name_plural = u"Слайдер"
    slider_title_needed = models.BooleanField(u"Нужна ли подпись к слайду?")
    slider_title = models.CharField(
        max_length=200, help_text="Заголовок акции")
    slider_img_path = ImageThumbsField(
        upload_to="main/img/slider/", sizes=SIZES)

    def __str__(self):
        return self.slider_title


class News(models.Model):
    SIZES = (
        {'code': 'resized', 'wxh': '800x600', 'resize': 'crop'},
    )

    class Meta:
        verbose_name = u"Новостные акции"
        verbose_name_plural = u"Новостные акции"
    news_img = ImageThumbsField(
        upload_to="main/img/news/", help_text="Изображения новости", default='def', sizes=SIZES)
    news_title = models.CharField(
        max_length=200, help_text="Заголовок новости")
    news_description = models.TextField(max_length=400)
    news_text = models.TextField()

    def __str__(self):
        return self.news_title


class Foto(models.Model):
    SIZES = (
        {'code': 'resized', 'wxh': '800x400', 'resize': 'crop'},
    )

    class Meta:
        verbose_name = u"Фотографии магазинов"
        verbose_name_plural = u"Фотографии магазинов"
    foto_title = models.CharField(
        max_length=200, help_text="Альтернатива", default='def')
    foto_img1 = ImageThumbsField(
        upload_to="main/img/foto/", help_text="1-ая", default='def', sizes=SIZES)
    foto_img2 = ImageThumbsField(
        upload_to="main/img/foto/", help_text="2-ая", default='def', sizes=SIZES)
    foto_img3 = ImageThumbsField(
        upload_to="main/img/foto/", help_text="3-я", default='def', sizes=SIZES)

    def __str__(self):
        return self.foto_title


class Recomend(models.Model):

    SIZES = (
        {'code': 'resized', 'wxh': '400x400', 'resize': 'crop'},
    )

    class Meta:
        verbose_name = u"Рекомендации"
        verbose_name_plural = u"Рекомендации"
    recomend_title = models.CharField(
        max_length=200, help_text="Заголовок", default='def')
    recomend_img = ImageThumbsField(
        upload_to="main/img/recomend/", help_text="картинка рекомендаций", default='def', sizes=SIZES)

    def __str__(self):
        return self.recomend_title



# Ниже идут блоки детального обзора каталога каталога

class DitailMenu(models.Model):
    class Meta:
        verbose_name = u""
        verbose_name_plural = u"Фотографии магазинов"
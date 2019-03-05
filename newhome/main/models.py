from django.db import models
from django_thumbs.fields import ImageThumbsField

# Create your models here.


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
        verbose_name = u"Новостные акуции"
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

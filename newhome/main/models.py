from django.db import models

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
    slider_img_path = models.ImageField(upload_to = "main/img/slider/")
    
    def __str__(self):
        return self.slider_title

class News(models.Model):
    class Meta:
        verbose_name = u"Новостные акуции"
        verbose_name_plural = u"Новостные акции"
    news_img = models.ImageField(upload_to = "main/img/news/", help_text="Изображения новости", default='def')
    news_title = models.CharField(max_length=200, help_text="Заголовок новости")
    news_description = models.TextField(max_length=400)
    news_text = models.TextField()
    
    def __str__(self):
        return self.news_title

class Foto(models.Model):
    class Meta:
        verbose_name = u"Фотографии магазинов"
        verbose_name_plural = u"Фотографии магазинов"
    foto_title = models.CharField(max_length=200, help_text="Альтернатива", default='def')
    foto_img1 = models.ImageField(upload_to = "main/img/foto/", help_text="1-ая", default='def')
    foto_img2 = models.ImageField(upload_to = "main/img/foto/", help_text="2-ая", default='def')
    foto_img3 = models.ImageField(upload_to = "main/img/foto/", help_text="3-я", default='def')
    def __str__(self):
        return self.foto_title

class Recomend(models.Model):
    class Meta:
        verbose_name = u"Рекомендации"
        verbose_name_plural = u"Рекомендации"
    recomend_title = models.CharField(max_length=200, help_text="Заголовок", default='def')
    recomend_img = models.ImageField(upload_to = "main/img/recomend/", help_text="картинка рекомендаций", default='def')

    def __str__(self):
        return self.recomend_title
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, help_text="Category")

    def __str__(self):
        return self.title

class Identity(models.Model):
    identity = models.TextField(help_text="uniq identity")

    def __str__(self):
        return self.identity

class Items(models.Model):
    title = models.CharField(max_length=200, help_text="Name of product")
    description = models.TextField(help_text="Description of product")
    amount = models.IntegerField(help_text="Total product amount")
    # Добавление элементов из классов выше
    # Добавление обьекта - все для всех
    category = models.ManyToManyField(Category, help_text="Choose category") 
    # Добавление обьекта - один для нескольких
    identity = models.ForeignKey(Identity, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title



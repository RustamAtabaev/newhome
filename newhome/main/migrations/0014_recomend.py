# Generated by Django 2.1.7 on 2019-02-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190222_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomend_title', models.CharField(default='def', help_text='Заголовок', max_length=200)),
                ('recomend_img', models.ImageField(default='def', help_text='картинка рекомендаций', upload_to='main/img/recomend/')),
            ],
            options={
                'verbose_name': 'Рекомендации',
                'verbose_name_plural': 'Рекомендации',
            },
        ),
    ]
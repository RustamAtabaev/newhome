# Generated by Django 2.1.7 on 2019-02-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190221_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(help_text='Заголовок новости', max_length=200)),
                ('news_description', models.TextField(max_length=400)),
                ('news_text', models.TextField()),
            ],
            options={
                'verbose_name': 'Новостные акуции',
                'verbose_name_plural': 'Новостные акции',
            },
        ),
    ]
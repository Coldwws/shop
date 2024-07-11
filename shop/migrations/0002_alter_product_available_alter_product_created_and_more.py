# Generated by Django 5.0.6 on 2024-07-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='В Наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(verbose_name='На складе'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновление'),
        ),
    ]
# Generated by Django 4.2.2 on 2024-06-23 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Введите заголовок статьи.', max_length=50, null=True, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, help_text='Введите URL статьи.', max_length=100, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, help_text='Введите статью.', null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, help_text='Добавьте изображение.', null=True, upload_to='catalog/image', verbose_name='Превью статьи')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('published', models.BooleanField(blank=True, verbose_name='Опубликована')),
                ('views_counter', models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(blank=True, help_text='Укажите создателя карточки продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddField(
            model_name='product',
            name='views_counter',
            field=models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик просмотров'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Выберите категорию.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='catalog', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Введите описание.', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте изображение продукта.', null=True, upload_to='catalog/image', verbose_name='Изображение продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена за покупку'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, help_text='Введите наименование продукта.', max_length=50, null=True, verbose_name='Наименование'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.PositiveIntegerField(default=1, help_text='Укажите номер версии.', verbose_name='Номер версии')),
                ('title', models.CharField(blank=True, help_text='Введите название версии.', max_length=50, null=True, verbose_name='Название версии')),
                ('currented', models.BooleanField(blank=True, verbose_name='Текущая версия')),
                ('product', models.ForeignKey(blank=True, help_text='Продукты данной версии:', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='versions', to='catalog.product', verbose_name='Продукты данной версии')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
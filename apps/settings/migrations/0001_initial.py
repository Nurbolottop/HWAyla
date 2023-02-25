# Generated by Django 4.1.7 on 2023-02-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название сайта')),
                ('descriptions', models.TextField(verbose_name='Описание сайта')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип сайта')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефонный номер')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Ваша Почта')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ваш Адрес')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Ваш Instagram')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Ваш Facebook')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Ваш Youtube')),
            ],
            options={
                'verbose_name': ('Настройка',),
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]

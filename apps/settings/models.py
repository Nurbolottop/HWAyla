from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    phone = models.CharField(
        max_length=30,
        verbose_name="Телефонный номер",
        blank=True,null=True
    )
    email = models.EmailField(
        verbose_name="Ваша Почта",
        blank=True,null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Ваш Адрес",
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name="Ваш Instagram",
        blank=True,null=True
    )
    facebook = models.URLField(
        verbose_name="Ваш Facebook",
        blank=True,null=True
    )
    youtube = models.URLField(
        verbose_name="Ваш Youtube",
        blank=True,null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки",
        verbose_name_plural = "Настройка"
        
class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Наша история",
        blank=True,null=True
    )
    
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = "О нас",
        verbose_name_plural = "О нас"
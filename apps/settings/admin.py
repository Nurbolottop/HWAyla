from django.contrib import admin

from .models import Settings,About
# Register your models here.
admin.site.register(Settings)
admin.site.register(About)
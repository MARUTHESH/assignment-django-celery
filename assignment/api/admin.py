from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.DataModel)
class DataModelAdmin(admin.ModelAdmin):
    list_display = ['email']

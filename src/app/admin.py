from django.contrib import admin

from . import models


# Admin
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from demo.models import Photo
from sorl.thumbnail.admin import AdminImageMixin

class PhotoAdmin(AdminImageMixin,admin.ModelAdmin):
    pass

admin.site.register(Photo,PhotoAdmin)
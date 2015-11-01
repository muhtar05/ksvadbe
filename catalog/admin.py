from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from catalog.models import Category,Firm,City,Product,ProductPhoto
from sorl.thumbnail.admin import AdminImageMixin

class CustomMPTTModelAdmin(MPTTModelAdmin):
    prepopulated_fields = {"alt_name": ("name",)}
    list_display = ('name','alt_name')

class FirmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"alt_title": ("title",)}

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"alt_name": ("name",)}

class ProductAdmin(AdminImageMixin,admin.ModelAdmin):
    prepopulated_fields = {"alt_title": ("title",)}

class ProductPhotoAdmin(AdminImageMixin,admin.ModelAdmin):
    pass

admin.site.register(Category,CustomMPTTModelAdmin)
admin.site.register(Firm,FirmAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductPhoto,ProductPhotoAdmin)

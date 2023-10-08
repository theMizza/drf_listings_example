from django.contrib import admin
from .models import Listings, Categories
from django_mptt_admin.admin import DjangoMpttAdmin
# Register your models here.


class CategoriesAdmin(DjangoMpttAdmin):
    pass


admin.site.register(Listings)
admin.site.register(Categories, CategoriesAdmin)


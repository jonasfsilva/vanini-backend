from django.contrib import admin

from catalog.models import Category
from catalog.models import Model
from catalog.models import Product
from catalog.models import ProductGalery
from core.admin import BaseSuperAdmin


@admin.register(Category)
class CategoryClass(BaseSuperAdmin):
    ...
    

@admin.register(Model)
class ModelClass(BaseSuperAdmin):
    ...


@admin.register(Product)
class ProductClass(BaseSuperAdmin):
    ...


@admin.register(ProductGalery)
class ProductGaleryClass(BaseSuperAdmin):
    ...

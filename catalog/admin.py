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


class ProductCategoryInline(admin.StackedInline):
    model = ProductGalery 
    extra = 0
    exclude = ("deleted", "deleted_at", "another_position")


@admin.register(Product)
class ProductClass(BaseSuperAdmin):
    inlines = [ProductCategoryInline,]


@admin.register(ProductGalery)
class ProductGaleryClass(BaseSuperAdmin):
    list_display = ("product", "order", )

from django.db import models
from core.models import BaseModel


class Model(BaseModel):
    name = models.CharField(verbose_name="Nome")
    
    def __str__(self) -> str:
        return self.name


class Category(BaseModel):
    name = models.CharField(verbose_name="Nome")
    image = models.ImageField(verbose_name="Imagem")
    
    def __str__(self) -> str:
        return self.name


class Product(BaseModel):

    name = models.CharField(verbose_name="Nome", max_length=100)
    description = models.TextField(verbose_name="Description")
    model = models.ForeignKey(
        Model, verbose_name="Modelo", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self) -> str:
        return self.name


class ProductGalery(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name="Produto", related_name="images")
    image = models.ImageField(upload_to="products/images/")
    order = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Galeria Produto"
        verbose_name_plural = "Galerias de Produtos"

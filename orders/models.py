from django.db import models

from catalog.models import Model
from core.models import BaseModel
from location.models import State


class QuotationInfo(BaseModel):

    name = models.CharField(verbose_name="Nome", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)
    ddd = models.CharField(verbose_name="DDD", max_length=3)
    phone = models.CharField(verbose_name="Telefone", max_length=15)
    address = models.CharField(verbose_name="Endereço", max_length=150)
    number = models.CharField(verbose_name="Numero", max_length=6)
    zipcode = models.CharField(verbose_name="CEP", max_length=100)
    city = models.CharField(verbose_name="Cidade", max_length=100)
    district = models.CharField(verbose_name="CEP", max_length=100)
    state = models.ForeignKey(State, on_delete=models.PROTECT)

    quantity = models.PositiveIntegerField(default=1)
    delivery_date = models.DateField(auto_now=False, auto_now_add=False)
    model = models.ForeignKey(Model, verbose_name="Modelo", on_delete=models.PROTECT)
    file_example = models.FileField(
        verbose_name="Arte de Exemplo", null=True, blank=True)
    observations = models.TextField(
        verbose_name="Observaçoes", null=True, blank=True)

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"

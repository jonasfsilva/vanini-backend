from django.db import models
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from localflavor.br.br_states import STATE_CHOICES
from localflavor.br.models import BRStateField
from core.models import BaseModel


class State(BaseModel):
    ZONE_CHOICES = (
        ("Norte", "Norte"),
        ("Nordeste", "Nordeste"),
        ("Sudeste", "Sudeste"),
        ("Sul", "Sul"),
        ("Centro-Oeste", "Centro-Oeste"),
    )
    uf = BRStateField(
        verbose_name="estado", choices=STATE_CHOICES, null=True, blank=True
    )
    zone_code = models.CharField(
        verbose_name="código IBGE da Zona", max_length=255)
    zone = models.CharField(
        verbose_name="zona", choices=ZONE_CHOICES, max_length=255)
    code = models.CharField(
        verbose_name="código IBGE",
        max_length=255,
        unique=True,
        error_messages={
            "unique": "Já existe um estado cadastrado com esse código"
        },
    )
    name = models.CharField(verbose_name="nome", max_length=255)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.name

    def value_choise(self):
        zone = {
            "Norte": "1",
            "Nordeste": "2",
            "Sudeste": "3",
            "Sul": "4",
            "Centro-Oeste": "5",
        }
        for key, value in zone.items():
            if key == self.zone:
                return value

    def clean(self):
        state = State.objects.filter(
            uf=self.uf, zone=self.zone).exclude(id=self.id)
        self.name = dict(STATE_CHOICES)[self.uf]
        if state:
            raise ValidationError(
                f"O estado {self.name} já se encontra cadastrado"
            )

        self.zone_code = self.value_choise()
        return self

    def delete(self):
        self.slug = self.slug + "-" + str(self.id)
        self.code = self.code + "-" + str(self.id)
        return super().delete()

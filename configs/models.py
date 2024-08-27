from django.db import models
from core.models import BaseModel


class Image(BaseModel):

    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagenwds"


class Site(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    call_to_action_link = models.URLField()
    twitter_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)

    about_image = models.ImageField(upload_to="about/", verbose_name="Sobre (Imagem)")
    about_title = models.CharField(max_length=100, verbose_name="Sobre (Título)")
    about_description = models.TextField(verbose_name="Sobre (Descrição)")

    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações dos Sites"

    def __str__(self) -> str:
        return self.name


class Contact(BaseModel):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    text = models.TextField()

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self) -> str:
        return self.name


class DinamicTool(BaseModel):

    title = models.CharField(max_length=120)
    resume = models.TextField()
    image = models.ImageField()
    link = models.URLField()

    class Meta:
        verbose_name = "Link para ferramenta dinamica"
        verbose_name_plural = "Links para ferramentas dinamicas"

    def __str__(self) -> str:
        return self.title


class MenuItem(BaseModel):

    title = models.CharField(max_length=120)
    link = models.URLField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Item do Menu"
        verbose_name_plural = "Itens do Menu"
        ordering = ["-order"]
        
    def __str__(self) -> str:
        return self.title


class Activity(BaseModel):

    title = models.CharField(max_length=120)
    date_hour = models.DateTimeField(auto_now=False)
    description = models.TextField()
    link = models.URLField()

    class Meta:
        verbose_name = "Agenda de atividade"
        verbose_name_plural = "Agenda de atividades"

    def __str__(self) -> str:
        return self.title


class Galery(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Título da Galeria")
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"

    def __str__(self) -> str:
        return self.title


class ImageGalery(BaseModel):

    galery = models.ForeignKey(Galery, on_delete=models.PROTECT, related_name="images")
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="gallery-images/")

    class Meta:
        verbose_name = "Imagem da Galeria"
        verbose_name_plural = "Imagens das Galerias"


class NewsLetterLead(BaseModel):

    email = models.EmailField()

    class Meta:
        verbose_name = "NewsLetter"
        verbose_name_plural = "NewsLetter"

    def __str__(self) -> str:
        return self.email


class BannerHeader(BaseModel):

    title = models.CharField(max_length=100, default="Banner 1")
    image = models.ImageField(upload_to="banners-headers/")
    image_mobile = models.ImageField(upload_to="banners-headers-mobile/")
    order = models.PositiveIntegerField(default=1)
    link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Banner Principal"
        verbose_name_plural = "Banners Principais"
        
    # def __str__(self) -> str:
    #     return self.title


class BannerMid(BaseModel):

    title = models.CharField(max_length=100, default="Banner 1")
    image = models.ImageField(upload_to="banners-mid/")
    image_mobile = models.ImageField(upload_to="banners-mid-mobile/")
    order = models.PositiveIntegerField(default=1)
    link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Banner Intermediario"
        verbose_name_plural = "Banners Intermediários"

    # def __str__(self) -> str:
    #     return self.title


class GaleryTypeVideo(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Título da Galeria")
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Galeria de Video"
        verbose_name_plural = "Galerias de Videos"

    def __str__(self) -> str:
        return self.title


class VideoGalery(BaseModel):

    galery = models.ForeignKey(GaleryTypeVideo, on_delete=models.PROTECT, related_name="videos")
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    video_link = models.ImageField(upload_to="gallery-videos/")

    class Meta:
        verbose_name = "Video da Galeria"
        verbose_name_plural = "Videos das Galerias"

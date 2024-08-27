from django.db import models

from core.models import BaseModel


class Tag(BaseModel):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    
    def __str__(self) -> str:
        return self.name


class Post(BaseModel):

    title = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name="Slug", null=True, blank=True)
    image = models.ImageField(upload_to="posts/images/")
    cover_image = models.ImageField(upload_to="posts/cover-images/")
    short_description = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=False)
    priority = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

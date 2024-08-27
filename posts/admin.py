from django.contrib import admin
from core.admin import BaseSuperAdmin
from django_summernote.admin import SummernoteModelAdmin
from posts.models import Post
from posts.models import Tag


@admin.register(Tag)
class TagClass(BaseSuperAdmin):
    ...


@admin.register(Post)
class PostClass(BaseSuperAdmin, SummernoteModelAdmin):
    summernote_fields = ('content', 'short_description', )

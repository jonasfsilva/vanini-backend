from django.contrib import admin
from core.admin import BaseSuperAdmin
from configs.models import BannerHeader, BannerMid, Contact, DinamicTool, Galery, GaleryTypeVideo, ImageGalery, MenuItem, VideoGalery
from configs.models import NewsLetterLead
from configs.models import Site
from configs.models import Activity


class ImageGaleryInline(admin.StackedInline):
    model = ImageGalery
    extra = 0
    exclude = (
        "deleted",
        "deleted_at",
    )


@admin.register(Contact)
class ContactClass(BaseSuperAdmin):
    # inlines = [ClientInfoInline, ]
    ...


@admin.register(Site)
class SiteClass(BaseSuperAdmin):
    ...


@admin.register(NewsLetterLead)
class NewsLetterLeadClass(BaseSuperAdmin):
    ...


@admin.register(DinamicTool)
class DinamicToolClass(BaseSuperAdmin):
    ...


@admin.register(MenuItem)
class MenuItemClass(BaseSuperAdmin):
    ...
    

@admin.register(Galery)
class GaleryClass(BaseSuperAdmin):
    inlines = [ImageGaleryInline,]


@admin.register(ImageGalery)
class ImageGaleryClass(BaseSuperAdmin):
    ...


@admin.register(BannerHeader)
class BannerHeaderClass(BaseSuperAdmin):
    list_display = ("title", )


@admin.register(BannerMid)
class BannerMidClass(BaseSuperAdmin):
    list_display = ("title", )


@admin.register(Activity)
class ActivityClass(BaseSuperAdmin):
    ...


@admin.register(GaleryTypeVideo)
class GaleryTypeVideoClass(BaseSuperAdmin):
    ...


@admin.register(VideoGalery)
class VideoGaleryClass(BaseSuperAdmin):
    ...

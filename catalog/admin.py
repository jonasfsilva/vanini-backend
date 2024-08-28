from django.contrib import admin


@admin.register(Tag)
class TagClass(BaseSuperAdmin):
    ...
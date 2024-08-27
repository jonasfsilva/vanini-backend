from django.contrib import admin


class BaseSuperAdmin(admin.ModelAdmin):
    exclude = ("created_at", "updated_at", "deleted_at", "deleted")

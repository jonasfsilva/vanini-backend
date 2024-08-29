from django.contrib import admin

from core.admin import BaseSuperAdmin
from orders.models import QuotationInfo


@admin.register(QuotationInfo)
class QuotationInfoClass(BaseSuperAdmin):
    list_display = ("name", "quantity", "city",)
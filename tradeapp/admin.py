from django.contrib import admin
from .models import TradePost


class TradePostModel(admin.ModelAdmin):
    list_display = ["__str__", "publisher_name", "product_price", "end_date"]

    class Meta:
        Model = TradePost


admin.site.register(TradePost, TradePostModel)

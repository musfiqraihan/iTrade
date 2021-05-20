from django.contrib import admin
from .models import TradePost, BiddingPost


class TradePostModel(admin.ModelAdmin):
    list_display = ["__str__", "publisher_name", "product_price", "end_date"]

    class Meta:
        Model = TradePost


admin.site.register(TradePost, TradePostModel)


class BiddingPostModel(admin.ModelAdmin):
    list_display = ["__str__", "bid_publisher_name", "bid_product_price_bdt", "posted_on"]

    class Meta:
        Model = BiddingPost


admin.site.register(BiddingPost, BiddingPostModel)
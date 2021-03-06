from django.db import models
from django.contrib.auth.models import User


class TradePost(models.Model):
    publisher_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='trade_images')
    product_price = models.FloatField(default=0.0)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.product_name


class BiddingPost(models.Model):
    bid_product_name = models.ForeignKey(TradePost, on_delete=models.CASCADE)
    bid_publisher_name = models.CharField(max_length=200)
    bid_product_price_bdt = models.FloatField(default=0.0)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.bid_product_name.product_name



# Generated by Django 3.2.3 on 2021-05-20 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0005_alter_biddingpost_bid_publisher_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biddingpost',
            old_name='bid_product_price',
            new_name='bid_product_price_bdt',
        ),
    ]
from django import forms
from .models import TradePost, BiddingPost


class CreateTradePost(forms.ModelForm):
    end_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}))

    class Meta:
        model = TradePost
        fields = [
            'product_name',
            'product_description',
            'product_image',
            'product_price',
            'end_date',
        ]


class CreateBiddingPost(forms.ModelForm):

    class Meta:
        model = BiddingPost
        fields = [
            'bid_product_price_bdt',
        ]
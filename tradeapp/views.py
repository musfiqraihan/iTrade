from django.shortcuts import render, get_object_or_404, redirect
from .models import TradePost, BiddingPost
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CreateTradePost, CreateBiddingPost
from django.contrib import messages
from django.http import HttpResponseNotFound
import datetime


def home(request):
    if request.user.is_authenticated:
        post = TradePost.objects.all().order_by('-posted_on')
        search = request.GET.get('index_search')

        if search:
            post = post.filter(
                Q(product_name__icontains=search)
            )

        paginator = Paginator(post, 8)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "post": page_obj,
        }

        return render(request, 'trade/index.html', context)

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def create_post(request):
    if request.user.is_authenticated:
        get_user = get_object_or_404(User, id=request.user.id)
        form = CreateTradePost(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.publisher_name = get_user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Post Created Successfully!")
            return redirect('index')

        return render(request, 'trade/create_post.html', {"form": form})

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def my_posts(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        post = TradePost.objects.filter(publisher_name=user).order_by('-posted_on')

        paginator = Paginator(post, 8)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "post": page_obj,
        }

        return render(request, 'trade/my_post.html', context)


    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')




def single_posts(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(TradePost, pk=id)
        get_user = get_object_or_404(User, id=request.user.id)
        get_bidder_list = BiddingPost.objects.filter(bid_product_name=post).order_by('-posted_on')

        check_lt = TradePost.objects.filter(pk=id, end_date__lt=datetime.date.today())

        if check_lt:
            get_winner = []

            for w in get_bidder_list:
                get_winner.append(w.bid_product_price_bdt)

            winner_price = max(get_winner)

            winner = BiddingPost.objects.get(bid_product_price_bdt=winner_price)
            winner_name = winner.bid_publisher_name

            context = {
                "quote": "Auction Closed. Winner is: ",
                "bid": get_bidder_list,
                "post": post,
                "winner": winner_name,
                "at": " at ",
                "price": winner_price,
            }
            return render(request, 'trade/single_post.html', context)

        else:
            form = CreateBiddingPost(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.bid_product_name = post
                    instance.bid_publisher_name = get_user
                    instance.save()
                    messages.add_message(request, messages.SUCCESS, "Bid Added Successfully!")
                    return redirect('single_post', id=post.id)
            return render(request, 'trade/single_post.html', {"form": form, "post": post, "bid": get_bidder_list})



    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')
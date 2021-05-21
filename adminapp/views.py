from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from tradeapp.models import TradePost, BiddingPost
from django.core.paginator import Paginator
from tradeapp.forms import CreateTradePost, CreateBiddingPost
from django.contrib import messages
from django.http import HttpResponseNotFound, JsonResponse
import datetime


def admin_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = get_object_or_404(User, id=request.user.id)
            post = TradePost.objects.all().order_by('-posted_on')

            paginator = Paginator(post, 8)

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                "post": page_obj,
                "user": user,
            }

            return render(request, 'adminsite/dashboard.html', context)


        else:
            return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                        '<a href="/">LOGIN</a></h1>')

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def admin_single_posts(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
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
                return render(request, 'adminsite/admin_single_post.html', context)

            else:
                form = CreateBiddingPost(request.POST or None)
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit=False)
                        instance.bid_product_name = post
                        instance.bid_publisher_name = get_user
                        instance.save()
                        messages.add_message(request, messages.SUCCESS, "Bid Added Successfully!")
                        return redirect('admin_single_post', id=post.id)
                return render(request, 'adminsite/admin_single_post.html',
                              {"form": form, "post": post, "bid": get_bidder_list})


        else:
            return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                        '<a href="/">LOGIN</a></h1>')

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def auction_static(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            post = TradePost.objects.filter(end_date__gt=datetime.date.today())

            current_post = 0
            for _ in post:
                current_post = current_post + 1

            total_value = 0
            for i in post:
                total_value = total_value + i.product_price

            context = {
                "current": current_post,
                "value": total_value,
            }

            return render(request, 'adminsite/auction_static.html', context)

        else:
            return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                        '<a href="/">LOGIN</a></h1>')

    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')


def get_data(request):
    if request.user.is_authenticated:
        if request.user.is_staff:

            march = TradePost.objects.filter(end_date__gte=datetime.date(2021, 3, 1),
                                             end_date__lte=datetime.date(2021, 3, 31))

            april = TradePost.objects.filter(end_date__gte=datetime.date(2021, 4, 1),
                                             end_date__lte=datetime.date(2021, 4, 30))

            may = TradePost.objects.filter(end_date__gte=datetime.date(2021, 5, 1),
                                           end_date__lte=datetime.date(2021, 5, 31))

            june = TradePost.objects.filter(end_date__gte=datetime.date(2021, 6, 1),
                                            end_date__lte=datetime.date(2021, 6, 30))

            july = TradePost.objects.filter(end_date__gte=datetime.date(2021, 7, 1),
                                            end_date__lte=datetime.date(2021, 7, 31))

            august = TradePost.objects.filter(end_date__gte=datetime.date(2021, 8, 1),
                                              end_date__lte=datetime.date(2021, 8, 30))

            count_march = 0
            for _ in march:
                count_march = count_march + 1

            march_value = 0
            for i in march:
                march_value = march_value + i.product_price

            count_april = 0
            for _ in april:
                count_april = count_april + 1

            april_value = 0
            for i in april:
                april_value = april_value + i.product_price

            count_may = 0
            for _ in may:
                count_may = count_may + 1

            may_value = 0
            for i in may:
                may_value = may_value + i.product_price

            count_june = 0
            for _ in june:
                count_june = count_june + 1

            june_value = 0
            for i in june:
                june_value = june_value + i.product_price

            count_july = 0
            for _ in july:
                count_july = count_july + 1

            july_value = 0
            for i in july:
                july_value = july_value + i.product_price

            count_august = 0
            for _ in august:
                count_august = count_august + 1

            august_value = 0
            for i in august:
                august_value = august_value + i.product_price

            data = {
                "auction_add": [count_march, count_april, count_may, count_june, count_july, count_august],
                "auction_complete": [count_march, 5, 7, 8, 10, 20],
                "auction_value": [march_value, april_value, may_value, june_value, july_value, august_value]
            }
            return JsonResponse(data)

        else:
            return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                        '<a href="/">LOGIN</a></h1>')
    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')

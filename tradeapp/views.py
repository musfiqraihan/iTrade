from django.shortcuts import render, get_object_or_404, redirect
from .models import TradePost
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CreateTradePost
from django.contrib import messages
from django.http import HttpResponseNotFound


def home(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)

        post = TradePost.objects.all().order_by('-posted_on')
        search = request.GET.get('index_search')

        if search:
            post = post.filter(
                Q(product_name__icontains=search) | Q(product_description_icontains=search)
            )

        paginator = Paginator(post, 8)  # Show 25 contacts per page.

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

        paginator = Paginator(post, 8)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "post": page_obj,
        }

        return render(request, 'trade/my_post.html', context)


    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">You are not eligible to see this page <br> DO '
                                    '<a href="/">LOGIN</a></h1>')




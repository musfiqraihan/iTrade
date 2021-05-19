from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUser
from django.contrib.auth.models import User


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            get_name = request.POST['user']
            password = request.POST['password']

            if '@' in get_name:
                try:
                    username = User.objects.get(email=get_name.lower()).username
                except User.DoesNotExist:
                    messages.add_message(request, messages.ERROR, "Email Doesn't exist!")
                    return redirect('login')
            else:
                username = get_name

            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')

            except User.DoesNotExist:
                return None

            else:
                messages.add_message(request, messages.ERROR, 'Username Or Password Mismatch!')

    return render(request, 'user/login.html')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = RegisterUser(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Registration Successfully Completed!")
            return redirect('index')

    return render(request, 'user/register.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')

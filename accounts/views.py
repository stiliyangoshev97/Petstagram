from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from accounts.forms import LoginForm, RegisterForm


def index(request):
    return render(request, 'index.html')

def return_user(request):
    return request.user


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = RegisterForm()


    success_message = "You have successfully signed-up!"

    context = {
        "form": form,
        "success_message": success_message,
        "form_isValid": form.is_valid(),
    }

    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect("index")

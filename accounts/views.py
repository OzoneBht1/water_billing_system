from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return reverse_lazy("users:home")
        # restrict autheticated user to access login and register
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                fn = form.cleaned_data.get("first_name")
                ln = form.cleaned_data.get("last_name")
                messages.success(
                    request, "Account was successfully created for " + fn + " " + ln
                )
                return redirect("accounts:userLogin")

        return render(request, "accounts/register.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        return reverse_lazy("users:home")
    else:
        if request.method == "POST":
            phone_number = request.POST.get("phone_number")
            password = request.POST.get("password")

            user = authenticate(request, username=phone_number, password=password)

            if user is not None:
                login(request, user)

                return redirect("users:home")
            else:
                messages.info(request, "Invalid Login")

        return render(request, "accounts/login.html", {})


def logoutUser(request):
    logout(request)
    return redirect("accounts:userLogin")


@login_required(login_url="accounts:userLogin")
def home(request):
    return render(request, reverse_lazy("users:home"), {})

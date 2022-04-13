from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# This is the view for the user to sign up and login. It checks if the forms are valid and then creates a new user or logs them in
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("users:home"))
        # restrict autheticated user to access login and register
    else:
        form = CreateUserForm()
        # creates empty form if no data is submitted i.e. GET request
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # saves the form to the database of the user if the form is valid
                fn = form.cleaned_data.get("first_name")
                ln = form.cleaned_data.get("last_name")
                messages.success(
                    request, "Account was successfully created for " + fn + " " + ln
                )
                return redirect("accounts:userLogin")

        return render(request, "accounts/register.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("users:home"))
    # restrict autheticated user to access login and register
    else:
        if request.method == "POST":
            phone_number = request.POST.get("phone_number")
            password = request.POST.get("password")
            #
            user = authenticate(request, username=phone_number, password=password)
            #  searches for the user in the database
            if user is not None:
                login(request, user)
                # logs the user in if the user is found
                return redirect(reverse_lazy("users:home"))
            else:
                messages.info(request, "Invalid Login")

        return render(request, "accounts/login.html", {})


def logoutUser(request):
    logout(request)
    # logouts the use. It uses the logout function from Django
    return redirect("accounts:userLogin")


@login_required(login_url="accounts:userLogin")
def home(request):
    return render(request, "user_view/homepage.html", {})

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import json
from .forms import PaymentForm, NewTapForm, PaymentForm2
from django.contrib import messages


def home(request):
    return render(request, "user_view/homepage.html", {})


def payment(request):

    with open("data.json") as f:
        data = json.load(f)
        # Loading the data from Json file containing details of provinces, districts and local bodies of Nepal

    if request.method == "POST":
        form = PaymentForm2(request.POST)
        print(form)

        login_data = request.POST.dict()
        print(login_data)
        # username = login_data.get("province")
        # password = login_data.get("municipality")
        # user_type = login_data.get("district")
        # print(user_type, username, password)
        if form.is_valid():
            # obj = form.save()
            # obj.province = login_data.get("province")
            # obj.save()
            form.save()
            messages.success(request, "Data saved successfully")
            return redirect("accounts:userLogin")
        else:
            messages.info(request, "Invalid Login")

    form = PaymentForm()

    # Passing the form from forms.py to the template, and also the data from the json file
    return render(request, "user_view/payment.html", {"data": data, "form": form})


def about(request):
    return render(request, "user_view/about.html", {})


def newtap(request):
    if request.method == "POST":
        form = NewTapForm(request.POST)
        print(form)

        login_data = request.POST.dict()
        print(login_data)
        # username = login_data.get("province")
        # password = login_data.get("municipality")
        # user_type = login_data.get("district")
        # print(user_type, username, password)
        if form.is_valid():
            # obj = form.save()
            # obj.province = login_data.get("province")
            # obj.save()
            form.save()
            messages.success(request, "Data saved successfully")
            return redirect("accounts:userLogin")

    form = NewTapForm()
    return render(request, "user_view/newtap.html", {"form": form})

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import json
from .forms import PaymentForm
from django.contrib import messages


def home(request):
    return render(request, "user_view/homepage.html", {})


def payment(request):

    with open("data.json") as f:
        data = json.load(f)

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully")
            return redirect("accounts:userLogin")

        return render(request, "user_view/payment.html", {})

    form = PaymentForm()
    return render(request, "user_view/payment.html", {"data": data, "form": form})


def about(request):
    return render(request, "user_view/about.html", {})

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy


def home(request):
    return render(request, "user_view/homepage.html", {})


def payment(request):
    return render(request, "user_view/payment.html", {})


def about(request):
    return render(request, "user_view/about.html", {})

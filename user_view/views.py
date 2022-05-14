from datetime import datetime
import re
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse_lazy
import json
from .forms import (
    PaymentForm,
    NewTapForm,
    PaymentForm2,
    BlankInpForm,
    MeterReplacementForm,
)
from django.contrib import messages
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .process import html_to_pdf
from django.views.generic import View
from .models import Payment
from django.views.generic import ListView, DetailView
from admin_view.models import Post
from django.contrib import messages


def payment(request):

    with open("data.json") as f:
        data = json.load(f)
        # Loading the data from Json file containing details of provinces, districts and local bodies of Nepal

    if request.method == "POST":
        form = PaymentForm2(request.POST)

        login_data = request.POST.dict()

        if form.is_valid():
            timestamp = datetime.now()
            dt_string = timestamp.strftime("%d/%m/%Y %H:%M:%S")
            phone_num = request.user.username
            email = request.user.email

            obj = form.save()
            obj.timestamp = dt_string
            obj.phone_num = phone_num
            obj.email = email
            # Adding the current time, phone number and email to the database
            obj.save()

            return redirect("user_view:gateway", pk=obj.customer_id)
        # sending the payment data to the gateway page

    form = PaymentForm(
        {
            "customer_id": request.user.profile.customer_id,
            "customer_name": request.user.first_name + " " + request.user.last_name,
        }
    )
    # rendering an empty form with default values of the name and ID from user's profile

    # Passing the form from forms.py to the template, and also the data from the json file
    return render(request, "user_view/payment.html", {"data": data, "form": form})


def about(request):
    return render(request, "user_view/about.html", {})


def newtap(request):
    if request.method == "POST":
        print(request.POST)
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

        form = NewTapForm()
        return render(request, "user_view/newtap.html", {"form": form})


def result(request, context):
    # This is the receipt that will be displayed after the payment is successful

    obj = Payment.objects.get(customer_id=context)
    # Details of the Payee obtained from by choosing the ID from the parameter
    print(obj.timestamp)
    print(obj.phone_num)
    print(obj.discount_amount)
    print(obj)
    messages.success(request, "Payment Successful! Thank you.")
    # return html_to_pdf(
    #     "user_view/result.html", {"pagesize": "auto", "context": context}
    # )
    return render(request, "user_view/result.html", {"context": obj})


def gateway(request, pk):
    if request.method == "POST":
        print("test", request.POST)
        obj = request.POST.get("pk", None)
        # the gateway portal, which isnt functional. We only click the submit button here
        if obj:
            print(obj)
            return result(request, obj)

    return render(request, "user_view/gateway.html", {"pk": pk})


class PostList(ListView):

    # queryset = Post.objects.filter(status=1).order_by("-created_on")
    model = Post
    template_name = "user_view/homepage.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["posts"] = Post.objects.filter(status=1).order_by("-created_on")
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = "user_view/post_detail.html"


def meterReplacement(request):
    with open("data.json") as f:
        data = json.load(f)
    form = MeterReplacementForm(
        {
            "customer_id": request.user.profile.customer_id,
            "contact": request.user.username,
        }
    )
    if request.method == "POST":
        print("hello")
        form = MeterReplacementForm(request.POST)
        if form.is_valid():
            print("hi")
            form.save()
            messages.success(request, "Your request has been submitted successfully")
            return redirect("user_view:meter_replacement")
    return render(
        request, "user_view/meterReplacement.html", {"data": data, "form": form}
    )

from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from user_view.models import MeterReplacement, Payment
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)
from .models import Post
from django.contrib import messages
from django.urls import reverse_lazy
import json
from django import template
from accounts.models import Profile
import csv

# Create your views here.


# def addPost(request):
#     if request.method == "post":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Post created Successfully")

#     form = PostForm()
#     return render(request, "admin_view/addPost.html", {"form": form})


class AddPostView(CreateView):
    model = Post
    template_name = "admin_view/add_post.html"
    fields = ["title", "content", "status", "author"]


class PostList(ListView):

    # queryset = Post.objects.filter(status=1).order_by("-created_on")
    model = Post
    template_name = "admin_view/all_post_list.html"


class PostDetail(DetailView):
    model = Post
    template_name = "admin_view/post_detail.html"


class PostUpdate(UpdateView):
    model = Post
    template_name = "admin_view/post_update.html"
    fields = ["title", "content", "status"]


class PostDelete(DeleteView):
    model = Post
    template_name = "admin_view/post_delete.html"
    success_url = reverse_lazy("admin_view:allposts")


class UserList(ListView):
    model = Profile
    template_name = "admin_view/user_list.html"


class UserDetail(DetailView):
    model = Profile
    template_name = "admin_view/user_detail.html"


class UserDelete(DeleteView):
    model = Profile
    template_name = "admin_view/user_delete.html"
    success_url = reverse_lazy("admin_view:user_list")


class PaymentList(ListView):
    model = Payment
    template_name = "admin_view/payment_list.html"


class PaymentDelete(DeleteView):
    model = Payment
    template_name = "admin_view/payment_delete.html"
    success_url = reverse_lazy("admin_view:payment_details")


class MeterReplacementList(ListView):
    model = MeterReplacement
    template_name = "admin_view/meter_list.html"


class MeterReplacementDelete(DeleteView):
    model = MeterReplacement
    template_name = "admin_view/meter_delete.html"
    success_url = reverse_lazy("admin_view:meter_replacement_list")


def officeDetail(request):

    with open("data.json") as f:
        data = json.load(f)

        return render(request, "admin_view/office_view.html", {"data": data})


def user_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attactment; filename: users.csv"

    # create a csv writer
    writer = csv.writer(response)

    # configure model

    profiles = Profile.objects.all()

    writer.writerow(
        ["Full Name ", "Phone Number", "Email", "House No", "Customer ID", "Address"]
    )

    for profile in profiles:
        writer.writerow(
            [
                profile.user.first_name + " " + profile.user.last_name,
                profile.user.username,
                profile.user.email,
                profile.house_no,
                profile.customer_id,
                profile.address,
            ]
        )

    return response

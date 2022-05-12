from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
from accounts.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

# Create your views here.


# def addPost(request):
#     if request.method == "post":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Post created Successfully")

#     form = PostForm()
#     return render(request, "admin_view/addPost.html", {"form": form})


@method_decorator(permission_required("is_superuser"), name="dispatch")
class AddPostView(CreateView):
    model = Post
    template_name = "admin_view/add_post.html"
    fields = ["title", "content", "status", "author"]


@method_decorator(permission_required("is_superuser"), name="dispatch")
class PostList(ListView):

    # queryset = Post.objects.filter(status=1).order_by("-created_on")
    model = Post
    template_name = "admin_view/all_post_list.html"


@method_decorator(permission_required("is_superuser"), name="dispatch")
class PostDetail(DetailView):
    model = Post
    template_name = "admin_view/post_detail.html"


@method_decorator(permission_required("is_superuser"), name="dispatch")
class PostUpdate(UpdateView):
    model = Post
    template_name = "admin_view/post_update.html"
    fields = ["title", "content", "status"]


@method_decorator(permission_required("is_superuser"), name="dispatch")
class PostDelete(DeleteView):
    model = Post
    template_name = "admin_view/post_delete.html"
    success_url = reverse_lazy("admin_view:allposts")


@method_decorator(permission_required("is_superuser"), name="dispatch")
class UserList(ListView):
    model = Profile
    template_name = "admin_view/user_list.html"


@method_decorator(permission_required("is_superuser"), name="dispatch")
class UserDelete(DeleteView):
    model = Profile
    template_name = "admin_view/user_delete.html"
    success_url = reverse_lazy("admin_view:user_list")


# class UserUpdate(UpdateView):
#     model = Profile
#     template_name = "admin_view/user_update.html"
#     fields = "__all__"


@method_decorator(permission_required("is_superuser"), name="dispatch")
def UserUpdate(request, pk):

    currentProfile = Profile.objects.get(id=pk)
    currentUser = User.objects.get(profile=currentProfile)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=currentUser)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=currentProfile)
        if p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("admin_view:user_list")
    else:
        u_form = UserUpdateForm(instance=currentUser)
        p_form = ProfileUpdateForm(instance=currentProfile)

    return render(
        request,
        "admin_view/user_update.html",
        {
            "u_form": u_form,
            "p_form": p_form,
        },
    )

    #  if request.method == "POST":
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(
    #         request.POST, request.FILES, instance=request.user.profile
    #     )
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, "Your account has been updated!")
    #         return redirect("accounts:profile")  # Redirect back to profile page

    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)

    # return render(
    #     request, "accounts/profile.html", {"u_form": u_form, "p_form": p_form}
    # )


@method_decorator(permission_required("is_superuser"), name="dispatch")
class PaymentList(ListView):
    model = Payment
    template_name = "admin_view/payment_list.html"


@method_decorator(permission_required("is_superuser"), name="dispatch")
class PaymentDelete(DeleteView):
    model = Payment
    template_name = "admin_view/payment_delete.html"
    success_url = reverse_lazy("admin_view:payment_details")


@method_decorator(permission_required("is_superuser"), name="dispatch")
class MeterReplacementList(ListView):
    model = MeterReplacement
    template_name = "admin_view/meter_list.html"


@method_decorator(permission_required("is_superuser"), name="dispatch")
class MeterReplacementDelete(DeleteView):
    model = MeterReplacement
    template_name = "admin_view/meter_delete.html"
    success_url = reverse_lazy("admin_view:meter_replacement_list")


@method_decorator(permission_required("is_superuser"), name="dispatch")
def officeDetail(request):

    with open("data.json") as f:
        data = json.load(f)

        return render(request, "admin_view/office_view.html", {"data": data})


@method_decorator(permission_required("is_superuser"), name="dispatch")
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

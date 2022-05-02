from django.shortcuts import render
from django.contrib.auth.models import User
from user_view.models import Payment
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

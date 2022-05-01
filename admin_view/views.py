from django.shortcuts import render
from django.contrib.auth.models import User
from user_view.models import Payment
from django.views import generic
from .models import Post

# Create your views here.


def dashboard(request):
    payment_count = Payment.objects.all().count()
    # user_count = User.object.filter(superuser=True).count()

    return render(request, "admin_view/dashboard.html", {})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "admin_view/dashboard.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "admin_view/post_detail.html"

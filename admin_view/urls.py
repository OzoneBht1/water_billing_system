from django.urls import path
from . import views
from admin_view.views import AddPostView

app_name = "admin_view"

# These are the URLS for the accounts app. They are used to direct the user to the correct page.


urlpatterns = [
    path("add_post/", AddPostView.as_view(), name="addpost"),
]

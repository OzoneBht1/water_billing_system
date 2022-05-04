from django.urls import path
from . import views
from admin_view.views import AddPostView

app_name = "admin_view"

# These are the URLS for the accounts app. They are used to direct the user to the correct page.


urlpatterns = [
    path("add_post/", AddPostView.as_view(), name="addpost"),
    path("all_posts", views.PostList.as_view(), name="allposts"),
    path("all_posts/<slug:slug>/", views.PostDetail.as_view(), name="post_detailview"),
    path(
        "all_posts/<slug:slug>/edit", views.PostUpdate.as_view(), name="post_updateview"
    ),
    path(
        "all_posts/<slug:slug>/delete",
        views.PostDelete.as_view(),
        name="post_deleteview",
    ),
]
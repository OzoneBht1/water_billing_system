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
    path("users", views.UserList.as_view(), name="user_list"),
    path("office_details", views.officeDetail, name="office_details"),
    path("payment_details", views.PaymentList.as_view(), name="payment_details"),
    path("users/<int:pk>", views.UserDelete.as_view(), name="user_delete"),
    # path("users/update/<int:pk>", views.UserUpdate.as_view(), name="user_update"),
    path("users/update/<int:pk>", views.UserUpdate, name="user_update"),
    path(
        "payment_details/<int:pk>", views.PaymentDelete.as_view(), name="payment_delete"
    ),
    path(
        "meter_replacement_list",
        views.MeterReplacementList.as_view(),
        name="meter_replacement_list",
    ),
    path(
        "meter_replacement_list/<int:pk>",
        views.MeterReplacementDelete.as_view(),
        name="meter_replacement_delete",
    ),
    path("user_csv", views.user_csv, name="user_csv"),
]

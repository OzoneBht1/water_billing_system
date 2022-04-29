from django.urls import path

from . import views


app_name = "user_view"
# These are the URLS for the user_view app. They are used to direct the user to the correct page.
urlpatterns = [
    path("", views.home, name="home"),
    path("payment/", views.payment, name="payment"),
    path("about/", views.about, name="about"),
    path("newtap/", views.newtap, name="newtap"),
    # path("generate/", views.generate, name="generate"),
    path("gateway/", views.gateway, name="gateway"),
    path("result", views.result, name="result"),
]

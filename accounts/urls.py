"""water_billing_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "accounts"

# These are the URLS for the accounts app. They are used to direct the user to the correct page.
urlpatterns = [
    path("register/", views.register, name="userRegistration"),
    path("login/", views.loginPage, name="userLogin"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/", views.profile, name="profile"),
]

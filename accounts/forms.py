from xml.dom import ValidationErr
from xml.etree.ElementInclude import include
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy
from django.contrib.auth import password_validation


# This is form created for the user to sign up. It uses the UserCreationForm from Django.
class CreateUserForm(UserCreationForm):

   
    first_name = forms.CharField(
        max_length=12,
        min_length=4,
        required=True,
        help_text="Required: First Name",
        widget=forms.TextInput(
            attrs={
                "class": "user-input",
                "placeholder": "First Name",
                "name": "first_name",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=12,
        min_length=4,
        required=True,
        help_text="Required: Last Name",
        widget=(
            forms.TextInput(
                attrs={
                    "class": "user-input",
                    "placeholder": "Last Name",
                    "name": "last_name",
                }
            )
        ),
    )
    email = forms.EmailField(
        widget=(
            forms.TextInput(
                attrs={
                    "class": "user-input",
                    "placeholder": "Email",
                    "name": "email",
                    "pattern": "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
                    "title": "Email must contain @ and . ",
                }
            )
        ),
    )
    password1 = forms.CharField(
        label=("Password"),
        widget=(
            forms.PasswordInput(
                attrs={
                    "class": "user-input",
                    "placeholder": "Password",
                    "name": "password1",
                }
            )
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password Confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "class": "user-input",
                "placeholder": "Retype Password",
            }
        ),
        help_text=("Just Enter the same password, for confirmation"),
    )
    username = forms.CharField(
        required=True,
        label="Phone Number",
        widget=forms.TextInput(
            attrs={
                "class": "user-input",
                "autocomplete": "off",
                "pattern": "[0-9]+",
                "title": "Enter numbers Only ",
                "placeholder": "Phone Number",
            }
        ),
    )
    # phone_number = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "autocomplete": "off",
    #             "pattern": "[0-9]+",
    #             "title": "Enter numbers Only ",
    #         }
    #     ),
    # )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

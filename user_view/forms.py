from cProfile import label
from user_view.models import Payment, NewTap
from django.forms import ModelForm, Textarea
from django.forms import ModelForm
from django import forms

# Providing labels, classes and error handling for the bill payment form
class PaymentForm(ModelForm):
    CHOICES = [("Green", "Green"), ("Red", "Red")]

    meter_status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    labels = {
        "reading_date": "Reading Date",
        "reading_month": "Reading Month",
        "customer_id": "Customer ID",
        "customer_name": "Customer Name",
        "previous_unit": "Previous Unit",
        "current_unit": "Current Unit",
        "saving_unit": "Saving Unit",
        "meter_status": "Meter Status",
        "bill_amount": "Bill Amount",
        "penalty": "Penalty",
        "total_unit": "Total Unit",
    }

    widgets = {
        "customer_id": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]{10}",
                "title": "Enter numbers Only ",
                "id": "customer_id",
            }
        ),
        "customer_name": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[a-zA-Z]{,}",
                "title": "Enter your name(string only)",
                "id": "customer_name",
            }
        ),
        "previous_unit": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]+",
                "title": "Enter numbers Only ",
                "id": "previous_unit",
            }
        ),
        "current_unit": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]{,}",
                "id": "current_unit",
            }
        ),
        "saving_unit": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]{,}",
                "id": "saving_unit",
            }
        ),
        "meter_status": Textarea(
            attrs={"cols": 40, "rows": 1, "class": "form-control input"}
        ),
        "bill_amount": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]{,}",
                "id": "bill_amount",
            }
        ),
        "penalty": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]{,}",
                "id": "penalty",
            }
        ),
        "total_unit": Textarea(
            attrs={
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]{,}",
                "id": "total_unit",
            }
        )
        # ),
        # "province": Textarea(
        #     attrs={
        #         "cols": 40,
        #         "rows": 1,
        #         "class": "form-control input",
        #         "pattern": "[0-9]{,}",
        #         "id": "province",
        #     }
        # ),
        # "district": Textarea(
        #     attrs={
        #         "cols": 40,
        #         "rows": 1,
        #         "class": "form-control input",
        #         "pattern": "[0-9]{,}",
        #         "id": "district",
        #     }
        # ),
        # "municipality": Textarea(
        #     attrs={
        #         "cols": 40,
        #         "rows": 1,
        #         "class": "form-control input",
        #         "pattern": "[0-9]{,}",
        #         "id": "municipality",
        #     }
        # ),
    }

    class Meta:
        model = Payment

        fields = (
            "reading_month",
            "reading_date",
            "customer_id",
            "customer_name",
            "previous_unit",
            "current_unit",
            "saving_unit",
            "meter_status",
            "bill_amount",
            "penalty",
            "total_unit",
        )


class PaymentForm2(ModelForm):
    class Meta:
        model = Payment

        fields = (
            "reading_month",
            "reading_date",
            "province",
            "district",
            "municipality",
            "customer_id",
            "customer_name",
            "previous_unit",
            "current_unit",
            "saving_unit",
            "meter_status",
            "bill_amount",
            "penalty",
            "total_unit",
        )


class NewTapForm(ModelForm):
    class Meta:
        model = NewTap

        fields = (
            "province",
            "district",
            "municipality",
            "first_name",
            "last_name",
            "house_no",
            "contact_no",
            "email",
            "citizenship",
        )

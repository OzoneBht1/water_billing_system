from cProfile import label

from typing import Text
from user_view.models import Payment, NewTap
from django.forms import ModelForm, NumberInput, Textarea
from django.forms import ModelForm
from django import forms

# Providing labels, classes and error handling for the bill payment form
class PaymentForm(ModelForm):

    reading_month = forms.CharField(
        label="Reading Month",
        widget=forms.Select(
            attrs={"class": "combo-box", "id": "month"},
            choices=Payment.MONTH_CHOICES,
        ),
    )

    customer_id = forms.IntegerField(
        label="Customer ID",
        widget=NumberInput(
            attrs={
                "min": 000000,
                "max": 999999,
                "title": "The 6 digit Customer ID provided.",
            }
        ),
    )
    previous_unit = forms.IntegerField(
        label="Previous Unit",
        widget=NumberInput(
            attrs={
                "min": 1,
                "max": 999999,
                "title": "The previous meter reading ",
                "id": "previous_unit",
            }
        ),
    )
    current_unit = forms.IntegerField(
        label="Current Unit",
        widget=NumberInput(
            attrs={
                "type": "number",
                "max": 999999,
                "min": 0,
                "pattern": "[0-9]{,}",
                "id": "current_unit",
            }
        ),
    )
    saving_unit = forms.IntegerField(
        label="Consumed Unit",
        widget=NumberInput(
            attrs={
                "type": "number",
                "max": 999999,
                "min": 0,
                "pattern": "[0-9]{,}",
                "id": "consumed_unit",
                "readonly": True,
            }
        ),
    )
    bill_amount = forms.FloatField(
        label="Bill Amount",
        widget=NumberInput(
            attrs={
                "min": 0,
                "max": 99999,
                "title": "The bill amount to be paid",
                "readonly": True,
                "id": "bill_amount",
            }
        ),
    )
    discount_amount = forms.FloatField(
        label="Discount(%)",
        widget=NumberInput(
            attrs={
                "min": 0,
                "max": 99999,
                "id": "discount",
                "readonly": True,
            }
        ),
    )
    penalty = forms.FloatField(
        label="Penalty",
        widget=NumberInput(
            attrs={
                "min": 0,
                "max": 99999,
                "id": "penalty",
                "readonly": True,
            }
        ),
    )
    total_amount = forms.FloatField(
        label="Total Amount",
        widget=NumberInput(attrs={"min": 0, "readonly": True, "id": "final_bill"}),
    )

    customer_name = forms.CharField(
        label="Customer Name",
    )

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        sorted_choices = sorted(Payment.MONTH_CHOICES, key=lambda x: x[1])
        print(sorted_choices)
        self.fields["reading_month"].choices = sorted_choices

    class Meta:
        model = Payment

        fields = (
            "reading_month",
            "customer_id",
            "customer_name",
            "previous_unit",
            "current_unit",
            "saving_unit",
            "bill_amount",
            "penalty",
            "total_amount",
        )


class PaymentForm2(ModelForm):
    class Meta:
        model = Payment

        fields = (
            "reading_month",
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
            "total_amount",
        )

        def clean(self):
            data = self.cleaned_data


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

from cProfile import label
from user_view.models import Payment, NewTap
from django.forms import ModelForm, NumberInput, Textarea
from django.forms import ModelForm
from django import forms

# Providing labels, classes and error handling for the bill payment form
class PaymentForm(ModelForm):
    CHOICES = [("Green", "Green"), ("Red", "Red")]
    # For meter status

    customer_id = forms.IntegerField(
        label="Customer ID",
        widget=NumberInput(
            attrs={
                "class": "form-control",
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
                "class": "form-control",
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
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
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
                "cols": 40,
                "rows": 1,
                "class": "form-control input",
                "pattern": "[0-9]{,}",
                "id": "consumed_unit",
                "readonly": True,
            }
        ),
    )
    bill_amount = forms.IntegerField(
        label="Bill Amount",
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "min": 0,
                "max": 99999,
                "title": "The bill amount to be paid",
                "readonly": True,
            }
        ),
    )
    penalty = forms.IntegerField(
        label="Penalty",
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "min": 0,
                "max": 99999,
                "id": "penalty",
                "readonly": True,
            }
        ),
    )
    total_unit = forms.IntegerField(
        label="Total Amount",
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "min": 0,
                "readonly": True,
            }
        ),
    )
    reading_date = forms.IntegerField(
        label="Reading Date",
        widget=NumberInput(
            attrs={"class": "form-control", "min": 1, "max": 31, "id": "date"}
        ),
    )
    reading_month = forms.IntegerField(
        label="Reading Month",
        widget=NumberInput(
            attrs={"class": "form-control", "min": 1, "max": 12, "id": "month"}
        ),
    )
    customer_name = forms.CharField(
        label="Customer Name",
        widget=Textarea(
            attrs={
                "class": "form-control",
                "rows": 1,
                "cols": 40,
                "pattern": "[a-zA-Z]{,}",
            }
        ),
    )

    meter_status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

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

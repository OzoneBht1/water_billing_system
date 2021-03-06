from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# These are the database models for the bill payment part. The models are created using the ORM.
class Payment(models.Model):
    MONTH_CHOICES = {
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"),
        ("May", "May"),
        ("June", "June"),
        ("July", "July"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November", "November"),
        ("December", "December"),
    }

    timestamp = models.CharField(max_length=100, blank=True, null=True)
    phone_num = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    reading_month = models.CharField(max_length=10, choices=MONTH_CHOICES)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    previous_unit = models.IntegerField()
    current_unit = models.IntegerField()
    consumed_unit = models.IntegerField()
    meter_status = models.CharField(
        max_length=100, default="Green", blank=True, null=True
    )
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    penalty = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # kun mahina samma ko bill ako
    # previous unit bhaneko pahila mahina kati uthyo
    # current unit bhaneko ahile kati uthyo
    # saving unit bhaneko chai kati uthyo
    def __str__(self) -> str:
        return f"{self.customer_name}"


class NewTap(models.Model):
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    citizenship = models.ImageField()


class BlankInp(models.Model):
    blankField = models.CharField(max_length=5, blank=True, null=True)


class MeterReplacement(models.Model):
    office_code = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    contact = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self) -> int:
        return str(self.customer_id)

from django.db import models


# These are the database models for the bill payment part. The models are created using the ORM.
class Payment(models.Model):
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=30, primary_key=True)
    customer_name = models.CharField(max_length=100)
    previous_unit = models.CharField(max_length=30)
    current_unit = models.CharField(max_length=30)
    saving_unit = models.CharField(max_length=30)
    meter_status = models.BooleanField(default=True)
    bill_amount = models.CharField(max_length=30)
    penalty = models.CharField(max_length=30)
    total_unit = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.customer_id}: {self.customer_name}"


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

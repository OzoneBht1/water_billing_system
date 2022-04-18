from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# These are the database models for the bill payment part. The models are created using the ORM.
class Payment(models.Model):
    reading_month = models.IntegerField()
    reading_date = models.IntegerField()
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    previous_unit = models.IntegerField()
    current_unit = models.IntegerField()
    saving_unit = models.IntegerField()
    meter_status = models.CharField(max_length=100, default="green")
    bill_amount = models.IntegerField()
    penalty = models.IntegerField()
    total_unit = models.IntegerField()
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

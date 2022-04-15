from django.contrib import admin

# Register your models here.

from user_view.models import NewTap, Payment


admin.site.register(Payment)
admin.site.register(NewTap)

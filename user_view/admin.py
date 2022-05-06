from django.contrib import admin

# Register your models here.

from user_view.models import NewTap, Payment, MeterReplacement


admin.site.register(Payment)
admin.site.register(NewTap)
admin.site.register(MeterReplacement)

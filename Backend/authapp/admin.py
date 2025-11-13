from django.contrib import admin
from .models import AdminRegistration, PaymentTransaction


@admin.register(AdminRegistration)
class AdminRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email', 'phone', 'password', 'created_at')



@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance')
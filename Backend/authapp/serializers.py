from rest_framework import serializers
from .models import MLModel
from .models import User
from django.db import models

class YourMLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = ['id', 'file', 'name']  # example fields




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password']


class PaymentTransaction(models.Model):
    number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    provider_id = models.CharField(max_length=50)
    client_id = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    message = models.TextField()
    operator_ref = models.CharField(max_length=100, blank=True, null=True)
    payid = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number} - {self.status}"


class TransactionStatus(models.Model):
    client_id = models.CharField(max_length=50)
    provider = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    txnid = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_id} - {self.status}"

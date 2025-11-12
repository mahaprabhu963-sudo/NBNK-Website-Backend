from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    


class User(models.Model):
    phone_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.phone_number

    
class MLModel(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name


class TransactionStatus(models.Model):
    client_id = models.CharField(max_length=50)
    provider = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    txnid = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)  # store full API response
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_id} - {self.status}"
    
class PaymentTransaction(models.Model):
    client_id = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_id} - {self.transaction_id}"
    
class BalanceHistory(models.Model):
    balance = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.balance} @ {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class PaymentTransaction(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)

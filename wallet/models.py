from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=24, unique=True)


class Wallet(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    transaction_card = models.ForeignKey('Transaction_card', on_delete=models.CASCADE, related_name='Transaction_card')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Transaction_card(models.Model):
    card_number = models.IntegerField(blank=False, null=False)
    cvv = models.IntegerField(blank=False, null=False)
    Expiry_date = models.DateTimeField(blank=False, null=False)
    balance = models.DecimalField(decimal_places=2, max_digits=50, max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.card_number} {self.cvv} {self.Expiry_date}'


class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
        ('T', 'Transfer')
    ]
    transaction_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=TRANSACTION_CHOICES,)
    amount = models.DecimalField(max_digits=10, decimal_places=2,)

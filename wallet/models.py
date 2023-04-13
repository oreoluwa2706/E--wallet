from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=24, unique=True)


class Account(models.Model):
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=9, decimal_places=2)


class Beneficiary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Wallet(models.Model):
    # unique_id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    transaction_card = models.ForeignKey('Transaction_card', on_delete=models.CASCADE, related_name='Transaction_card')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    transaction = models.ForeignKey('Transaction_card', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.transaction_card} {self.account}'


class Transaction_card(models.Model):
    card_number = models.CharField(max_length=16, blank=False, null=False)
    card_name = models.CharField(max_length=255, blank=False, null=False)
    cvv = models.CharField(max_length=3, blank=False, null=False)
    Expiry_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return f'{self.card_number} {self.cvv} {self.Expiry_date}'


class Transaction(models.Model):
    # objects = None
    TRANSACTION_CHOICES = [
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
        ('T', 'Transfer')
    ]
    transaction_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=TRANSACTION_CHOICES, )
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class WalletUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=24, unique=True)


class UserAccount(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.OneToOneField(
        to='WalletUser',
        on_delete=models.CASCADE,
        related_name='account'
    )
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def transfer(self, to_account, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        to_account.balance += amount
        self.save()
        to_account.save()

    def get_transaction_history(self):
        return 'Transaction'.objects.filter(account=self).order_by('transaction_time')


class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
        ('T', 'Transfer')
    ]
    account = models.ForeignKey(
        to='UserAccount',
        on_delete=models.CASCADE,
        related_name='transactions'

    )
    transaction_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=1,
        choices=TRANSACTION_CHOICES,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    @classmethod
    def create_deposit(cls, account, amount):
        transaction = cls(
            account=account,
            type='D',
            amount=amount
        )
        account.deposit(amount)
        transaction.save()
        return transaction

    @classmethod
    def create_withdrawal(cls, account, amount):
        transaction = cls(
            account=account,
            type='W',
            amount=amount
        )
        account.withdraw(amount)
        transaction.save()
        return transaction

    @classmethod
    def create_transfer(cls, from_account, to_account, amount):
        transaction = cls(
            account=from_account,
            type='T',
            amount=amount
        )
        from_account.transfer(to_account, amount)
        transaction.save()
        return transaction

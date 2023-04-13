from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserCreatePasswordRetypeSerializer, \
    UserCreateSerializer

from wallet.models import Wallet, Transaction, Transaction_card, Account, Beneficiary, User


class WalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        field = ['user', 'transaction_card', 'account']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        field = ['bank_name', 'account_number']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('account', 'transaction_time', 'amount')


"""
class UserCreate(UserCreatePasswordRetypeSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'password']


class UserCreates(UserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', ]
"""


class Transaction_cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_card
        fields = ('card_number', 'cvv', 'Expiry date')


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = 'account'

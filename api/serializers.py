from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserCreatePasswordRetypeSerializer, \
    UserCreateSerializer

from wallet.models import Wallet, Transaction, Transaction_card


class WalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        field = ['first_name', 'last_name']


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

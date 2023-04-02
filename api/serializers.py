from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserCreatePasswordRetypeSerializer, \
    UserCreateSerializer

from wallet.models import UserAccount, Transaction


class UserAccountSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'user']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('account', 'transaction_time', 'amount')


class UserCreate(UserCreatePasswordRetypeSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'password']


class UserCreate(UserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name',]

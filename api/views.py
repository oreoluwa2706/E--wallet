from django.shortcuts import (get_object_or_404, render)
from rest_framework import status, generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from wallet.models import User, Transaction, Wallet, Transaction_card
from .permissions import IsAdminOrReadOnly
from .serializers import TransactionSerializer, WalletTransactionSerializer, Transaction_cardSerializer


class TransactionViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class WalletTransactionViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Wallet.objects.all()
    serializer_class = WalletTransactionSerializer


class TransactionCardViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Transaction_card.objects.all()
    serializer_class = Transaction_cardSerializer


@api_view()
def Transaction_detail(request, pk):
    try:
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def create_deposit(cls, account, amount):
    transaction = cls(
        account=account,
        type='D',
        amount=amount
    )
    account.deposit(amount)
    transaction.save()
    return transaction


@api_view()
def create_withdrawal(cls, account, amount):
    transaction = cls(
        account=account,
        type='W',
        amount=amount
    )
    account.withdraw(amount)
    transaction.save()
    return transaction


@api_view()
def create_transfer(self, from_account, to_account, amount):
    transaction = self(
        account=from_account,
        type='T',
        amount=amount
    )

    if amount > self.balance:
        raise ValueError("Insufficient balance")
    self.balance -= amount
    to_account.balance += amount
    self.save()
    to_account.save()
    from_account.transfer(to_account, amount)
    transaction.save()
    return transaction


@api_view()
def get(request, id):
    try:
        transaction = Transaction.objects.get(pk=id)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetAllTransaction:
    def get_transaction_history(self):
        return 'Transaction'.objects.filter(account=self).order_by('transaction_time')

from django.shortcuts import (get_object_or_404, render)

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from wallet.models import UserAccount, Transaction
from .permissions import IsAdminOrReadOnly
from .serializers import UserAccountSerializer, TransactionSerializer


class UserAccountViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class TransactionViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

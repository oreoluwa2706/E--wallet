from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('wallet', views.WalletTransactionViewSet)
router.register('transaction', views.TransactionViewSet)
router.register('transaction_card', views.TransactionCardViewSet)
router.register('account', views.AccountViewSet)
router.register('beneficiary', views.BeneficiaryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
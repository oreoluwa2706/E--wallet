from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Wallet, User, Transaction, Transaction_card, Account, Beneficiary


# Register your models here.

@admin.register(User)
class User(UserAdmin):
    pass


admin.site.register(Transaction)
admin.site.register(Transaction_card)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Beneficiary)


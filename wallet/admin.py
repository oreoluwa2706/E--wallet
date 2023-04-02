from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WalletUser, UserAccount, Transaction


# Register your models here.

@admin.register(WalletUser)
class User(UserAdmin):
    pass


admin.site.register(UserAccount)
admin.site.register(Transaction)

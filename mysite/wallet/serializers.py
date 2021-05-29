from rest_framework import serializers
from .models import Wallet

class CreateWallet(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('user','current_balance','created_at')





from django.db import models
from django.db import models
from django.conf import settings
from .errors import InsufficientBalance


class Wallet(models.Model):
    user = models.CharField(unique=True,max_length=100)
    current_balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def deposit(self, value):
        """It deposits a value to your wallet and creates a transaction
        with the deposited value.
        """
        self.transaction_set.create(
            value=value,
            running_balance=self.current_balance + value

        )
        self.current_balance += value
        self.save()

    def withdraw(self, value):
        if value > self.current_balance:
            raise InsufficientBalance("This wallet has insufficient balance ")

        self.transaction_set.create(
            value=value,
            running_balance=self.current_balance - value
        )
        self.current_balance -= value
        self.save()

    def transfer(self,wallet,value):
        self.withdraw(wallet,value)
        wallet.deposit(value)


class Transaction(models.Model):
    """A particular wallet holds this transaction"""
    wallet = models.ForeignKey(Wallet,on_delete=models.DO_NOTHING)
    """The value of this transaction"""
    value = models.FloatField(default=0)

    """The value of the wallet at the time of this transaction.
    useful for displaying transaction history in wallet
    """
    running_balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


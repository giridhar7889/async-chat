from django.db import IntegrityError


class InsufficientBalance(IntegrityError):
    """Raised when a wallet has insufficient balance to run
    an operation
    we're subclassing from mod:django.db.IntegrityError
    so that it automatically rollbacks to django transaction lifecycle.

"""

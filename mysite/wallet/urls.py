from django.urls import path
from .views import create_wallet


app_name = 'wallet'

urlpatterns = [
    path('create/',create_wallet.as_view(),name="create_wallet"),




]
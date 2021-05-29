from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Wallet
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateWallet


class create_wallet(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user

        create_wallet_serializer = CreateWallet(data=request.data)
        print(request.data)
        if create_wallet_serializer.is_valid():
            new_wallet = create_wallet_serializer.save()
            print(new_wallet)
            if new_wallet:
                return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)



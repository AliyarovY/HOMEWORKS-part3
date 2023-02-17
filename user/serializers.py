from .models import *

from payments.serializers import PaymentSerializer

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)


    class Meta:
        model = User
        fields = ('email', 'phone_number', 'city', 'avatar', 'payments',)

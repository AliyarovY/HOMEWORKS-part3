from django.contrib.auth.hashers import make_password

from .models import *

from payments.serializers import PaymentSerializer

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True, required=False)


    class Meta:
        model = User
        fields = ('email', 'phone_number', 'city', 'avatar', 'payments', 'password')


    def validate_password(self, value):
        return make_password(value)

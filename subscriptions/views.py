from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import SubscriptionSerializer
from .models import Subscription


class SubscriptionViewSet(mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

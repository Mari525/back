from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = "__all__"

class CourierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Courier
    fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = "__all__"
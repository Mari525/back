from .models import *
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  permissions_classes = [
    permissions.AllowAny
  ]
  serializer_class = OrderSerializer
  filter_backends = [SearchFilter, OrderingFilter]

  # @action(methods=['POST'], detail=True)
  # def delivered(self, request):
  #   order = self.get_object()
  #   is_delivered = json.loads(request.POST.get('is_delivered'))
  #   if is_delivered:
  #     order.is_delivered = True
  #   else:
  #     order.is_delivered = False
  #   order.save()
  #   return Response()

  @action(methods=['GET'], detail=False)
  def get_data(self, request):
    data = dict()
    data['info'] = ''
    return Response(data)



class CourierViewSet(viewsets.ModelViewSet):
  queryset = Courier.objects.all()
  permissions_classes = [
    permissions.AllowAny
  ]
  serializer_class = CourierSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['is_working']


class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  permissions_classes = [
    permissions.AllowAny
  ]
  serializer_class = CustomerSerializer


# class PageNumberPaginationDataOnly(PageNumberPagination):

#   def get_paginated_response(self, data):
#     return Response(data)
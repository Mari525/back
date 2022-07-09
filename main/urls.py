from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/order', OrderViewSet, 'order')
router.register('api/courier', CourierViewSet, 'courier')
router.register('api/customer', CustomerViewSet, 'customer')

urlpatterns = router.urls
from .models import Customer, Order
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .serializers import CustomerSerializer, OrderSerializer
from .signals import send_order_sms
import logging

logger = logging.getLogger(__name__)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            logger.error(f"Error creating customer: {e}")
            return Response({"detail": "Error creating customer"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return response
        except Exception as e:
            logger.error(f"Error updating customer: {e}")
            return Response({"detail": "Error updating customer"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            order = self.get_object()
            customer = order.customer
            message = f'New order placed: {order.item} for {order.amount} at {order.time}'
            send_order_sms(customer.phone_number, message)
            return response
        except Exception as e:
            logger.error(f"Error creating order: {e}")
            return Response({"detail": "Error creating order"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return response
        except Exception as e:
            logger.error(f"Error updating order: {e}")
            return Response({"detail": "Error updating order"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            return response
        except Exception as e:
            logger.error(f"Error deleting order: {e}")
            return Response({"detail": "Error deleting order"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

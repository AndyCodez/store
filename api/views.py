from .models import Customer, Order
from rest_framework import viewsets
from .serializers import CustomerSerializer, OrderSerializer
from .signals import send_order_sms

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        order = self.get_object()
        customer = order.customer
        message = f'New order placed: {order.item} for {order.amount} at {order.time}'
        send_order_sms(customer.phone_number, message)
        return response
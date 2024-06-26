# api/tests.py

from django.test import TestCase
from unittest.mock import patch
from decimal import Decimal
from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(name="John Doe", code="JD123", phone_number="+254705414060")

    def test_customer_creation(self):
        customer = Customer.objects.get(code="JD123")
        self.assertEqual(customer.name, "John Doe")

class OrderModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", code="JD123", phone_number="+254705414060")

    @patch('api.signals.send_sms')  # Mock the send_sms function
    def test_order_creation(self, mock_send_sms):
        order = Order.objects.create(customer=self.customer, item="Widget", amount=Decimal('19.99'))
        self.assertEqual(order.amount, Decimal('19.99'))
        mock_send_sms.assert_called_once_with(self.customer.phone_number, 'Order placed: Widget for $19.99')

    def test_order_creation_multiple_objects(self):
        Order.objects.create(customer=self.customer, item="Phone", amount=Decimal('599.99'))
        Order.objects.create(customer=self.customer, item="Tablet", amount=Decimal('349.50'))
        orders = Order.objects.filter(customer=self.customer)
        self.assertEqual(len(orders), 2)

    def test_order_deletion(self):
        order = Order.objects.create(customer=self.customer, item="Laptop", amount=Decimal('1099.99'))
        order.delete()
        orders = Order.objects.filter(customer=self.customer)
        self.assertEqual(len(orders), 0)

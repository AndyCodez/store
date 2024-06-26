from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .services import send_sms

@receiver(post_save, sender=Order)
def send_order_sms(sender, instance, created, **kwargs):
    if created:
        customer = instance.customer
        message = f"Order placed: {instance.item} for ${instance.amount}"
        send_sms(customer.phone_number, message)

import os
import africastalking

# Initialize SDK
username = os.getenv('AT_USER')
api_key = os.getenv('AT_API_KEY')

africastalking.initialize(username, api_key)

sms = africastalking.SMS

def send_sms(phone_number, message):
    print(f"Sending SMS to {phone_number}: {message}")
    response = sms.send(message, [phone_number])
    return response

from sms import send_sms

def send_notification(phone_number, message):
    response = send_sms(phone_number,message)
    return response

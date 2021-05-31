from sms import ZamtelSMSApi

#instatiate the sms class
zamtel_sms = ZamtelSMSApi()

def send_notification(phone_number, message):
    response = zamtel_sms.send_sms(phone_number,message)
    return response


send_notification('0966468776','Hello')
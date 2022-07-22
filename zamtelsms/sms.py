from zamtelsms.smsapi.zamtel import ZamtelSMSApi
#instatiate the sms class
zamtel_sms = ZamtelSMSApi()

def send_sms(phone_number, message):
    response = zamtel_sms.send_sms(phone_number,message)
    return response
    
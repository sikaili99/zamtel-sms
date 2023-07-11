from decouple import config
import requests
import  json

class ZamtelSMSApi():
    """
    This simple code is used to send notification messages to users
    using the Zamtel bulk SMS API 
    """
    def __init__(self):
        self.api_key=config("ZAMTEL_API_KEY")
        self.sender_id=config("ZAMTEL_SENDER_ID")
        self.base_url=config("ZAMTEL_BASE_URL")

    def send_sms(self,phone_number, message):
        response = requests.post(f"{self.base_url}api_key/{self.api_key}/contacts/{phone_number}/senderId/{self.sender_id}/message/{message}")
        return json.loads(response.text)

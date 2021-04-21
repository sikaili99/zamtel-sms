import requests
import  json
import os

# ZAMTEL BULKSMS API CREDS
api_key=os.environ.get("API_KEY")
sender_id=os.environ.get("SENDER_ID")
base_url=os.environ.get("BASE_URL")

def send_sms(phone_number, message):
    response = requests.post(f"{base_url}api_key/{api_key}/contacts/{phone_number}/senderId/{sender_id}/message/{message}")
    return json.loads(response.text)
    
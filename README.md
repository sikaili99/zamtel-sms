Zamte SMS
==========================

Zamtel bulk SMS api example in Python

# Installation

` pip install zamtelsms `

# Setup 
Create a .env file in the root of your project and add the following
```
API_KEY=YOUR_API_KEY_FROM_ZAMTEL
SENDER_ID=YOUR_SENDER_ID_FROM_ZAMTEL
BASE_URL=https://bulksms.zamtel.co.zm/api/v2.1/action/send/

```
* API_KEY is the API_KEY you can from Zamtel
* SENDER_ID is the SENDER_ID you can from Zamtel

# Usage

You can use the function to send a single here is an example

```
from sms import send_sms

response = send_sms('0975442232', 'Hello there, I am testing the Zamtel Bulk SMS API')

print(response)
```

You can also pass an array of phone numbers to send a sms SMS to multiple clients. 

```
from sms import send_sms

phone_numbers = ['0976xxxxxx','0976xxxxxx','0976xxxxxx','0976xxxxxx','0976xxxxxx',]

message = 'Hello there, I am testing the Zamtel Bulk SMS API'

response =  send_sms(phone_numbers, message)

print(response)

# output

{'success': True, 'responseText': 'SMS(es) have been queued for delivery'}

```

It is as simple as that 😃

Happy coding!!

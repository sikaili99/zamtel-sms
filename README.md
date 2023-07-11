Zamtel bulk SMS api example in Python
==========================

# Installation

` pip install zamtelsms `

# Setup 
Create a .env file in the root of your project and add the following
```
ZAMTEL_API_KEY=YOUR_API_KEY_FROM_ZAMTEL
ZAMTEL_SENDER_ID=YOUR_SENDER_ID_FROM_ZAMTEL
ZAMTEL_BASE_URL=https://bulksms.zamtel.co.zm/api/v2.1/action/send/

```
* ZAMTEL_API_KEY is the API_KEY you were given by Zamtel
* ZAMTEL_SENDER_ID is the ZAMTEL_SENDER_ID you were given by Zamtel

# Usage

You can use the function to send a single here is an example

```
from zamtelsms.sms import send_sms

response = send_sms('0975442232', 'Hello there, I am testing the Zamtel Bulk SMS API')

print(response)
```

You can also pass an array of phone numbers to send a sms SMS to multiple clients. 

```
from zamtelsms.sms import send_sms

phone_numbers = ['0976xxxxxx','0976xxxxxx','0976xxxxxx','0976xxxxxx','0976xxxxxx',]

message = 'Hello there, I am testing the Zamtel Bulk SMS API'

response =  send_sms(phone_numbers, message)

print(response)

# output

{'success': True, 'responseText': 'SMS(es) have been queued for delivery'}

```

It is as simple as that 😃

Happy coding!!

# zamtel-sms
Zamtel bulk SMS api example in Python

You can use the `send_notification` function like this

`send_notification('0975442232', 'Hello there, I am testing the Zamtel Bulk SMS API')`

You can also pass an array of phone numbers to send a notification SMS to multiple clients. 

```
phone_numbers = ['0976xxxxxx','0976xxxxxx','0976xxxxxx','0976xxxxxx','0976xxxxxx',]

message = 'Hello there, I am testing the Zamtel Bulk SMS API'

send_notification(phone_numbers, message)

```

It is as simple as that 😃

Happy coding!!

import requests
import json
from typing import List

telephone_numbers = ["233593523188", "233556977474", "233595123202","233242815291"]
sender = "FireAlert"
houseNumber = "CoDE"

message = f"A fire has been identified in {houseNumber}. It's an emergency!"

def sendSMS(sender: str=sender, message: str=message, phone_numbers: List[str]=telephone_numbers):
    data = {
        'sender': sender,
        'message': message,
        'recipients': phone_numbers
    }

    headers = {
        'api-key': "eU1JY3VmU3FydGRzUW9GdVdwb1k",
        "Content-Type": "application/json"
    }
    params = json.dumps(data)
    messageResponse = requests.post(
        url="https://sms.arkesel.com/api/v2/sms/send",
        data=params,
        headers=headers)
    print(messageResponse.json())
    return messageResponse.json()
import time
import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()


def get_status(user_id):
    vk_url = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': user_id,
        'fields': "online",
        'v': 5.92,
        'access_token': os.getenv('Token')
    }
    response = requests.post(vk_url, params=params)
    return response.json().get('response')[0]['online']


def sms_sender(sms_text):
    account_sid = os.getenv('twilio_sid')
    auth_token = os.getenv('twilio_token')
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="2 sms s kompa",
            from_=os.getenv('NUMBER_FROM'),
            to=os.getenv('NUMBER_TO')
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)

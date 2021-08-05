# by Dhwani Vaishnav, inspired by Bukola on YouTube. 
# Fun facts courtesy of @/anfederico on GitHub

import random, schedule, time
from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number


# open funfacts.txt
file1 = open("funfacts.txt", "a")
FUN_FACTS = file1.readlines()

cellphone = 6472547321
twilio_number = 4432130126

def send_message(fact = FUN_FACTS):
    account = "AC8590056f5c367407feb1bad4fe3c1754"
    token = "647b2d8a676153a597905ca752c8082d"
    client = Client(account, token)

    client.messages.create(to=cellphone, from_=twilio_number, body=fact)

# random library
fact = FUN_FACTS[random.randint(0, len(FUN_FACTS))]

# schedule texts
schedule.every().day.at("13:00").do(send_message, fact)
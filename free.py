import time
import random, string
from discord import Webhook, RequestsWebhookAdapter

link = input("Webhook Link : ")
amount = int(input("How many codes to generate : "))
for i in range(amount):
    time.sleep(5)
    code = "https://discord.gift/" + "".join(random.choices(string.ascii_letters + string.digits, k=16))
    print("[GENERATED] " + code)
    webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
    webhook.send(code)

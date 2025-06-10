from flask import Flask
from threading import Thread
from telethon.sync import TelegramClient
import os
import time

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")
recipient = os.getenv("TARGET_USERNAME")  # Use string instead of int

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

with TelegramClient('session', api_id, api_hash) as client:
    # Optional: Print all dialog IDs
    # for dialog in client.iter_dialogs():
    #     print(dialog.name, dialog.id)

    while True:
        client.send_message(recipient, """
车随叫随到，整个柬埔寨哪儿都可以到只要您联系我们

👍  金边到外省价位表：

📍 金边   ➡️   西港    =70$
📍 金边   ➡️   木牌    =50$
📍 金边   ➡️   财通    =35$
📍 金边   ➡️   七星海  =75$
📍 金边   ➡️   暹粒    =75$
📍 金边   ➡️   戈公    =85$
📍 金边   ➡️   波贝    =110$
📍 金边   ➡️   拜林    =110$
📍 金边   ➡️   波哥山  =70$
📍 金边   ➡️   开普    =60$ 
📍 金边   ➡️   贡布    =55$
📍 西港   ➡️   戈公    =85$ 
📍 西港   ➡️   七星海  =70$
📍 西港   ➡️   贡布    =55$
📍 西港   ➡️   财通    =100$
📍 西港   ➡️   木牌    =110$
📍 西港   ➡️   暹粒    =145$

➡️ @Ai520z
🎉 +855 76 668 9568

🔗 https://t.me/Rentcar2025""")
        time.sleep(3600)  # every 1 hour


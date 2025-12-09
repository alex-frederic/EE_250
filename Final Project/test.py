import requests
import os

print("ALERT: Human detected!")
os.system("curl -X POST https://pcrawseesaw.app.n8n.cloud/webhook/send-sms-alert")

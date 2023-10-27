import requests

url = "https://whatsva.id/api/sendMessageText"

payload = "{\r\n    \"instance_key\": \"rIhmFbFiFJvR\",\r\n    \"jid\": \"083837358230\",\r\n    \"message\": \"hello admin\"\r\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

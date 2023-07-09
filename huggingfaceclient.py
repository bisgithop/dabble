import json
import requests
API_TOKEN = "GET IT FROM HUGGING FACE"

API_URL = "https://api-inference.huggingface.co/models/gpt2-xl"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query("hi")
for i in data:
    print(data)

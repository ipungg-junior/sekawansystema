import requests

TOKEN = '7437934173:AAGFDh6nw09HFCGMUVOxesSzLQMBAK__rUQ'
URL = f'https://api.telegram.org/bot{TOKEN}/'

def broadcast(message):
    payload = {
        'chat_id': -1002171465011,
        'text': message
    }
    response = requests.post(URL + 'sendMessage', data=payload)
    return response.json()

def get_updates(debug=False):
    tmp = []
    response = requests.get(URL + 'getUpdates').json()
    if (debug):
        print(response)
    for update in response['result']:
        if 'message' in update:
            tmp.append(update['message']['chat']['id'])
    return tmp


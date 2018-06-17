from datetime import datetime, timedelta
import requests
import json

GOMIDASI_PAIR = [
        ['月曜日', '普通ゴミ'],
        ['火曜日', '空き缶、ペットボトル、空き瓶、乾電池'],
        ['水曜日', 'プラスチック製容器包装'],
        ['木曜日', '普通ゴミ'],
        ['金曜日', 'なし'],
        ['土曜日', 'ミックスペーパー'],
        ['日曜日', 'なし']
        ]

def get_text():
    wday = (datetime.today() + timedelta(days=1)).weekday()
    if wday == 4 or wday == 6:
        text = '明日は、何も無い日ですよ。'
    else:
        pair = GOMIDASI_PAIR[wday]
        text = '明日の%sは、%sの日ですよ。' % (pair[0], pair[1])
    return text

def get_access_token(chan_id, chan_secret):
    endpoint = 'https://api.line.me/v2/oauth/accessToken'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'client_credentials', 'client_id': chan_id, 'client_secret': chan_secret}
    r = requests.post(endpoint, data=payload, headers=headers)
    return json.loads(r.text)['access_token']

def push_message(text, access_token, to=[]):
    endpoint = 'https://api.line.me/v2/bot/message/push'
    headers = {'content-type': 'application/json', 'authorization': 'Bearer %s' % access_token}
    for i in to:
        payload = {'to': i, 'messages': [{'type': 'text', 'text': text}]}
        requests.post(endpoint, headers=headers, json=payload)

if __name__ == '__main__':
    chan_id = ''
    chan_secret = ''
    to = ['']
    text = get_text()
    access_token = get_access_token(chan_id, chan_secret)
    push_message(text, access_token, to)

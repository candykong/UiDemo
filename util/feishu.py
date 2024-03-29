import requests
import json

def send_feishu_message(webhook_url, message):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'msg_type': 'text',
        'content': {
            'text': message
        }
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        print("消息发送成功")
    except requests.exceptions.RequestException as e:
        print("消息发送失败:", str(e))

# # 替换成您自己的飞书机器人 webhook URL
# webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/3a029b35-396c-46c7-8f53-133efc1ee78f'
# message = 'Hello, 飞书!'
# send_feishu_message(webhook_url, message)
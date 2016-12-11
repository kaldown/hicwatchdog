#! -*- coding: utf-8 -*-

import requests

BOT_TOKEN = '302872852:AAFCedWRxyVoMWmq7V9bkjeKXDSSHw6xbNg'

BASE_URL = 'https://api.telegram.org/bot{token}/{method}'

hook_url = 'https://hicwatchdog.herokuapp.com/'

def set_web_hook():
    url = BASE_URL.format(token=BOT_TOKEN, method='setWebhook')
    return requests.get(url, params={'url': hook_url+'/hicwatchdog_hook/'})

def get_web_hook_info():
    url = BASE_URL.format(token=BOT_TOKEN, method='getWebhookinfo')
    return requests.get(url)

def send_message(**kwargs):
    url = BASE_URL.format(token=BOT_TOKEN, method='sendMessage')
    return requests.get(url, params=kwargs)


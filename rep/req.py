import requests

def get_html(url):
    req = requests.get(url)
    return req.text
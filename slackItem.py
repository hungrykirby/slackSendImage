import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class SlackItem:
  token = None

  def __init__(self):
    self.token = os.environ.get("TOKEN")

  def post_with_img(self, img_path):
    token = self.token
    url = "https://slack.com/api/files.upload"
    data = {
      'token': token,
      'channels': '#imgs',
      'title': 'my file',
      'initial_comment': "initilal\ncomment"
    }
    img_file = {'file': open(img_path, 'rb')}
    if token:
      requests.post(url, data=data, files=img_file)
  
  def test(self):
    # 設定
    url = 'https://slack.com/api/chat.postMessage'
    token = self.token
    CHANNEL='#imgs'
    TEXT='test'

    post_json = {
        'token': self.TOKEN,
        'text': TEXT,
        'channel': CHANNEL,
        'link_names': 1
    }
    if token:
      requests.post(url, data = post_json)

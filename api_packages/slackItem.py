import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class SlackItem:
  token = None
  channel = None
  SLACK_API_BASE = "https://slack.com/api/"

  def __init__(self, channel = 'imgs'):
    self.token = os.environ.get("TOKEN")
    self.channel = channel

  def post_with_img(self, img_path, file_title, initial_comment):
    token = self.token
    channel = self.channel
    url = self.SLACK_API_BASE + "files.upload"
    data = {
      'token': token,
      'channels': '#' + channel,
      'title': file_title,
      'initial_comment': initial_comment
    }
    img_file = {'file': open(img_path, 'rb')}
    if token:
      requests.post(url, data=data, files=img_file)
  
  def post_text(self, text):
    url = self.SLACK_API_BASE + 'chat.postMessage'
    token = self.token
    # print(self.channel)

    post_json = {
      'token': token,
      'text': text,
      'channel': '#' + self.channel,
      'link_names': 1
    }
    if token:
      requests.post(url, data = post_json)
  
  def test(self):
    url = self.SLACK_API_BASE + 'chat.postMessage'
    token = self.token
    text = "test post"

    post_json = {
        'token': token,
        'text': text,
        'channel': '#' + self.channel,
        'link_names': 1
    }
    if token:
      requests.post(url, data = post_json)

import requests
from bs4 import BeautifulSoup
import datetime

class HtmlFetcher:
  url = None

  def __init__(self, url):
    self.url = url

  def fetch_pressure_from_jma(search_time = datetime.datetime.now()):
    url = "https://www.jma.go.jp/jp/amedas_h/today-44132.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    trs = soup.select("div#div_table > table > tr")
    for tr in trs:
      tds = tr.select("td")
      # 2hours ago
      print(tds)
    print("---")
    # print(trs)
    print("---")

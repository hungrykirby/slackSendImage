import requests
from bs4 import BeautifulSoup
import datetime

import re

class HtmlFetcher:
  url = None

  def __init__(self, url):
    self.url = url

  def fetch_pressure_from_jma(self, search_time = datetime.datetime.now()):
    url = "https://www.jma.go.jp/jp/amedas_h/today-44132.html"
    try:
      res = requests.get(url)
      soup = BeautifulSoup(res.text, 'html.parser')
      trs = soup.select("div#div_table > table > tr")
      list_time_pressure = []
      for tr in trs:
        tds = tr.select("td")
        # print(tds[0].get_text().isdigit())
        if tds[0].get_text().isdigit() and tds[8].get_text().replace('\xa0', ''):
          list_time_pressure.append(
            {
              'time': int(tds[0].get_text()),
              'pressure': tds[8].get_text()
            }
          )
      if len(list_time_pressure) == 0:
        return None
      else:
        date_place_title = soup.select("table#tbl_title td.td_title")[0].get_text()
        year = re.search(r'\d{4}年', date_place_title).group()[0:4]
        month = re.search(r'\d{2}月', date_place_title).group()[0:2]
        day = re.search(r'\d{2}日', date_place_title).group()[0:2]
        place = re.search(r'\s+\D+\Z', date_place_title).group()[1:]
        result = {}

        if search_time:
          # 指定した時刻に最も近いデータを取得
          sorted_time_pressures = sorted(list_time_pressure, key=lambda x: abs(int(search_time.hour - x['time'])))
        # もっとも時間が最近のものを取得
        sorted_time_pressures = sorted(list_time_pressure, key=lambda x:-x['time'])
        result = {
          'data': sorted_time_pressures,
          'info': {'day': day, 'month': month, 'year': year, 'place': place}
        }
        return result
    except Exception as e:
      print(e)
      return False

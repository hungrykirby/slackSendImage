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
    list_time_pressure = []
    for tr in trs:
      tds = tr.select("td")
      print(tds[0].get_text().isdigit())
      if tds[0].get_text().isdigit() and tds[8].get_text().replace('\xa0', ''):
        list_time_pressure.append(
          {
            'time': int(tds[0].get_text()),
            'pressure': tds[8].get_text()
          }
        )
    print("---")
    if len(list_time_pressure) == 0:
      return None
    else:
      sorted_time_pressures = sorted(list_time_pressure, key=lambda x:-x['time'])
      nearest = sorted_time_pressures[0]
    print(nearest)
    print("---")

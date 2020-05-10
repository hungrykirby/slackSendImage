from api_packages import slackItem
from api_packages import googleItem
from data_packages import fetchHtml
from data_packages import generateGraph
import sys

import datetime

def main():
  args = sys.argv
  now = datetime.datetime.now()
  file_name = now.strftime("%Y_%m_%d_%H_%M_%S")
  # print(args)
  if len(args) > 1:
    channel = args[1]
  else:
    channel = 'imgs'
  si = slackItem.SlackItem(channel)
  fetched_html = fetchHtml.HtmlFetcher(None)
  fetched_html_data = fetched_html.fetch_pressure_from_jma(None)
  if fetched_html_data is None or fetched_html_data == False:
    return False
  text = 'Place: ' + fetched_html_data['info']['place']
  text += '\nDate: ' + fetched_html_data['info']['day'] + '\n'
  text += str(fetched_html_data['data'][0]['time']) + '時の気圧は'
  text += fetched_html_data['data'][0]['pressure'] + 'hPaです'
  # si.post_text(text)
  if len(args) > 1:
    dev = True
  else:
    dev = False
  g = googleItem.GoogleItem(dev)
  g.write_pressure_spreadsheet(
    fetched_html_data['info']['place'],
    fetched_html_data['info']['year'],
    fetched_html_data['info']['month'],
    fetched_html_data['info']['day'],
    fetched_html_data['data'][0]['time'],
    fetched_html_data['data'][0]['pressure']
  )
  data_for_graph = g.fetch_pressure_time(12)
  generator = generateGraph.GraphGenerator("relation of pressure and time", file_name + '.png')
  generator.set_labels('time', 'pressure')
  generator.create_pressure_graph(list(reversed(data_for_graph['time'])), list(reversed(data_for_graph['pressure'])))

  si.post_with_img(file_name + '.png', '保存した画像', text)

if __name__ == "__main__":
  print("Hello bot")
  main()
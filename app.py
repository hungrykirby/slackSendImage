from api_packages import slackItem
from api_packages import googleItem
from data_packages import fetchHtml
import sys

def main():
  args = sys.argv
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
  si.post_text(text)

  g = googleItem.GoogleItem()
  g.write_pressure_spreadsheet(
    fetched_html_data['info']['place'],
    fetched_html_data['info']['year'],
    fetched_html_data['info']['month'],
    fetched_html_data['info']['day'],
    fetched_html_data['data'][0]['time'],
    fetched_html_data['data'][0]['pressure']
  )

if __name__ == "__main__":
  print("Hello bot")
  main()
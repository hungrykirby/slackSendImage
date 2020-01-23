import slackItem
import fetchHtml

def main():
  si = slackItem.SlackItem()
  fetched_html = fetchHtml.HtmlFetcher(None)
  fetched_html_data = fetched_html.fetch_pressure_from_jma(None)
  if fetched_html_data is None:
    return False
  text = str(fetched_html_data[0]['time']) + '時の気圧は'
  text += fetched_html_data[0]['pressure'] + 'hPaです'
  si.post_text(text)

if __name__ == "__main__":
  print("Hello bot")
  main()
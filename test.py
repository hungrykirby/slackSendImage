import fetchHtml

test = fetchHtml.HtmlFetcher(None)

hoge = test.fetch_pressure_from_jma()
print(hoge)
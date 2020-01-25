from data_packages import fetchHtml
a = fetchHtml.HtmlFetcher(None).fetch_pressure_from_jma()
print(a)
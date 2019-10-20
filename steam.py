<<<<<<< HEAD
import requests
import lxml.html
import pandas as pd

html = requests.get('https://store.steampowered.com/search/?filter=topsellers')
doc = lxml.html.fromstring(html.content)

titles = doc.xpath('.//div[@id="search_result_container"]')[0]

span = titles.xpath('.//span[@class="title"]/text()')

tbl = pd.DataFrame(span, columns=['Top Selling Games'])

print(tbl)
=======
import requests
import lxml.html
import pandas as pd

html = requests.get('https://store.steampowered.com/search/?filter=topsellers')
doc = lxml.html.fromstring(html.content)

titles = doc.xpath('.//div[@id="search_result_container"]')[0]

span = titles.xpath('.//span[@class="title"]/text()')

tbl = pd.DataFrame(span, columns=['Top Selling Games'])

print(tbl)
>>>>>>> 442c5b8a5ce823a66f5760c011c127b99dde1d1f

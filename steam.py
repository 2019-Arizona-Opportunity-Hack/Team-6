import requests
import lxml.html
import pandas as pd
import plotly.graph_objects as go

html = requests.get('https://store.steampowered.com/search/?filter=topsellers')
doc = lxml.html.fromstring(html.content)

# new_releases = doc.xpath('//div[@id="tab_topsellers_content"]')[0]

titles = doc.xpath('.//div[@id="search_result_container"]')[0]

span = titles.xpath('.//span[@class="title"]/text()')

tbl = pd.DataFrame(span, columns=['Games'])
arr = tbl.values

fig = go.Figure(data=[go.Table(
    header=dict(values=['Top Selling Games'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[arr], # 2nd column
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
])

fig.show()

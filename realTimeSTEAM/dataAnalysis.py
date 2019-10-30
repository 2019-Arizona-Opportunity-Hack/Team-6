import pandas as pd
import chart_studio.plotly as py
from pytrends.request import TrendReq
import plotly.express as px
import chart_studio.tools as tls

from cachetools import cache, TTLCache, cached

cache = TTLCache(maxsize=100, ttl=300)  # 2 - let's create the cache object.



pytrends = TrendReq(hl='en-US', tz=360)
def related(list1, list2): # find if the the 2 lists are related
    for i in list1:
        for j in list2:
            if i in j:
                return True
    return False
def showInfo():
    info = pd.read_csv("Fan_Fusion_Panels.csv", encoding ="ANSI")
    print(info)
#showInfo()
def toLower(text): # make string to lowercase
    newText = text.lower()
    return newText
def removeSpecialChar(text): # get rid of special characters
    k = text.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~=_+"})
    return k

@cached(cache)
def findTrends(keywords):
    trending =[]
    df = pytrends.trending_searches(pn='united_states')
    for i in df[0]:
        #print(i)
        kw_list = [i]
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
        top = pytrends.related_topics() #find related topic
        k = removeSpecialChar(i)
        topics = top[k]['top']['topic_type']
        lowerTop = topics.apply(toLower)
        topics = lowerTop.apply(removeSpecialChar)
        list_topic = list(topics)
        #print(list_topic)
        if related(keywords, list_topic):
            trending.append(str(i))
    return trending
def embedPlotly(html):
    tls.get_embed(html)
def plotInterest(list):
    kw_list = [list]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='')
    interest = pytrends.interest_over_time()
    df = interest[list]
    x_axis = df.index.to_frame()
    #print(x_axis)
    fig = px.line(df,x = x_axis['date'],  y=df)
    py.iplot(fig, filename = 'timeline')
    first_plot_url = py.plot(fig, filename='timeline', auto_open=False,)

    embedPlotly(first_plot_url)
    result = first_plot_url+".embed"
    return result



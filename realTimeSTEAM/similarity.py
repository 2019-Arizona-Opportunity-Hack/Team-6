from monkeylearn import MonkeyLearn
import wikipedia
import realTimeSTEAM.dataAnalysis as s
import pandas as pd
import plotly.express as px
import chart_studio.plotly as py

def findPercentage(keyword):
    s = wikipedia.search(keyword)
    result=wikipedia.page(s[0])
    #print(result.content)
    ml = MonkeyLearn('f38c742c00e4f06a2442863e6fa13f0e6f13fc44')
    response = ml.classifiers.classify(
        model_id='cl_LNaB7RwX',
        data=[
            result.content,
        ]
    )
    j = response.body
    confidence = j[0]['classifications'][0] #['confidence']
    return confidence

def allPercentage():
    trend = s.findTrends("film")
    l = []
    col =['trend', 'tag', 'confidence']
    df = pd.DataFrame(columns= col)
    for i in trend:
        values = findPercentage(i)
        x = values['confidence']
        tag = values['tag_name']
        l.append([i,tag, x])
        #df.append({'trend': i, 'tag': tag, 'confidence':x}, ignore_index=True)

    return df.append(pd.DataFrame(l, columns=col))

#print(allPercentage())
def plotSimilarity():
    data = allPercentage()
    fig = px.bar(data, x='trend', y='confidence', hover_data=['tag'], labels={'trend':'trending on Google'})
    py.iplot(fig, filename = 'barChart')
    first_plot_url = py.plot(fig, filename='barChart', auto_open=False,)
    s.embedPlotly(first_plot_url)
    result = first_plot_url+".embed"
    return result

#print(plotSimilarity())

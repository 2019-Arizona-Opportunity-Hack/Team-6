import requests
import lxml.html
import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objects as go
import tweepy
import realTimeSTEAM.dataAnalysis as d

def plotTwitter():
    consumer_key= "Q0um0FyLCoKbHxEYX05PrUrRs"
    consumer_secret = "aoDkrmtJE1oycLmtkgNcWhC00QVfcf7vvsXhzocplj5kig2XR0 "
    access_token = "93130299-crrOgEkv4QECLKl52U0J863f1lvCNIY2tVK8UaECX"
    access_token_secret = "gs7RjaLpxo9HYBeXUcgSt6tR3qMcoEbVdPJbsRlM0L9pB"
    #setting access token and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #creating API object passing auth info
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #public_tweets = api.home_timeline()

    query = "Science"
    language = "en"

    results = api.search(q=query, lang=language)

    for tweet in results:
        print tweet.user.screen_name, "Tweeted: ", tweet.text

    for tweet in public_tweets:
        print tweet.text
        print tweet.created_at
        print tweet.user.screen_name
        print tweet.user.location
    
    fig = go.Figure(data=[go.Table(
        header=dict(values=['public_tweets'],
                    line_color='darkslategray',
                    fill_color='lightskyblue',
                    align='left'),
      
    ])
    py.iplot(fig, filename = 'twitterPlot')
    first_plot_url = py.plot(fig, filename='twitterPlot', auto_open=False,)

    d.embedPlotly(first_plot_url)
    result = first_plot_url+".embed"
    return result

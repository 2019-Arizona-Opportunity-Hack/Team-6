from flask import Flask, render_template, Response, request
import Twitter as tw
app = Flask(__name__,
            static_folder='templates/assets')

@app.route('/', methods=["GET"])
@app.route('/index',methods=["GET"])
def index():
    #url = s.plotInterest("Star wars")
    url = "https://plot.ly/~ccharmander4/69.embed"
    #steam = st.plotSteam()
    steam = "https://plot.ly/~ccharmander4/80.embed"
    if request.method=="GET":
        text = request.form["topic"]
        tw.twitter_wordcloud(text)
    return render_template("index.html", googleTrend = url, steamTrend = steam)

""""@app.route('/', methods=["GET"])
def generate_wordcloud():
    text = request.form["topic"]
    tw.twitter_wordcloud(text)
    return render_template("table.html")
"""
@app.route('/table')
def table():
    return render_template("table.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/data')
def data():
    with open("data.csv") as fp:
        csv = fp.read()
    #csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=data_trend.csv"})
app.config['ENV']='development'
app.config['DEBUG']=True

import os

port = int(os.environ.get('PORT',4000))

app.run(host='0.0.0.0', port=port,debug=True)


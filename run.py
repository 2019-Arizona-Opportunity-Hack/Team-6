from flask import Flask, render_template, Response

app = Flask(__name__,
            static_folder='templates/assets')

@app.route('/')
def index():
    #url = s.plotInterest("Star wars")
    url = "https://plot.ly/~ccharmander4/69.embed"
    topTrends = "//plot.ly/~ccharmander4/57.embed"
    #steam = st.plotSteam()
    steam = "https://plot.ly/~ccharmander4/80.embed"
    return render_template("index.html", topTrend = topTrends, googleTrend = url, steamTrend = steam)

@app.route('/table')
def table():
    return render_template("table.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/data')
def data():
    with open("outputs/Adjacency.csv") as fp:
        csv = fp.read()
    #csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=data.csv"})
app.config['ENV']='development'
app.config['DEBUG']=True

import os

port = int(os.environ.get('PORT',3000))

app.run(host='0.0.0.0', port=port,debug=True)


from flask import Flask, render_template, Response
import realTimeSTEAM.dataAnalysis as s
import realTimeSTEAM.similarity as sim
import realTimeSTEAM.table as t
import steam as st
#from app import app

app = Flask(__name__,
            static_folder='templates/assets')

@app.route('/')
def index():
    #url = s.plotInterest("Star wars")
    url = "https://plot.ly/~ccharmander4/69"
    topTrends = "//plot.ly/~ccharmander4/57.embed"
    steam = st.plotSteam()
    return render_template("index.html", topTrend = topTrends, googleTrend = url, steamTrend = steam)

@app.route('/table')
def table():
    return render_template("table.html", table=t.getTable())

@app.route('/data')
def data():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    csv = '1,2,3\n4,5,6\n'
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


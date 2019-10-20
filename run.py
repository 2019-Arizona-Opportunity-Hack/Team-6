from flask import Flask, render_template
import realTimeSTEAM.dataAnalysis as s
import realTimeSTEAM.similarity as sim
#from app import app

app = Flask(__name__,
            static_folder='templates/assets')

@app.route('/')
def index():
    url = s.plotInterest("Star wars")
    topTrends = "//plot.ly/~ccharmander4/57.embed"
    return render_template("index.html", topTrend = topTrends, googleTrend = url)
app.config['ENV']='development'
app.config['DEBUG']=True

import os

port = int(os.environ.get('PORT',3000))

app.run(host='0.0.0.0', port=port,debug=True)


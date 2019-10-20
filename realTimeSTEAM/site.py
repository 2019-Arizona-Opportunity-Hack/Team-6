import realTimeSTEAM.dataAnalysis as s
from flask import Flask, render_template
#
#from app import app

app = Flask(__name__,
            static_folder='templates/assets')

@app.route('/')

def index():
    url = s.plotInterest("Star wars")
    return render_template("index.html", googleTrend = url)
app.config['ENV']='development'
app.config['DEBUG']=True

app.run(host='0.0.0.0', port=3000,debug=True)


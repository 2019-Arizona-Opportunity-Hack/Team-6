from flask import Flask, render_template
#import steam as s
#from app import app

app = Flask(__name__,
            static_folder='templates/assets')

@app.route('/')
#url = s.plotInterest("Star wars")
def index():
    return render_template("index.html", googleTrend = "https://plot.ly/~ccharmander4/5/.embed")
app.config['ENV']='development'
app.config['DEBUG']=True

app.run(host='0.0.0.0', port=3000,debug=True)


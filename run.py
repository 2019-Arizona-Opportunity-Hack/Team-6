from flask import Flask, render_template, Response, request, flash
import Twitter as tw
app = Flask(__name__,
            static_folder='templates/assets')

@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    error = None
    url = "https://plot.ly/~ccharmander4/69.embed"
        #steam = st.plotSteam()
    steam = "https://plot.ly/~ccharmander4/80.embed"
    try:
            text = request.args.get("topic")
            tw.twitter_wordcloud(text)
            img = "assets/img/"+text+".png"
            return render_template("index.html", googleTrend = url, steamTrend = steam, img_source = img)

    except Exception as e:
        #flash(e)
        #url = s.plotInterest("Star wars")

        return render_template("index.html", googleTrend = url, steamTrend = steam)


@app.route('/table')
def table():
    return render_template("table.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/data')
def data():
    with open("templates/assets/csv/twitter_report.csv", encoding='utf-8') as fp:
        csv = fp.read()
    #csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=twitter_data_report.csv"})

@app.route('/data2')
def data2():
    with open("templates/assets/csv/words_frequency.csv", encoding='utf-8') as fp:
        csv = fp.read()
    #csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=context_words_frequency.csv"})
app.config['ENV']='development'
app.config['DEBUG']=True

import os

port = int(os.environ.get('PORT',4000))

app.run(host='0.0.0.0', port=port,debug=True)


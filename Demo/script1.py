from flask import Flask, request, render_template
from dbConnect import getCurrencyNames
from flask_bootstrap import Bootstrap
from wordsFrequency import getWordsFreq

#crypto flask app
app = Flask(__name__)
Bootstrap(app)

# home page
@app.route('/')
def index():
    return render_template("home.html")

# currency details
@app.route('/currency/<c_name>')
def currency_dashboard(c_name):
    return render_template("c_dashboard.html", c_name=c_name)

# currency list
@app.route('/list')
def listdisplay():
    value_table = getCurrencyNames()
    currencies = []
    for row in value_table:
        currencies.append(row[0])
    return render_template("list.html", currencies=currencies)

# word cloud data
@app.route('/word_cloud')
def word_cloud():
    try:
        words_json = getWordsFreq()
        return words_json
    except:
        return []



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template, Response
from dbConnect import getCurrencyNames, getDomains, readCurrencies
from flask_bootstrap import Bootstrap
from wordsFrequency import getWordsFreq
from similarity import getCurrencyPopularity
import json
from wtforms import TextField, Form

# crypto flask app
app = Flask(__name__)
Bootstrap(app)


class SearchForm(Form):
    autocomp = TextField('Enter Currency name', id='currency_autocomplete')

# home page
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/allcurrencies', methods=['GET'])
def allcurrencies():
    value_table = readCurrencies()
    currencies = []
    for row in value_table:
        currencies.append(row[0])
    return Response(json.dumps(currencies), mimetype='application/json')

# currency details
@app.route('/currency/<c_name>')
def currency_dashboard(c_name):
    return render_template("c_dashboard.html", c_name=c_name)


# currency domains
@app.route('/currency/<c_name>/domains')
def currency_domains(c_name):
    domains = getDomains(c_name)
    return render_template("c_domains.html", domains=domains[0:10], c_name=c_name)

# currency list
@app.route('/list')
def listdisplay():
    return render_template("list.html")

# popular currencies
@app.route('/getpopular')
def popularCurrencies():
    popular = getCurrencyPopularity(count=10)
    currencies = [str(pair[0][0]).capitalize() for pair in popular]
    scores = [int(pair[1]) for pair in popular]
    pop_json = {'currencies': currencies, 'scores': scores}
    return json.dumps(pop_json)

# word cloud data
@app.route('/word_cloud')
def word_cloud():
    try:
        words_json = getCurrencyPopularity()
        words_json = [{'text': str(word[0][0]).capitalize(), 'weight': int(word[1]), 'link': '/currency/' + str(word[0][0]).lower()} for word in words_json]
        return json.dumps(words_json)
    except:
        return []


if __name__ == "__main__":
    app.run(debug=True)

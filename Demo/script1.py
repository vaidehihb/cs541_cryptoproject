from flask import Flask, request, render_template, Response
from dbConnect import getDomains
from similarity import readPopularity
import json
from wtforms import TextField, Form

# crypto flask app
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template("home.html")

# currency table
@app.route('/currencylist')
def currency_table():
    return render_template("currency_table.html")

# currency details
@app.route('/currency/<c_name>')
def currency_dashboard(c_name):
    params = {}
    params['rating'] = 7.5
    params['popularity'] = 90
    params['dominance'] = 40
    params['skewness'] = 60
    params['kurtosis'] = 70
    params['sd'] = 4
    params['pricedata'] = []
    params['trusted'] = True
    return render_template("c_dashboard.html", c_name=c_name, params = params)


# currency domains
@app.route('/currency/<c_name>/domains')
def currency_domains(c_name):
    domains = getDomains(c_name)
    return render_template("c_domains.html", domains=domains[0:10], c_name=c_name)


# word cloud data
@app.route('/word_cloud')
def word_cloud():
    try:
        popular = readPopularity()
        words_json = [{'text': str(word[0]).capitalize(), 'weight': int(word[1])} for word in popular]
        return json.dumps(words_json)
    except:
        return json.dumps({})


if __name__ == "__main__":
    app.run(debug=True)

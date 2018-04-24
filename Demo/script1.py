from flask import Flask, request, render_template, Response
from dbConnect import getDomains
from flask_bootstrap import Bootstrap
from similarity import readPopularity
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


# currency details
@app.route('/currency/<c_name>')
def currency_dashboard(c_name):
    return render_template("c_dashboard.html", c_name=c_name)


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

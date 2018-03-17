from flask import Flask, request, render_template
from dbConnect import getCurrencyNames

app = Flask(__name__)


@app.route('/')
@app.route('/<user>')
def home(user=None):
    return render_template("home.html", user=user)


@app.route('/httpmethods/<mname>', methods=['GET', 'POST'])
def httpmethods(mname):
    return render_template("httpmethods.html", mname=request.method)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/currency/<c_name>')
def currencyDashboard(c_name):
    return render_template("c_dashboard.html", c_name=c_name)


@app.route('/list')
def listdisplay():
    # currencies = ["Bitcoin","Ethereum","Ripple"]
    value_table = getCurrencyNames()
    currencies = []
    for row in value_table:
        currencies.append(row[0])
    return render_template("list.html", currencies=currencies)


@app.route('/templateparam/<name>')
def templateparam(name):
    return render_template("params.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)

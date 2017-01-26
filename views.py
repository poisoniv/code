from flask import Flask, render_template
from models import Product
from google.appengine.ext import ndb

app = Flask(__name__)


@app.route("/")
def index():
    # This is main page of the site
	qry = Product.query(Product.productname >= 'babe')

		
    return render_template("index.html",**locals())


@app.route("/product_query")
def product_query():
    # This will be the endpoint for querying GCP DataStore
    # This will take the results from the query and create the JSON needed for the text box
    return "some json payload"


if __name__ == "__main__":
    app.run()
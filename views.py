from flask import Flask, render_template
from models import product
from google.appengine.ext import ndb
import logging
import json

app = Flask(__name__)


@app.route("/")
def index():

	

	return render_template("index.html")


@app.route("/product_query")
def product_query():
    # This will be the endpoint for querying GCP DataStore
    # This will take the results from the query and create the JSON needed for the text box
	
	    # This is main page of the site
	qry = product.query(product.productname >= "babe")
	logging.info("products:")
	logging.info(qry)
	tommy="2peas"
	payload = []
	for prd in qry:
		this_el = {"label":"product name", "value":prd.productname}
		payload.append(this_el)
		
		logging.info(prd.productname)
		return json.dumps(payload)


if __name__ == "__main__":
    app.run(debug=True)
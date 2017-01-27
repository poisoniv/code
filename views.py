from flask import Flask, render_template, url_for, request
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
    search_term = request.args.get('s')
    qry = product.query(product.productname >= search_term)

    logging.info("products:")
    logging.info(qry)

    payload = []

    for prd in qry:
        payload.append(prd.productname)
        logging.info(prd.productname)
        data = {"title": prd.productname}
        payload.append(data)

    return json.dumps(payload)


if __name__ == "__main__":
    app.run(debug=True)
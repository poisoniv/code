import json

from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import literal
import pymysql


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@104.198.68.242/productcatalog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:Wiggle12@localhost/productcatalog?unix_socket=/cloudsql/gcp-ac:us-central1:autocomplete_db1'
db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/product_query")
def product_query():
    search_term = request.args.get('s')
    payload = []
    if search_term:
        qry = Product.query.filter(Product.name.contains(search_term)).limit(10).all()

        for prd in qry:
            data = {"title": prd.name}
            payload.append(data)

    return json.dumps(payload)


if __name__ == "__main__":
    app.run(debug=True)
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@/productcatalog?unix_socket=/cloudsql/gcp-ac:autocompelte-db"
db = SQLAlchemy(app)


class product(db.Model):
    productname = db.Column(db.String(255))
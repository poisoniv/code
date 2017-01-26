# models.py

from google.appengine.ext import ndb

class Product(ndb.Model):
    productname = ndb.StringProperty()
# models.py

from google.appengine.ext import ndb

class product(ndb.Model):
    productname = ndb.StringProperty()
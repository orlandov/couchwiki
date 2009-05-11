#!python

import datetime
from couchdb.schema import Document, TextField, DateTimeField

class Page(Document):
    body = TextField()
    name = TextField()
    type = TextField(default="page")
    created = DateTimeField(default=datetime.datetime.now())

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)

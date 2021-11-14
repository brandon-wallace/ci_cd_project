'''
application/main.py
'''
from flask import Flask

app = Flask(__name__)


@app.get('/')
def index():
    '''Landing page index route'''

    return 'Hello!'

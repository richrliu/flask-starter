from app import app
from flask import make_response, request

import requests
import json

@app.route('/')
@app.route('/index')
def index():
  return 'Hello, World!'

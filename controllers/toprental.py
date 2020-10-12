#\controllers\register.py
import config, re, json
from bottle import template, route, request, redirect
from models import registerdb

@route('/toprental')
def getTopRental():
  config.kargs['toprentals'] = json.dumps(registerdb.getTopRental())
  return template('toprental', data=config.kargs)
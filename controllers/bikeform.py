#\controllers\bikeform.py
import config
from bottle import template, route, request

@route("/bikeform")
def renderForm():
  return template('bikeform', data=config.kargs)

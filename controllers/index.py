#\controllers\index.py
from bottle import template

def render(**kargs):
  return template('index', data=kargs)
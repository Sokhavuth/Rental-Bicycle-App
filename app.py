#\app.py
import os, json, config
from bottle import route, run
from controllers import index, bikeform, customer, register
from public import setup
from models import bicycledb
  
@route('/')
def main():
  config.kargs['bicycles'] = json.dumps(bicycledb.select())
  return index.render(config.kargs)
  
if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)

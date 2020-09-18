#\app.py
import os, config
from bottle import route, run
from controllers import index, bikeform
from public import setup
  
@route('/')
def main():
  return index.render(**config.kargs)
  
if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)
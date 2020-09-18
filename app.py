#\app.py
import os
from bottle import route, run
from controllers import index
from public import setup
  
@route('/')
def main():
  kargs = {"site_title":"RENTAL BICYCLE APP", "message":"កម្មវិធី​គេហទំព័រ!"}
  return index.render(**kargs)
  
if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  run(host='localhost', port=9000, debug=True, reloader=True)
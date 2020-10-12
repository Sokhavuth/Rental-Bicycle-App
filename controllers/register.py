#\controllers\register.py
import config, re, json, datetime
from bottle import template, route, request, redirect
from models import customerdb, bicycledb, registerdb

@route('/register')
def displayRegister():
  config.kargs['registers'] = json.dumps(registerdb.select())
  return template('register', data=config.kargs)

@route('/registerForm')
def getRegisterForm():
  config.kargs['bicycles'] = json.dumps(bicycledb.select())
  config.kargs['customers'] = json.dumps(customerdb.select())
  return template('registerform', data=config.kargs)

@route('/register', method="POST")
def insertToRegister():
  brand = json.loads(request.forms.get("fbikelist"))
  customer = json.loads(request.forms.get("fcustomerlist"))
  bicycledb.amountMinus(brand[0])
  registerdb.insert(brand[0], customer[1], brand[1], (datetime.date.today()).strftime('%Y-%m-%d'), '1990-07-30')
  redirect('/register')

@route('/register/returndate/<id>/<bikeid>')
def editReturnDate(id, bikeid):
  registerdb.setReturnDate((datetime.date.today()).strftime('%Y-%m-%d'), id)
  bicycledb.amountPlus(bikeid)
  redirect('/register')

@route('/register/delete/<id>')
def deleteRegister(id):
  registerdb.delete(id)
  redirect('/register')

@route("/register/<key>/<index>")
def sortCustomer(key, index):
  config.kargs['registers'] = json.dumps(registerdb.sort(key))
  config.kargs['sortIndex'] = index
  return template('register', data=config.kargs)

@route("/search/register/<query>")
def searchCustomer(query):
  config.kargs['registers'] = json.dumps(registerdb.search(query))
  return template('register', data=config.kargs)
#\controllers\customer.py
import config, re, json
from bottle import template, route, request, redirect
from models import customerdb

@route('/customer')
def displayCustomer():
  config.kargs['customers'] = json.dumps(customerdb.select())
  return template('customer', data=config.kargs)

@route('/custform')
def getCustomerForm():
  return template('custform', data=config.kargs)

@route('/custform/edit/<id>')
def editCustomerForm(id):
  config.kargs['rowedit'] = customerdb.edit(id)
  config.kargs['id'] = id
  return template('custform', data=config.kargs)

@route("/customer/delete/<id>")
def deleteCustomer(id):
  config.kargs['id'] = id
  customerdb.delete(id)
  redirect('/customer')

@route("/customer/<key>/<index>")
def sortCustomer(key, index):
  config.kargs['customers'] = json.dumps(customerdb.sort(key))
  config.kargs['sortIndex'] = index
  return template('customer', data=config.kargs)

@route("/search/customer/<query>")
def searchCustomer(query):
  config.kargs['customers'] = json.dumps(customerdb.search(query))
  return template('customer', data=config.kargs)

@route('/customer', method="POST")
def getFormData():
  name = request.forms.get("fname")
  phone = request.forms.get("fphone")

  if not re.match(r"^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", phone):
    config.kargs['message'] = "You need to enter a right phone number."
    return template('custform', data=config.kargs)

  else:
    if 'rowedit' in config.kargs:
      customerdb.update(name, phone, config.kargs['id'])
      del config.kargs['rowedit']
      redirect('/customer')

    else:
      customerdb.insert(name, phone)
      redirect('/customer')
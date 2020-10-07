#\controllers\bikeform.py
import config, re, json
from bottle import template, route, request, redirect
from models import bicycledb

@route("/bikeform")
def renderForm():
  if 'rowedit' in config.kargs:
    del config.kargs['rowedit']

  return template('bikeform', data=config.kargs)

@route("/bikeform/edit/<id>")
def editForm(id):
  config.kargs['rowedit'] = bicycledb.edit(id)
  config.kargs['id'] = id
  return template('bikeform', data=config.kargs)

@route("/bikeform/delete/<id>")
def deleteForm(id):
  config.kargs['id'] = id
  bicycledb.delete(id)
  redirect('/')

@route("/bicycle/<brand>/<sortIndex>")
def sortBicycle(brand,sortIndex):
  config.kargs['bicycles'] = json.dumps(bicycledb.sort(brand))
  config.kargs['sortIndex'] = sortIndex
  return template('index', data=config.kargs)

@route("/search/bicycle/<query>")
def searchBicycle(query):
  config.kargs['bicycles'] = json.dumps(bicycledb.search(query))
  return template('index', data=config.kargs)

@route("/bikeform", method="POST")
def getFormData():
  brand = request.forms.get("fbrand")
  country = request.forms.get("fcountry")
  year = request.forms.get("fyear")
  amount = request.forms.get("famount")
  price = request.forms.get("fprice")

  if re.search("[0-9]", country):
    config.kargs['message'] = "Country name could contain only letter."
    return template('bikeform', data=config.kargs)

  elif not (re.match("^[0-9]+$", year) and re.match("^[0-9]+$", amount)):
    config.kargs['message'] = "Year and amount must be whole number."
    return template('bikeform', data=config.kargs)

  elif not (re.match(r"\A[-+]?\d*\.\d+|\d+\Z", price)):
    config.kargs['message'] = "Price must be a number."
    return template('bikeform', data=config.kargs)

  else:
    if 'rowedit' in config.kargs:
      bicycledb.update(brand, country, int(year), int(amount), float(price), config.kargs['id'])
      del config.kargs['rowedit']
      redirect('/')

    else:
      bicycledb.insert(brand, country, int(year), int(amount), float(price))
      return template('bikeform', data=config.kargs)
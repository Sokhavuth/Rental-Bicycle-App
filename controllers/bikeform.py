#\controllers\bikeform.py
import config, re
from bottle import template, route, request
from models import insertBicycle

@route("/bikeform")
def renderForm():
  return template('bikeform', data=config.kargs)

@route("/bikeform", method="POST")
def getFormData():
  brand = request.forms.get("fbrand")
  country = request.forms.get("fcountry")
  year = request.forms.get("fyear")
  amount = request.forms.get("famount")
  price = request.forms.get("fprice")

  if not re.findall("[a-zA-Z]", country):
    config.kargs['message'] = "Country name could contain only letter."
    return template('bikeform', data=config.kargs)

  elif not (re.findall("[0-9]", year) and re.findall("[0-9]", amount)):
    config.kargs['message'] = "Year and amount must be whole number."
    return template('bikeform', data=config.kargs)

  elif not (re.findall(r"[-+]?\d*\.\d+|\d+", price)):
    config.kargs['message'] = "Price must be a number."
    return template('bikeform', data=config.kargs)

  else:
    insertBicycle.insert(brand, country, int(year), int(amount), float(price))
    return template('bikeform', data=config.kargs)
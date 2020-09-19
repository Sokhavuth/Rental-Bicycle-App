//\public\js\main.js
class Bicycle{
  bicycleForm(formId){
    var brand = document.forms[formId]['fbrand'].value;
    var country = document.forms[formId]['fcountry'].value;
    var year = document.forms[formId]['fyear'].value;
    var amount = document.forms[formId]['famount'].value;
    var price = document.forms[formId]['fprice'].value;
    if((brand == "") || (country == "") || (year == "") || (amount == "") || (price == "")){
      return false;
    }else{
      var numberRGEX = /^(?:[1-9]\d*|0)?(?:\.\d+)?$/;
      var intRGEX = /^[0-9]+$/;
      var numberResult = numberRGEX.test(price);
      var intResult = (intRGEX.test(year) && intRGEX.test(amount));
      if(!numberResult){
        alert('Please enter a number for price.');
        return false;
      }
      if(!intResult){
        alert('Please enter a whole number for year and amount.');
        return false;
      }
    }
  }
}//end of class

var bicycle = new Bicycle();

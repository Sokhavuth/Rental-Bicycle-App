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

  showBicycle(bicycles){
    var html = '';
    
    if(bicycles.length > 0){
      html += "<table>";
      html += "<tr>";
      for(var k in {id:0, brand:0, country:0, year:0, amount:0, price:0}){
        html += "<th>" + k.toUpperCase() + "</th>";
      }
      html += "<th>OPTION</th>";
      html += "</tr>";

      for(var i=0; i<bicycles.length; i++){
        html += "<tr>";
        html +=  "<td>" + (i+1) + "</td>";
        for(var j in bicycles[i]){
          html += "<td>" + bicycles[i][j] + "</td>";
        }
        html += `<td class="option"><a onclick="alert(${i+1},'bikeform')" class="edit" id="'+i+'">Edit</a>|<a onclick="alert(${i+1})" class="delete" >Delete</a></td>`;
        html += "</tr>";
      }

      html += "</table>";
    }

    document.getElementById("table").innerHTML = html;
  }

}//end of class

var bicycle = new Bicycle();

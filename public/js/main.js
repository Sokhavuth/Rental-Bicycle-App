//\public\js\main.js
class Bicycle{

  setActiveMenu(){
    const pathName = window.location.pathname;
    $("#menu a").each(function(){
      if($(this).attr("href") === pathName)
        $(this).parent().addClass( "active" );
    });
  }

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

  showBicycle(bicycles,sortIndex){
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
          if(j > 0)
            html += "<td>" + bicycles[i][j] + "</td>";
        }
        html += `<td class="option"><a href="/bikeform/edit/${bicycles[i][0]}" class="edit">Edit</a>|<a href="/bikeform/delete/${bicycles[i][0]}" class="delete" >Delete</a></td>`;
        html += "</tr>";
      }

      html += "</table>";
    }

    document.getElementById("table").innerHTML = html;
    document.getElementById("bikekey").selectedIndex = sortIndex;
    
  }

  sortBicycle(){
    var element = document.getElementById("bikekey");
    var sortIndex = element.selectedIndex;
    var key = element.options[sortIndex].value;

    window.location.href = "/bicycle/" + key + "/" + sortIndex;
  
  }

  searchBicycle(){
    var query = $("#query").val();
    location.href= "/search/bicycle/" + query;
  }

  customerForm(formId){
    var name = document.forms[formId]['fname'].value;
    var phone = document.forms[formId]['fphone'].value;
  
    if((name == "") || (phone == "")){
      alert("Please fill this form with your name and phone number!");
      return false;
    }else{
      var phoneRegex = /^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;
      var numberResult = phoneRegex.test(phone);
      if(!numberResult){
        alert("Please fill this form with the right phone number.");
        return false;
      }
    }
  }

  showCustomer(customers, sortIndex){
    var html = '';
    
    if(customers.length > 0){
      html += "<table>";
      html += "<tr>";
      for(var k in {id:0, name:0, phone:0}){
        html += "<th>" + k.toUpperCase() + "</th>";
      }
      html += "<th>OPTION</th>";
      html += "</tr>";

      for(var i=0; i<customers.length; i++){
        html += "<tr>";
        html +=  "<td>" + (i+1) + "</td>";
        for(var j in customers[i]){
          if(j > 0)
            html += "<td>" + customers[i][j] + "</td>";
        }
        html += `<td class="option"><a href="/custform/edit/${customers[i][0]}" class="edit">Edit</a>|<a href="/customer/delete/${customers[i][0]}" class="delete" >Delete</a></td>`;
        html += "</tr>";
      }

      html += "</table>";
    }

    document.getElementById("table").innerHTML = html;
    document.getElementById("custkey").selectedIndex = sortIndex;
  }

  sortCustomer(){
    var element = document.getElementById("custkey");
    var sortIndex = element.selectedIndex;
    var key = element.options[sortIndex].value;

    window.location.href = "/customer/" + key + "/" + sortIndex;
  }

  searchCustomer(){
    var query = $("#query").val();
    location.href= "/search/customer/" + query;
  }

}//end of class

var bicycle = new Bicycle();

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

  registerForm(bicycles, customers){
    for(var i=0; i<bicycles.length; i++){
      var brand = bicycles[i][1];
      var amount = bicycles[i][4];
      if(amount > 0)
        $('#bikelist').append(`<option value='[${bicycles[i][0]}, "${brand}"]'>${brand}</option>`);
    }

    for(var i=0; i<customers.length; i++){
      var name = customers[i][1];
      $('#customerlist').append(`<option value='[${customers[i][0]}, "${name}"]'>${name}</option>`);
    }
  }

  showRegister(registers, sortIndex){
    registers = JSON.parse(registers);
    sortIndex = JSON.parse(sortIndex);

    var html = '';
    
    if(registers.length > 0){
      html += "<table>";
      html += "<tr>";
      for(var k in {id:1, customer:1, bicycle:1, 'Rental Date':1, 'Return Date':1}){
        html += "<th>" + k.toUpperCase() + "</th>";
      }
      html += "<th>OPTION</th>";
      html += "</tr>";

      for(var i=0; i<registers.length; i++){
        html += "<tr>";
        html +=  "<td>" + (i+1) + "</td>";
        for(var j in registers[i]){
          if(j > 1){
            if(j == 5){
              if(registers[i][j] == "1990-07-30")
                html += `<td class='return-date'><a href='/register/returndate/${registers[i][0]}/${registers[i][1]}'><img src='/static/images/return.png' /></a></td>`;
              else
                html += "<td class='return-date'>" + registers[i][j] + "</td>";
              
            }else{
              html += "<td>" + registers[i][j] + "</td>";
            }
          }
        }
        html += `<td class="option"><a href="/register/delete/${registers[i][0]}" class="delete" >Delete</a></td>`;
        html += "</tr>";
      }

      html += "</table>";
    }

    document.getElementById("table").innerHTML = html;
    document.getElementById("regiskey").selectedIndex = sortIndex;
  }

  sortRegister(){
    var element = document.getElementById("regiskey");
    var sortIndex = element.selectedIndex;
    var key = element.options[sortIndex].value;

    window.location.href = "/register/" + key + "/" + sortIndex;
  }

  searchRegister(){
    var query = $("#query").val();
    location.href= "/search/register/" + query;
  }

}//end of class

var bicycle = new Bicycle();

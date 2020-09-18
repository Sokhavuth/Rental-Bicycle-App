from bottle import route

@route('/json')
def request_json():
  return '''
    <script>
    var xhttp = new XMLHttpRequest();
 
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var ms = JSON.parse(this.responseText);
        alert(ms.message);
      }
    };
 
    xhttp.open("GET", "/response", true);
    xhttp.send();
    </script>
    '''

@route('/response')
def return_json():
  return {'message':"json data"}
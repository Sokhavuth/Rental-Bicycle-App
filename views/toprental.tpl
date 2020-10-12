<!--\views\register.tpl-->

%include("./partials/header.tpl")

<div class="main" id="main">
  <div class="content" id="content">
    <div class="top-widget">
    <span>TOP RENTAL</span>
    </div>
    
    <div id="table-customer"></div>
    <div id="table-bicycle"></div>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/main.js"></script>
    <script>
      $(document).ready(function() {
        bicycle.showTopRental({{!data['toprentals']}});
      });
    
    </script>
    
  </div><!--content-->

</div><!--main-->

%include("./partials/footer")
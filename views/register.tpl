<!--\views\register.tpl-->

%include("./partials/header.tpl")

<div class="main" id="main">
  <div class="content" id="content">
    <div class="top-widget">
    <span>REGISTERS</span><input onclick="location.href='/registerForm'" type="button" value="Add Register" />
    </div>
    <div class="bottom-widget">
      <span>
        <select id="regiskey">
          <option value="Customer" >Customer</option>
          <option value="Brand" >Bicycle</option>
          <option value="RentDate" >Rental Date</option>
          <option value="ReturnDate" >Return Date</option>
        </select>
        <input onclick="bicycle.sortRegister()" type="button" value="Sort" />
      </span>
      <span class="search">
        <input id="query" type="text" /><input onclick="bicycle.searchRegister()" type="button" value="Search" />
      </span>
    </div>
    <div id="table"></div>
    
    <script>bicycle.showRegister({{!data['registers']}}, {{!data['sortIndex']}})</script>
    
  </div><!--content-->

</div><!--main-->

%include("./partials/footer")
<!--\views\bikeform.tpl-->

%include("./partials/header.tpl")

<style>

</style>

<div class="main" id="main">
  <div class="content" id="content">
    <div class="top-widget">
    <span>CUSTOMERS</span><input onclick="location.href='/custform'" type="button" value="Add Customer" />
    </div>
    <div class="bottom-widget">
      <span>
        <select id="custkey">
          <option value="Name" >Name</option>
          <option value="Phone" >Phone</option>
        </select>
        <input onclick="bicycle.sortCustomer()" type="button" value="Sort" />
      </span>
      <span class="search">
        <input id="query" type="text" /><input onclick="bicycle.searchCustomer()" type="button" value="Search" />
      </span>
    </div><!--bottom-widget-->
    <div id="table"></div>
    <script>bicycle.showCustomer({{!data['customers']}}, {{!data['sortIndex']}})</script>
  </div><!--content-->

</div><!--main-->

%include("./partials/footer")
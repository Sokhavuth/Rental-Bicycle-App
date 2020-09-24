<!--\views\index.tpl-->

%include("./partials/header.tpl")

<style>

</style>

<div class="main" id="main">
  <div class="content" id="content">
    <div class="top-widget">
    <span>BICYCLES</span><input onclick="location.href='/bikeform'" type="button" value="Add Bicycle" />
    </div>
    <div class="bottom-widget">
      <span>
        <select id="bikekey">
          <option value="Brand" >Brand</option>
          <option value="Country" >Country</option>
          <option value="Year" >Year</option>
          <option value="Amount" >Amount</option>
          <option value="Price" >Price</option>
        </select>
        <input onclick="bicycle.sortBicycle()" type="button" value="Sort" />
      </span>
      <span class="search">
        <input type="text" /><input type="button" value="Search" />
      </span>
    </div><!--bottom-widget-->
    <div id="table"></div>
    <script>bicycle.showBicycle({{!data['bicycles']}})</script>
  </div><!--content-->

  %include("./partials/sidebar.tpl")

</div><!--main-->

%include("./partials/footer")
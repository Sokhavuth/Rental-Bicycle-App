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
        <select>
          <option value="Brand" >Brand</option>
        </select>
        <input type="button" value="Sort" />
      </span>
      <span class="search">
        <input type="text" /><input type="button" value="Search" />
      </span>
    </div><!--bottom-widget-->
  </div><!--content-->

  %include("./partials/sidebar.tpl")

</div><!--main-->

%include("./partials/footer")
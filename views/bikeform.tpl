<!--\views\bikeform.tpl-->

%include("./partials/header.tpl")

<style>
#bikeform{
  margin-top: 30px;
  width: 30%;
  display: grid;
  grid-template-columns: auto calc(85% - 5px);
  grid-gap: 5px;
}
#bikeform a{
  text-align: right;
}
</style>

<div class="main" id="main">
  <div class="content" id="content">
    <span>BICYCLE ENTRY FORM</span>
    <form id="bikeform" method="POST" action="/bikeform" onsubmit="return Bicycle.bicycleForm('bikeform')">
      <a>Brand:</a><input name="fbrand" type="text" />
      <a>Country:</a><input name="fcountry" type="text" />
      <a>Year:</a><input name="fyear" type="text" />
      <a>Amount:</a><input name="famount" type="text" />
      <a>Price:</a><input name="fprice" type="text" />
      <a></a><input type="submit" />
    </form>
  </div><!--content-->

</div><!--main-->

%include("./partials/footer")
<!--\views\registerform.tpl-->

%include("./partials/header.tpl")

<style>
#registform{
  margin-top: 30px;
  width: 30%;
  display: grid;
  grid-template-columns: auto calc(85% - 5px);
  grid-gap: 5px;
}
#registform a{
  text-align: right;
}
</style>

<div class="main" id="main">
  <div class="content" id="content">
    <span>REGISTER ENTRY FORM</span>
    
    <form id="registform" method="POST" action="/register" onsubmit="return bicycle.registerForm()">
      <a>Bicycles: </a><select name="fbikelist" id="bikelist"></select>
      <a>Customers: </a><select name="fcustomerlist" id="customerlist"></select>
      <a></a><input type="submit" />
    </form>
    <script>bicycle.registerForm({{!data['bicycles']}}, {{!data['customers']}})</script>
  </div><!--content-->

</div><!--main-->

%include("./partials/footer")
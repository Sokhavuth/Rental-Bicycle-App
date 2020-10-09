<!--\views\bikeform.tpl-->

%include("./partials/header.tpl")

<style>
#custform{
  margin-top: 30px;
  width: 30%;
  display: grid;
  grid-template-columns: auto calc(85% - 5px);
  grid-gap: 5px;
}
#custform a{
  text-align: right;
}
</style>

<div class="main" id="main">
  <div class="content" id="content">
    <span>CUSTOMER ENTRY FORM</span>
    
    <form id="custform" method="POST" action="/customer" onsubmit="return bicycle.customerForm('custform')">
      %if 'rowedit' in data:
      <a>Name:</a><input name="fname" value="{{data['rowedit'][1]}}" type="text" required />
      <a>Phone:</a><input name="fphone" value="{{data['rowedit'][2]}}" type="text" required />
      %else:
      <a>Name:</a><input name="fname" type="text" required />
      <a>Phone:</a><input name="fphone" type="text" required />
      %end
      <a></a><input type="submit" />
    </form>
    
    <p>{{data['message']}}</p>
    %data['message'] = ""
  </div><!--content-->

</div><!--main-->

%include("./partials/footer")
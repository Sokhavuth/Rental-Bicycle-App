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
    %if 'rowedit' in data:
    <form id="bikeform" method="POST" action="/bikeform" onsubmit="return bicycle.bicycleForm('bikeform')">
      <a>Brand:</a><input name="fbrand" value="{{data['rowedit'][0]}}" type="text" required />
      <a>Country:</a><input name="fcountry" value="{{data['rowedit'][1]}}" type="text" required />
      <a>Year:</a><input name="fyear" value="{{data['rowedit'][2]}}" type="text" required />
      <a>Amount:</a><input name="famount" value="{{data['rowedit'][3]}}" type="text" required />
      <a>Price:</a><input name="fprice" value="{{data['rowedit'][4]}}" type="text" required />
      <a></a><input type="submit" />
    </form>
    %else:
    <form id="bikeform" method="POST" action="/bikeform" onsubmit="return bicycle.bicycleForm('bikeform')">
      <a>Brand:</a><input name="fbrand" type="text" required />
      <a>Country:</a><input name="fcountry" type="text" required />
      <a>Year:</a><input name="fyear" type="text" required />
      <a>Amount:</a><input name="famount" type="text" required />
      <a>Price:</a><input name="fprice" type="text" required />
      <a></a><input type="submit" />
    </form>
    %end
    <p>{{data['message']}}</p>
    %data['message'] = ""
  </div><!--content-->

</div><!--main-->

%include("./partials/footer")
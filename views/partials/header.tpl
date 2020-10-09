<!--\views\partials\header.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['site_title']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/main.js"></script>
    <link href="/static/styles/main.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
    
  <body>
    <div class="site" id="site">
      <header class="site-header" id="site-header">
        {{data['site_title']}}
      </header>

      <nav>
        <ul class="menu" id="menu">
          <li><a href="/">Bicycle</a></li>
          <li><a href="/customer">Customer</a></li>
          <li><a>Register</a></li>
          <li><a>Top Rental</a></li>
        </ul>
      </nav>
      <script>bicycle.setActiveMenu()</script>
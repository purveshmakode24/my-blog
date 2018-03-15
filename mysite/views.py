from django.http import HttpResponse 
from django.shortcuts import  render
import datetime

def hello(request):
	html  = """ 
      <!DOCTYPE html>
<html lang="en">
<head>
  <title>Ashish Nimbalkar</title> 
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  body {
      font: 20px Montserrat, sans-serif;
      line-height: 1.8;
      color: #f5f6f7;
  }
  p {font-size: 16px;}
  .margin {margin-bottom: 45px;}
  .margin1 {margin-left: 17px ;}
  .bg-1 { 
      background-color: #1abc9c; /* Green */
      color: #ffffff;
  }
  .bg-2 { 
      background-color: #474e5d; /* Dark Blue */
      color: #ffffff;
  }
  .bg-3 { 
      background-color: #ffffff; /* White */
      color: #555555;
  }
  .bg-4 { 
      background-color: #2f2f2f; /* Black Gray */
      color: #fff;
  }
  .container-fluid {
      padding-top: 70px;
      padding-bottom: 70px;
  }
  .navbar {
      padding-top: 15px;
      padding-bottom: 15px;
      border: 0;
      border-radius: 0;
      margin-bottom: 0;
      font-size: 12px;
      letter-spacing: 5px;
  }
  .navbar-nav  li a:hover {
      color: #1abc9c !important;
  }
  </style>
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-default">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#">Me</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">WHO</a></li>
        <li><a href="#">WHAT</a></li>
        <li><a href="#">WHERE</a></li>
      </ul>
    </div>
  </div>
</nav>

<!-- First Container -->
<div class="container-fluid bg-1 text-center">
  <h3 class="margin">ASHISH NIMBALKAR</h3>
  <h3 class = "margin">I'm a Programmer</h3>
  <div> 
   <a href="https://github.com/ashunimbz" class="btn btn-info btn-lg" role="button">Github</a>
    <a href="https://www.linkedin.com/in/ashish-nimbalkar-602371152/" class="btn btn-info btn-lg margin1" role="button">LinkedIn</a>
    <a href="https://www.quora.com/profile/Ashish-Nimbalkar-1" class="btn btn-info btn-lg margin1" role="button">Quora</a>
  <a href="https://www.facebook.com/ashish.nimbalkar.528" class="btn  btn-info btn-lg margin1" role="button">Facebook</a>
  </div>
</div>

 <div class =  "bg-1" >
 <h2 >SKILLS</h2>
 <div class="list-group ">
    <a href="#" class="list-group-item list-group-item-success">C++</a>
    <a href="#" class="list-group-item list-group-item-info">Django</a>
    <a href="#" class="list-group-item list-group-item-success">Java </a>
    <a href="#" class="list-group-item list-group-item-danger">Python</a>
  </div>
  </div>



<!-- Footer -->
<footer class="container-fluid bg-4 text-center">
  <h2>ABOUT ME </h2>
  <div>
  
  <p  font-size = "20" >I am currently studying Information technology at GECA.I like to solve puzzles .I do competative programming in my free time . I am a big fan of Yuvaraj Singh ( Cricketer ) .I also closely follow football especially La-liga .Real madrid is my favorite team .I like to watch sci-fi hollywood movies. My favorite singer is Ed-sheeran ,while favorite band is Imagine Dragons.</p>
  
  </div> 
</footer>

</body>
</html>"""
	return HttpResponse(html) 

def time(request):
	now =  datetime.datetime.now() 
	html  =  "<html><body>  It is now %s</html></body>"%now
	return HttpResponse(now)

def addtime(request ,  offset):
	t  =   int(offset)
	dt  =  datetime.datetime.now() + datetime.timedelta(hours = t)
	html  = "<html><body> After %s it would be %s </html></body>"% (t ,  dt)
	return HttpResponse(html)

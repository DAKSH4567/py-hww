<!DOCTYPE html>
<html>
<head>
<title>Website Part 1</title>
<style>
body{
margin:0;
font-family:Arial,Helvetica,sans-serif;
background:#f9fbff;
}
nav{
background:#ff7a59;
padding:15px;
display:flex;
justify-content:space-between;
align-items:center;
color:white;
}
nav ul{
list-style:none;
display:flex;
margin:0;
padding:0;
}
nav ul li{
margin-left:20px;
}
nav ul li a{
color:white;
text-decoration:none;
font-weight:bold;
}
.hero{
padding:60px 20px;
text-align:center;
background:#ffe3dc;
}
.hero h1{
margin-bottom:10px;
}
.hero p{
color:#555;
}
.features{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
padding:40px;
}
.box{
background:white;
padding:25px;
border-radius:10px;
box-shadow:0 4px 12px rgba(0,0,0,0.1);
text-align:center;
}
</style>
</head>
<body>
<nav>
<h2>My Website</h2>
<ul>
<li><a href="#">Home</a></li>
<li><a href="#">About</a></li>
<li><a href="#">Contact</a></li>
</ul>
</nav>
<div class="hero">
<h1>Welcome to My Website</h1>
<p>This is the first part of the website</p>
</div>
<div class="features">
<div class="box">Simple Design</div>
<div class="box">Fast Loading</div>
<div class="box">Responsive Layout</div>
</div>
</body>
</html>

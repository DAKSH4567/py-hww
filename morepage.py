<!DOCTYPE html>
<html>
<head>
<title>Content Display</title>
<style>
body{
margin:0;
font-family:Arial,Helvetica,sans-serif;
background:#f2f6ff;
}
header{
background:#4a90e2;
color:white;
padding:20px;
text-align:center;
}
.section{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:20px;
padding:30px;
}
.card{
background:white;
padding:20px;
border-radius:10px;
box-shadow:0 4px 10px rgba(0,0,0,0.1);
text-align:center;
}
.card h3{
margin:10px 0;
color:#333;
}
.card p{
color:#666;
font-size:14px;
}
</style>
</head>
<body>
<header>
<h1>Content Display</h1>
<p>Explore our website sections</p>
</header>
<div class="section">
<div class="card">
<h3>Gallery</h3>
<p>View images and designs</p>
</div>
<div class="card">
<h3>Courses</h3>
<p>Learn new skills easily</p>
</div>
<div class="card">
<h3>About Us</h3>
<p>Know more about our team</p>
</div>
<div class="card">
<h3>Contact</h3>
<p>Get in touch with us</p>
</div>
</div>
</body>
</html>

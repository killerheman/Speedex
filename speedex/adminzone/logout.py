#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
	<meta charset="utf-8">
	<title>Loading Screen</title>
	<link rel="stylesheet" type="text/css" href="admincss/logout.css">
	<script>
 function logout()
 {
    window.history.forward();
	window.setTimeout("window.location.href='../login.py'",2000);
 }
</script>
</head>
<body onload="logout()">
	<div class="box">
		<div class="b b1"></div>
		<div class="b b2"></div>
		<div class="b b3"></div>
		<div class="b b4"></div>
	</div>

</body>
</html>
"""
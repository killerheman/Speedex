#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<link href="css/style.css" rel="stylesheet" type="text/css">
<script src="js/java.js" type="text/javascript"></script>
</head>
<body onload="slide()">
<div id="outer">
<!--header div start-->
<div id="header">
    <div id="logo"> <img src="images/logo.png" height="150px" width="150px" style="border-radius:25px 12px 12px 12px;"></div>
    <div id="pt"><span style="font-size:80; color:white;margin-left:50px;text-shadow: 1px 1px 2px black, 0 0 25px #f56600, 0 0 5px darkblue;font-family:forte;">SpeedEx Courier </span>
	</div>
</div>
<!--header div end here-->
<!--Menu div starts here-->
<div id="menu">
    <ul>
     <li><a href="index.py">HOME</a></li>
	 <li><a href="aboutus.py">ABOUT US</a></li>
	 <li><a href="contactus.py">CONTACT US</a></li>
	 <li><a href="complain.py">COMPLAIN</a></li>
	 <li><a href="tracking.py">TRACKING</a></li>
	 <li><a href="register.py">REGISTER</a></li>
	 <li><a href="login.py">LOGIN</a></li>
    </ul>
</div>
<!--Main div ends here-->

<!--Main div starts here-->
<div id="main" style="height:250px;">
     
<p style="font-size:25px;font-weight:bold;color:#f56600;margin-top:15px;padding-top:20px;">&nbsp;&nbsp;&nbsp;&nbsp;TRACK YOUR ORDER NOW !</p>
      <hr noshade />
	  <br/>
	  <br/>
	  <form action="track.py" method="post">
	  <table border="0" style="margin:0px auto;width:60%;">
	  <tr>
	  <td><input type="text" name="refno" style="width:90%;height:100%;"/></td>
	  <td><input type="submit" Value="TRACK" style="background-color:#f56600;width:100%;height:40px"/> </td>
	  </tr>
	  </table>
	  </form>	  
</div>
<!--Main div ends here-->
<!--Footer div starts here-->
<div id="footer">
     <div id="lfooter">
	     <b style="margin-left:50px;font-family:Harlow Solid;color:white;font-size:30px;">Address</b><hr style="width:300px;" />
	     <p style="margin-left:50px;font-family:times new roman;color:white;font-size:17px;">16,Cannaught Road,Alankar Cinema <br/>Compound
         Agarkar Nagar,Pune<br/>Maharastra 411001<br/> 020 2748 7571<br/><a href="#">http://speedexindia.com</a></p>
	 </div>
     <div id="mfooter">
	      <b style="margin-left:70px;font-family:Harlow Solid;color:white;font-size:30px;">Follow us on</b><hr style="width:300px;"/><br/>&nbsp;&nbsp;&nbsp;&nbsp;
		<a href="#"><img src="images/facebook.png" height="40px" width="40px"/></a>&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="#"><img src="images/instagram.png" height="40px" width="40px"/></a>&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="#"><img src="images/google.png" height="40px" width="40px"/></a>&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="#"><img src="images/youtube.png" height="40px" width="40px"/></a>
	&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="#"><img src="images/linkedin.png" height="40px" width="40px"/></a>
	&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="#"><img src="images/skype.png" height="40px" width="40px"/></a>
	 </div>
	 <div id="rfooter" style="margin-top:0px;">
	       <b style="margin-left:50px;font-family:Harlow Solid;color:white;font-size:30px;">Design and developed by:</b><hr style="width:300px;" />
		   <p style="margin-left:50px;font-family:Arial black;color:white;font-size:20px;">Himanshu Sharma</p><br/><br/>
		   <p style="color:white;margin-left:50px;font-size:18px;">&copy;Copyright SpeedexPost</p>
		   
	 </div>
</div>
<!--Footer div ends here-->
</div>
</body>
</html>
"""
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
     <li style="margin-left:-15px;"><a href="Speedex.html">HOME</a></li>
	 <li><a href="aboutus.py">ABOUT US</a></li>
	 <li><a href="contactus.py">CONTACT US</a></li>
	 <li><a href="complain.py">COMPLAIN</a></li>
	 <li><a href="tracking.py">TRACKING</a></li>
	 <li><a href="register.py">REGISTER</a></li>
	 <li><a href="login.py">LOGIN</a></li>
    </ul>
</div>
<!--Main div ends here-->
<!--slider start-->
      <div id="slider"><img height="350px" width="1200px"/> 
      </div>
<!--slider end-->
<!--Main div starts here-->
<div id="main">
      <div id="lmain">
      <b style="font-size:23px;font-weight:bold;color:#f56600"><p>&nbsp;&nbsp;&nbsp;&nbsp;ABOUT COURIER TRACKING SYSTEM</b></p>
      <hr style="width:750px;" noshade />
	      <div class="mainc">
		       <b style="font-size:17px;">Manage Couriers</b>
			   <div class="mainpic">
			   <img src="images/pic1.jpeg" height="150px" width="320px">
			   </div>
			   <p style="padding-left:5px;text-align:justify;">Ability to define Special Event days(days where employees cannot request time-off,are warned or notified on the calender)</p>
		   </div>
		  <div class="mainc">
		        <b style="font-size:17px;">Manage Trackings</b>
			   <div class="mainpic">
			   <img src="images/pic2.jpg" height="150px" width="320px">
			   </div>
			   <p style="padding-left:5px;text-align:justify;">Group your user by offices.Ability to display balance in hours or in days</p>		  
		  </div>
		  <div class="mainc">
		        <b style="font-size:17px;">Manage Customers</b>
			   <div class="mainpic">
			   <img src="images/pic3.jpg" height="150px" width="320px">
			   </div>
			   <p style="padding-left:5px;">3 levels (Administrations,Managers,Employees each with thier own different permission.Single Sign-On,LDAP,Active Directory support .</p>
		  </div>
		  <div class="mainc">
               <b style="font-size:17px;">Manage Login</b>
			   <div class="mainpic">
			   <img src="images/pic4.jpg" height="150px" width="320px">
			   </div>
			   <p style="padding-left:5px;text-align:justify;">Ability to upload your company logo to personalize the interface.Ability to set time-off,pending request and holiday reminders.</p>
		  </div>
      </div>
	  <div id="rmain">
	        <b style="font-size:23px;font-weight:bold;color:#f56600"><p>&nbsp;&nbsp;&nbsp;&nbsp;FEATURES</b></p>
            <hr style="width:360px;" noshade />  
	        <div class="mainf1"style="background: url('images/f1.jpeg');background-size:cover;" >
			     <div class="inner" style="color:white;text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;font-size:22px;font-weight:bold;text-align:center;">QUICK, RELIABLE DELIVERY  </div>
			</div>
			<div class="mainf2" style="background: url('images/f2.jpg');background-size:cover;">
			<div class="inner" style="color:white;text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;font-size:23px;font-weight:bold;text-align:center;"> A STRONG TRACK RECORD </div>
			</div>
	  </div>
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
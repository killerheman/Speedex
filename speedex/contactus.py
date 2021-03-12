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
<!--slider start-->
      
<!--slider end-->
<!--Main div starts here-->
<div id="main">
      <div id="lmain">
      <b style="font-size:23px;font-weight:bold;color:#f56600"><p>&nbsp;&nbsp;&nbsp;&nbsp;CONTACT US</b></p>
      <hr style="width:750px;" noshade />
	  <form action="contactuscode.py" method="post">
     <table style="margin-left:30px;width:80%;color:#0d47a1;height:80%;font-size:20px;font-weight:bolder;" >
	    <tr>
		    <td>Enter name:</td>
			<td><input type="text" name="name" required /></td>
		</tr>
		<tr>
		    <td>Enter Mobile No.:</td>
			<td><input type="number" name="mobileno" required /></td>
		</tr>
		<tr>
		    <td>Enter Email Id:</td>
			<td><input type="email" name="email" required /></td>
		</tr>
		<tr>
		    <td>Address:</td>
			<td><textarea name="address" required></textarea></td>
		</tr>
		<tr>
		    <td>Enter Purpose:</td>
			<td><textarea name="purpose" required></textarea></td>
		</tr>
		<tr>
		     <td colspan="2" align="center"><input type="submit" value="SUBMIT" style="margin-left:70px;"/>
				
		     <input type="reset" value="RESET" style="background-color:#00C851;"/>
			 </td>
		</tr>
	 </table>
	 </form>	  
       </div>
	  <div id="rmain">
	        <b style="font-size:23px;font-weight:bold;color:#f56600"><p>&nbsp;&nbsp;&nbsp;&nbsp;WHERE TO FIND US</b></p>
            <hr style="width:360px;" noshade />  
	        <div class="mainf1" style="border:none;">
			<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3720.0341605949748!2d72.86200631493536!3d21.190801885910812!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be04fbabb69d8df%3A0x6031fc8f3ffaf79!2sSPEEDEXPOST+COURIER+SERVICES!5e0!3m2!1sen!2sin!4v1564866843795!5m2!1sen!2sin" width="350px" height="250px" frameborder="0" style="border:1px" allowfullscreen></iframe>
			</div>
			<div class="mainf2">
			<p style="font-size:25px;font-weight:bold;margin-left:20px;color:#f56600;">Get in touch</p>
			<p style="font-size:18px;margin-left:20px;color:#0d47a1;">16,Cannaught Road<br/>Alankar Cinema Compound<br/>Agarkar Nagar<br/>Pune,Maharastra (411001)<br/><br/>
			+020 27487571<br/>www.speedexindia.com</p>
			
			
			
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
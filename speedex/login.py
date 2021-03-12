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
<div id="main" style="background:url('images/bg1.jpg');background-size:cover;">
      <div id="lmain" style="background-color:rgba(0,0,0,0.4);border-radius:50px 0px 50px 0px;height:300px;width:600px;margin-left:280px;margin-top:150px;">
	  <div id="circle">
	  <img src="images/user.png" height="60px" width="60px" style="margin-left:20px;margin-top:14px;"/>
	  </div>
      
	  <br/>
	  <form action="logincode.py" method="post">
<table style="margin:0px auto;width:85%; height:200px;font-size:20px;font-weight:bolder;color:white;">
<tr>
<td>Admin Login Id</td>
<td><input type="text" name="aid" required/></td>
</tr>
<tr>
<td>Enter Password</td>
<td><input type="password" name="password" required /></td>

</tr>
<tr>
     <td colspan="2" align="center"><input type="submit" value="LOGIN" style="margin-left:0px;"/>
	 </td>
</tr>
</table>
</form>
	  
	  
	 <!--Form ends here-->
	  
	      
       </div>
	  
</div>
<!--Main div ends here-->
<!--Footer div starts here-->
<div id="footer">
     <div id="lfooter" style="width:600px;height:50px;">
	     <p style="color:white;margin-left:50px;font-size:18px;">&copy;Copyright SpeedexPost</p>
	 </div>
     
	 <div id="rfooter" style="width:600px;height:50px;margin-top:0px;">
	       <p style="margin-left:150px;font-family:verdana;color:white;font-size:18px;">Design and developed by : Himanshu Sharma</p>
		   	   
		   
	 </div>
</div>
<!--Footer div ends here-->
</div>
</body>
</html>
"""
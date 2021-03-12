#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<link href="admincss/adminhome.css" rel="stylesheet" type="text/css">
<script src="js/java.js" type="text/javascript"></script>
</head>
<body>
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
     <li style="margin-left:-20px;"><a href="adminhome.py">HOME</a></li>
	 <li><a href="complains.py">COMPLAINS</a></li>
	 <li><a href="contactmgmt.py">CONTACT MGMT</a></li>
	 <li><a href="consignment.py">CONSIGNMENT</a></li>
	 <li><a href="addcity.py">ADD CITY</a></li>
	 <li><a href="changepwd.py">CHANGE PWD</a></li>
	 <li><a href="logout.py">LOGOUT</a></li>
    </ul>
</div>


<!--Main div starts here-->
<div id="main" style="padding-top:5;margin-top:15px;">
    <p style="font-size:30px;text-align:center;font-family:lucida handwriting;font-weight:bold;color:#f56600;">Change Your Password Here !</p>
<hr/>
<form action="pass.py" method="post">
<table style="color:#0d47a1;font-size:20px;font-weight:bold;width:60%;height:300px;" border="0" align="center">
 <tr>
   <td>Enter Old Password:</td>
   <td><input type="password" name="oldpass" required /></td>
 </tr>
 <tr>
   <td>Enter New Password:</td>
   <td><input type="password" name="newpass" required /></td>
 </tr>
 <tr>
   <td>Enter Confirm Password:</td>
   <td><input type="password" name="cpass" required /></td>
 </tr>
 <tr>
    <td colspan="2" align="center">
	<input type="Submit" value="UPDATE"/>
	</td>
 </tr>
 </form>
</table>
 <br/>  
<br/>
</div>
<!--Main div ends here-->
<!--Footer div starts here-->
<div id="footer">
     <div id="lfooter">
	     <p style="color:white;margin-left:50px;font-size:18px;">&copy;Copyright SpeedexPost</p>
	 </div>
     
	 <div id="rfooter">
	       <p style="margin-left:150px;font-family:verdana;color:white;font-size:18px;">Design and developed by : Himanshu Sharma</p>
		   	   
		   
	 </div>
</div>
<!--Footer div ends here-->
</div>
</body>
</html>
"""
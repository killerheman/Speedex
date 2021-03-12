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
<!--Main div ends here-->
<!--slider start-->
      
<!--slider end-->
<!--Main div starts here-->
<div id="main" style="margin-top:20px;" >
      <br/>
      <form action="addcitycode.py" method="post">
   <table style="color:#0d47a1;font-size:25px;font-weight:bold;width:60%;height:100px;" border="0" align="center">
       <tr>
	   <td>Enter City :</td>
	   <td align="center"><input type="text" name="cityname"/></td>
	   <td><input type="submit" value="ADD CITY"/></td>
	   </tr>
</table>
</form>
<br/>

<table style="margin:0px auto;width:60%;font-family:verdana;text-align:center;font-size:17px;" border="7">
  <tr style="border:none;background-color:#ff7043;"> 
    <th>S No.</th>
    <th>City name</th>
    <th>Delete</th>
  </tr>
  
  
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from city"
cur.execute(q)
res=cur.fetchall()
n=1
for r in res:
 print "<tr>"
 print "<td style='background-color:#ff7043;'>",n,"</td>"
 print "<td>",r[1],"</td>"
 print "<td><a href='deletecode.py?id="+str(r[0])+"'>Delete</a></td>"
 print "</tr>"
 n=n+1
	      
print"""
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
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
     <table style="width:80%;">
	 <tr>
	 <td><p style="font-size:20px;"><a href="consignment.py">Consignment Management</a> </p><td>
	 <td><p style="font-size:35px;text-align:center;font-family:lucida handwriting;font-weight:bold;color:#f56600;">View Consignment</p></td>
	 </tr>
	 </table>
   <hr/>
   <br/>
      <table border="5" style="font-size:16px;"> 
      <tr style="border:none;background-color:#ff7043;">
	     <th>Ref No.</th>
		 <th>Sender Name</th>
		 <th>Sender Address</th>
		 <th>Sender Contact</th>
		 <th>Reciever Name</th>
		 <th>Reciever Address</th>
		 <th>Reciever Contact</th>
		 <th>Source</th>
		 <th>Current City</th>
		 <th>Destination</th>
		 <th>Status</th>
		 <th>Post Date</th>
		 <th>Update</th>
		 <th>Delete</th>
      </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from consignment"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td style='background-color:#ff7043;'>",r[0],"</td>"
 print "<td>",r[1],"</td>"
 print "<td>",r[2],"</td>"
 print "<td>",r[3],"</td>"
 print "<td>",r[4],"</td>"
 print "<td>",r[5],"</td>"
 print "<td>",r[6],"</td>"
 print "<td>",r[7],"</td>"
 print "<td>",r[8],"</td>"
 print "<td>",r[9],"</td>"
 print "<td>",r[10],"</td>"
 print "<td>",r[11],"</td>"
 print "<td><a href='updatestatus.py?id="+str(r[0])+"'>Update</a></td>"
 print "<td><a href='deletestatus.py?id="+str(r[0])+"'>Delete</a></td>"
 print "</tr>"

   
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
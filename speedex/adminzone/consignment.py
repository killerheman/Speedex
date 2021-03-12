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
	 <td><p style="font-size:20px;"><a href="showconsignment.py">View Consignment</a> </p><td>
	 <td><p style="font-size:35px;text-align:center;font-family:lucida handwriting;font-weight:bold;color:#f56600;">Consignment Management</p></td>
	 </tr>
	 </table>
   <hr/>
   <form action="concode.py" method="post">
   <table style="color:#0d47a1;font-size:20px;font-weight:bold;width:60%;height:450px;" border="0" align="center">
   <tr>
      <td>Reference No. </td>
	  <td><input type="number" name="refno" required /></td>
   </tr>
   <tr>
      <td>Sender Name : </td>
	  <td><input type="text" name="sname" required /></td>
   </tr>
   <tr>
      <td>Sender Address:</td>
	  <td><textarea name="saddress" required></textarea></td>
   </tr>
   <tr>
      <td>Sender Contact No. :</td>
	  <td><input type="number" name="scontact" required /></td>
   </tr>
   <tr>
      <td>Reciever Name :</td>
	  <td><input type="text" name="rname" required /></td>
   </tr>
   <tr>
      <td>Reciever Address :</td>
	  <td><textarea name="raddress" required></textarea></td>
   </tr>
   <tr>
      <td>Reciever Contact No. :</td>
	  <td><input type="number" name="rcontact" required /></td>
   </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from city"
cur.execute(q)
res1=cur.fetchall()
cur.execute(q)
res2=cur.fetchall()
cur.execute(q)
res3=cur.fetchall() 
print "<tr>"
print "<td>Select Source Location :</td>"
print "<td><select name='source'>"  
print "<option>Select Source Location</option>"
for r in res1:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"

print "<tr>"
print "<td>Select Current Location :</td>"
print "<td><select name='curcity'>"  
print "<option>Select Current Location</option>"
for r in res2:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"
 
print "<tr>"
print "<td>Select Destination Location :</td>"
print "<td><select name='destination'>"  
print "<option>Select Destination Location</option>"
for r in res3:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"

   
print""" 
<tr>
  <td>Status :</td>
  <td><select name="status" required>
      <option value="">Select Status</option>
      <option>Initiated</option>
	  <option>Pipeline</option>
	  <option>Delivered</option>
	  <option>Cancelled</option>
   </select>
  </td>
</tr>
<tr>
     <td colspan="2" align="center"><input type="submit" value="SUBMIT" style="margin-left:130px;"/>
		
     <input type="reset" value="RESET" style="background-color:#00C851;"/>
 </td>
</tr>
</table>
</form>
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
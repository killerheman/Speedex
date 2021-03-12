#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
mobileno=f.getvalue('mobileno')
email=f.getvalue('email')
address=f.getvalue('address')
purpose=f.getvalue('purpose')
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
query="insert into contactus(name,mobileno,email,address,purpose,curdate) values('"+name+"','"+mobileno+"','"+email+"','"+address+"','"+purpose+"',sysdate())"
n=cur.execute(query)
if n==1:
 print "<script>alert('Success');window.location.href='index.py';</script>"
else:
 print"<script>alert('Unsuccess');window.location.href='contactus.py'</script>"
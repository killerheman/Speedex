#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
cityname=cgi.FieldStorage().getvalue('cityname')
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
query="insert into city(cityname) values('"+cityname+"')"
n=cur.execute(query)
if n==1:
 print"<script>alert('Added City');window.location.href='addcity.py';</script>"
else:
 print"<script>alert('Not Added');window.location.href='addcity.py'</script>"
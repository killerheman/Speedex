#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
id=f.getvalue('id')
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="delete from contactus where id='"+id+"'"
n=cur.execute(q)
if n==1:
 print "<script>alert('Record Deleted');window.location.href='contactmgmt.py'</script>"
else:
 print "<script>alert('Record not deleted');window.location.href='contactmgmt.py';</script>"
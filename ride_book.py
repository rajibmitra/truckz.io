#!C:\Python34\python.exe
import cgi
import cx_Oracle

print('Content-type: application/json\r\n\r\n')
con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
data=cgi.FieldStorage()
owner_name=data.getvalue('owner_name')
customer_name=data.getvalue('customer_name')
source=data.getvalue('source')
destination=data.getvalue('destination')
sts=-1
cid=0
did=0

sql="SELECT CUSTOMER_ID FROM CUSTOMER WHERE NAME = '%s'" % (customer_name)
cur.execute(sql)
for r in cur:
        cid=r[0]
sql="SELECT OWNER_ID FROM OWNER WHERE NAME = '%s'" % (owner_name)
cur.execute(sql)
for r in cur:
        did=r[0]
if sts==-1:
    sql="UPDATE OWNER SET STATUS = 'REQUESTED' WHERE OWNER_ID = %s" % (did)
    cur.execute(sql)
    cur.execute('commit')
    sql="UPDATE CUSTOMER SET STATUS = 'REQUESTED' WHERE CUSTOMER_ID = %s" % (cid)
    cur.execute(sql)
    cur.execute('commit')
    sql="INSERT INTO RIDE(OWNER_ID, CUSTOMER_ID, SOURC, DESTN) VALUES(%s, %s, '%s', '%s')" % (did, cid, source, destination)
    cur.execute(sql)
    cur.execute('commit')
    sts=1

print("[\"", sts, "\"]")

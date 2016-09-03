#!C:\Python34\python.exe
import cgi
import cx_Oracle
import json

#print('Content-type: text/html\r\n\r\n')
print('Content-type: application/json\r\n\r\n')

con=cx_Oracle.connect('cbs/apss@localhost/xe')
# print(con, ' ', con.version)

cur=con.cursor()
data=cgi.FieldStorage()
sts=-1
truck_id=-1
reg_no=data.getvalue('reg_no')
typ=data.getvalue('type')
name=data.getvalue('name')
cost_per_km=data.getvalue('cost_per_km')
max_weight=data.getvalue('max_weight')
volumn=data.getvalue('volumn')

#print('<h1> Truck Details: ', reg_no, typ, name, cost_per_km, '</h1>')
sql="INSERT INTO TRUCK(REG_NO, TYPE, NAME, COST_PER_KM, MAX_WEIGHT, VOLUMN) VALUES('%s', '%s', '%s', '%s','%s','%s')" % (reg_no, typ, name, cost_per_km, max_weight, volumn)
#print('<h1>', sql, '</h1>')
cur.execute(sql)
cur.execute('commit')
#print('<h3> Truck Registered</h3>')

sql="SELECT TRUCK_ID FROM TRUCK WHERE REG_NO = '%s'" % (reg_no)
#print(sql)
cur.execute(sql)
for r in cur:
    truck_id=r[0]
    sts=1
print("[\"", sts, "\",\"", truck_id, "\"]")

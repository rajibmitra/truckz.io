#!C:\Python34\python.exe
import cx_Oracle

con=cx_Oracle.connect('cbs/apss@localhost/xe')

cur=con.cursor()
sts=-1
did=0

if sts==-1:
        sql="SELECT ID FROM SESSIONS WHERE TYPE = 'DID'"
        cur.execute(sql)
        for r in cur:
            did=r[0]

        sql="UPDATE OWNER SET STATUS = 'OFFLINE' WHERE OWNER_ID = %s" % (did)
        cur.execute(sql)
        cur.execute("commit")

        sql="DELETE FROM SESSIONS WHERE TYPE = 'DID' AND ID = %s" % (did)
        cur.execute(sql)
        cur.execute("commit")

        print("location: ../owner.html\r\n\r\n")
else:
        print("location: ../owner_homepage.html\r\n\r\n")

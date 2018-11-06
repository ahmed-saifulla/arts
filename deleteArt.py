#!C:\Users\HP\AppData\Local\Programs\Python\Python37-32\python

print("Content-Type: text/HTML")
print("")

import cgi

s_form = cgi.FieldStorage()

s_artid= s_form.getvalue("artid")

import mysql.connector

o_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="artroom"
)


o_mycursor = o_mydb.cursor()

s_sql = "DELETE FROM art WHERE id= %s"
t_val = (s_artid,)

o_mycursor.execute(s_sql, t_val)


o_mydb.commit()

print(o_mycursor.rowcount, "record deleted.")

o_mycursor.close()

s_redirectURL = "http://localhost/arts/gallery.py"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(s_redirectURL)+'" />') 
print('  </head>')
print('</html>')


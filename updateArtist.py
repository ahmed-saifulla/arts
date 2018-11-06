#!C:\Users\HP\AppData\Local\Programs\Python\Python37-32\python

print("Content-Type: text/HTML")
print("")

import cgi

s_form = cgi.FieldStorage()

s_aid= s_form.getvalue("aid")
s_artistname= s_form.getvalue("artistName")
s_specialisation= s_form.getvalue("specialisation")
s_place= s_form.getvalue("place")
s_contact= s_form.getvalue("contact")


import mysql.connector

o_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="artroom"
)


o_mycursor = o_mydb.cursor()

s_sql = "UPDATE artist SET a_name = %s, spec = %s, place= %s, contact = %s WHERE id = %s"
t_val = (s_artistname,s_specialisation,s_place,s_contact,s_aid)

o_mycursor.execute(s_sql, t_val)


o_mydb.commit()

print(o_mycursor.rowcount, "record updated.")

o_mycursor.close()

s_redirectURL = "http://localhost/arts/index.html"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(s_redirectURL)+'" />') 
print('  </head>')
print('</html>')


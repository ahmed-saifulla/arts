#!C:\Users\HP\AppData\Local\Programs\Python\Python37-32\python

print("Content-Type: text/HTML")
print("")

import cgi,os
import cgitb
cgitb.enable()

import os,sys
try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass

s_form = cgi.FieldStorage()

s_title= s_form.getvalue("title")
s_aid= s_form.getvalue("aid")
s_cid= s_form.getvalue("cid")
s_cost= s_form.getvalue("cost")
s_descr= s_form.getvalue("descr")
s_fileitem = s_form['fileUp']



import mysql.connector

o_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="artroom"
)


o_mycursor = o_mydb.cursor()

s_sql = "INSERT INTO art (name, a_id, c_id, cost, descr) VALUES (%s, %s,%s ,%s ,%s )"
t_val = (s_title , s_aid ,s_cid ,s_cost, s_descr)

o_mycursor.execute(s_sql, t_val)



o_mycursor2 = o_mydb.cursor()

o_mycursor2.execute("SELECT * from art")
a_rows = o_mycursor2.fetchall()

s_fileitem.filename = str(a_rows[len(a_rows) - 1][0])+".png"
print (s_fileitem.filename)


o_mydb.commit()

print(o_mycursor.rowcount, "record inserted.")

o_mycursor.close()



print ("----")
print ("filename",s_fileitem.filename)
print ("file",s_fileitem.file)
print ("----")



#test wether upload success

if s_fileitem.filename:

    s_fn = os.path.basename(s_fileitem.filename)
    open('C:/xampp/htdocs/arts/uploads/' + s_fn,'wb').write(s_fileitem.file.read(1500000))
    s_message = 'The file"' + s_fn + '" was uploaded successfully'
else:
    s_message = 'No file uploaded'


s_redirectURL = "http://localhost/arts/gallery.py"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(s_redirectURL)+'" />') 
print('  </head>')
print('</html>')


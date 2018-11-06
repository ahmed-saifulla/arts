#!C:\Users\HP\AppData\Local\Programs\Python\Python37-32\python

print("Content-Type: text/HTML")
print("")

import cgi

s_form = cgi.FieldStorage()

s_name= s_form.getvalue("a_name")
s_special= s_form.getvalue("special")
s_place= s_form.getvalue("place")
s_contact= s_form.getvalue("contact")
s_password= s_form.getvalue("pwd")


import mysql.connector

o_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="artroom"
)


o_mycursor = o_mydb.cursor()

s_sql = "INSERT INTO artist (a_name, spec, place, contact, password) VALUES (%s, %s,%s ,%s ,%s )"
t_val = (s_name , s_special ,s_place ,s_contact, s_password)

o_mycursor.execute(s_sql, t_val)



o_mydb.commit()




o_mycursor.execute("SELECT * FROM artist ")



a_rows = o_mycursor.fetchall()

a_rows.reverse()





print("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Home | Arts </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" type="text/css" media="screen" href="sass/style.css" />
    <script src="js/jquery.min.js"></script>

    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="css/bootstrap4.min.css">
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap4.min.js"></script>

    <!-- Custom Library for Carosel 1 -->
    <link rel="stylesheet" href="css/carosel1.css">
    <script src="js/carosel1.js"></script>

    <!-- Bootbox -->
    <script src="js/bootbox.min.js"></script>

    <script> alert('Signed Up Successfully,  Your Artist ID is :""",a_rows[0][0],""" '); 
             window.location = 'http://localhost/arts/index.html'; </script>

    <style> #aid{ display:none; }</style>
  

    
</head>
<body>
        <!-- Navbar START-->
        <nav class="navbar navbar-expand-md bg-dark navbar-dark">
            <!-- Brand -->
            <a class="navbar-brand" href="#">ARTS</a>
            
            <!-- Toggler/collapsibe Button -->
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <!-- Navbar links -->
            <div class="collapse navbar-collapse" id="collapsibleNavbar">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="gallery.py">Gallery</a>
                    </li>
                    <!-- <li class="nav-item">
                        <a class="nav-link" href="rules.html">Rules</a>
                    </li> -->
                    <li class="nav-item">
                        <a class="nav-link" href="#" data-target="#myModal" data-toggle="modal" >Login</a>
                    </li> 
                </ul>
            </div> 
        </nav>

        <div class="modal fade" id="myModal" role="dialog">
            <div class="modal-dialog">
        
              <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Artist Login</h4>
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                  
                </div>
                <div class="modal-body">
                  <form action="adminPanel.py" method="POST">
                      Artist ID<input type="text" name="aid" required class="form-control"><br>
                      Password<input type="password" name="pwd" required  class="form-control">
                  
                </div>
                <div class="modal-footer">
                  <input type="submit" class="btn btn-success" id="login-btn" value="Login">
                </form>
                  <script>
                    $('#login-btn').click(function(){
                        
                    });
                  </script>

                </div>
              </div>
              
            </div>
          </div>
        <!-- Navbar E N D -->
        
        <!-- ------------------------------------------------------------------------------------ -->
        
        <!-- Main Banner START-->
        <section id="gallery-bg">
        
            
        </section>
        <!-- Main Banner E N D -->

        <!-- ------------------------------------------------------------------------------------ -->
        
        
        <!-- ------------------------------------------------------------------------------------ -->

        <footer>
            <p>A Shabaka Product . 2018 </p>
        </footer>

        
</body>
</html>""")

cur.close()
con.close()

######



# s_redirectURL = "http://localhost/arts/gallery.py"
# print('<html>')
# print('  <head>')
# print('    <meta http-equiv="refresh" content="0;url='+str(s_redirectURL)+'" />') 
# print('  </head>')
# print('</html>')


#!C:\Users\HP\AppData\Local\Programs\Python\Python37-32\python

print("Content-Type: text/HTML")
print("")

import cgi
import mysql.connector

o_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="artroom"
)

o_mycursor = o_mydb.cursor()


o_mycursor.execute("SELECT * FROM art AS A INNER JOIN artist AS B ON A.a_id = B.id ")



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
                    <li class="nav-item">
                        <a class="nav-link" href="#" data-target="#myModalSignUp" data-toggle="modal" >Sign Up</a>
                    </li>
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

          <div class="modal fade" id="myModalSignUp" role="dialog">
            <div class="modal-dialog">
        
              <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title"> Artist Sign Up</h4>
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                  
                </div>
                <div class="modal-body">
                  <form action="signup.py" method="POST">
                      Name<input type="text" name="a_name" required class="form-control"><br>
                      Specialist In<input type="text" name="special" required class="form-control"><br>
                      Place<input type="text" name="place" required class="form-control"><br>
                      Contact No<input type="text" name="contact" required class="form-control" pattern="[0-9]{10}" ><br>
                      Password<input type="password" name="pwd" required  class="form-control">
                  
                </div>
                <div class="modal-footer">
                  <input type="submit" class="btn btn-success" id="login-btn" value="Login">
                </form>
                  

                </div>
              </div>
              
            </div>
          </div>
        <!-- Navbar E N D -->
        
        <!-- ------------------------------------------------------------------------------------ -->
        
        <!-- Main Banner START-->
        <section id="gallery-bg">
        <div class="row">
            """)
            
            
def s_artid():
    for s_row in a_rows:
        print (" <div style='float:left; margin:0px; padding:80px; ' class='col-md-3'><img src=\"uploads/"+ str(s_row[0])+".png\" width='200px' height='200px'> <h4> "+ str(s_row[1])+" </h4> <h5>Artist : "+ str(s_row[7])+" </h5>  <h5>Cost : "+ str(s_row[4])+" </h5></div> ")

print(""" """,s_artid(),"""
            
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


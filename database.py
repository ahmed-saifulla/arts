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

o_mycursor.execute("SELECT * FROM art")

a_rows = o_mycursor.fetchall()

a_rows.reverse()

# # mydb.commit()




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
                    <!-- <li class="nav-item">
                        <a class="nav-link" href="candidates.html">Candidates</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="rules.html">Rules</a>
                    </li> -->
                    <li class="nav-item">
                        <a class="nav-link" href="#" data-target="#myModal" data-toggle="modal" >Logout</a>
                    </li> 
                </ul>
            </div> 
        </nav>

        <div class="modal fade" id="myModal" role="dialog">
            <div class="modal-dialog">
        
              <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Are You sure?</h4>
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                  
                </div>
              
                <div class="modal-footer">
                  <input type="submit" class="btn btn-danger" id="logout-btn" value="Yes, Logout">
                </form>
                  <script>
                    $('#logout-btn').click(function(){
                        window.location.replace("http://localhost/arts/index.html");
                    });
                  </script>

                </div>
              </div>
              
            </div>
          </div>
        <!-- Navbar E N D -->
        
        <!-- ------------------------------------------------------------------------------------ -->
        
        <!-- Main Banner START-->
        <section id="main-bg">
        <div class="row">
            """)
            
            
def s_artid():
    for s_row in a_rows:
        print (" <div style='float:left; margin:0px; padding:80px; ' class='col-md-3'><img src=\"uploads/"+ str(s_row[0])+".png\" width='200px' height='200px'></div> ")

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

# <div class="col-md-2">

#             </div>

#             <div class="col-md-8">
#                 <table>
#                     <thead>
#                         <tr>
#                             <th> Art id<th>
#                             <th> Name <th>
#                             <th> Artist <th>
#                             <th> Category <th>
#                             <th> Cost <th>
#                             <th> Descr <th> 
#                         </tr>
#                     </thead>
#                     <tbody>
#                         <tr>
#                             <td> ID <td>
#                             <td> Name <td>
#                             <td> Artist <td>
#                             <td> Category <td>
#                             <td> Cost <td>
#                             <td> Descr <td> 
#                         </tr>
#                     </tbody>
#                 </table>

#             </div>

#             <div class="col-md-2">

#             </div>



cur.close()
con.close()


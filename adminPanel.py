#!C:\Users\HP\AppData\Local\Programs\Python\Python37-32\python
    

print("Content-Type: text/HTML")
print("")

import cgi

s_form = cgi.FieldStorage()

s_aid = s_form.getvalue("aid")
s_pwd = s_form.getvalue("pwd")


import mysql.connector

o_mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="artroom"
)

o_mycursor = o_mydb.cursor()

s_sql = "SELECT * FROM artist WHERE id = %s AND password = %s"
t_val = (s_aid , s_pwd)

o_mycursor.execute(s_sql, t_val)

o_mycursor.fetchall()
o_mydb.commit()

if (o_mycursor.rowcount > 0):
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
        <section id="gallery-bg">
        <div class="row">
            <div class="col-md-2">

            </div>

            <div class="col-md-3">
                <br> <h3> New Uploads </h3>
                <form class="form" action="fileUp.py" method="POST" enctype="multipart/form-data">
                    
                    <br><label for="title">Title:</label>
                    <input type="text" class="form-control" id="title" placeholder="Enter Art Title" name="title">
                    
                    <br><label for="cid">Category:</label>
                    <select name="cid" class="form-control" id="cid">
                        <option value="1"> 1 - Oil Paint </option>
                        <option value="2"> 2 - Acrylic Paint </option>
                        <option value="2"> 3 - Watercolor Paint </option>
                        <option value="2"> 4 - Gouache paint </option>
                        <option value="2"> 5 - Ink paintings </option>
                    </select>

                    <br><label for="cost">Cost:</label>
                    <input type="text" class="form-control" id="cost" placeholder="Cost" name="cost" pattern="[0-9]{1,}" title="Price in Rupees">
                    
                    <br><label for="descr">Description:</label>
                    <input type="text" class="form-control" id="descr" placeholder="Description" name="descr">

                    
                    <input type="text" class="form-control" id="aid"   value=""",s_aid,""" name="aid">
                    
                    <br><label for="fileUp">File:</label>
                    <input type="file" class="form-control" id="fileUp"  name="fileUp">
                    
                    
                    <br><button type="submit" class="btn btn-primary">Upload</button>
                </form>
                
            </div>

            <div class="col-md-2">
                <br> <h3> Delete </h3>
                <form class="form" action="deleteArt.py" method="POST">
                    
                    <br><label for="artid">Title:</label>
                    <input type="text" class="form-control" id="artid" placeholder="Enter Art ID" name="artid">
                    
                    <br><button type="submit" class="btn btn-primary">Delete</button>
                </form>
                
            </div>

            <div class="col-md-3">
                 <br> <h3> Update </h3>
                <form class="form" action="updateArtist.py" method="POST">
                    
                    
                    <input type="text" class="form-control" id="aid"   value=""",s_aid,""" name="aid">
                    

                    <br><label for="artistName">Artist Name:</label>
                    <input type="text" class="form-control" id="artistName" placeholder="Enter Artist Name" name="artistName">
                    
                    <br><label for="special">Specialisation:</label>
                    <input type="text" class="form-control" id="specialisation" placeholder="Specialisation" name="specialisation">
                    
                    <br><label for="place">Place:</label>
                    <input type="text" class="form-control" id="place" placeholder="Place" name="place">
                    
                    <br><label for="special">Contact:</label>
                    <input type="text" class="form-control" id="contact" placeholder="Contact" name="contact">
                    

                    <br><button type="submit" class="btn btn-primary">Update</button>
                </form>
               
            </div>

            <div class="col-md-2">

            </div>
        </section>
        <!-- Main Banner E N D -->

        <!-- ------------------------------------------------------------------------------------ -->
        
        
        <!-- ------------------------------------------------------------------------------------ -->

        <footer>
            <p>A Shabaka Product . 2018 </p>
        </footer>

        
</body>
</html>""")

else:
    s_redirectURL = "http://localhost/arts/index.html"
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url='+str(s_redirectURL)+'" />') 
    print('  </head>')
    print('</html>')

cur.close()
con.close()
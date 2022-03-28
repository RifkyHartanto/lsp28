<?php 

require 'process.php';

if(isset($_POST["register"])){
    if(tambahUser($_POST) > 0){
        echo "
        <script type='text/javascript'>
            alert('Register berhasil, silahkan login!')
            window.location = '../login/index.php'
        </script>
        ";
    }else{
        echo "
        <script type='text/javascript'>
            alert('Mohon maaf, pendaftaran gagal')
            window.location = 'index.php'
        </script>
        ";
    }
}



?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="container">
        <span><img src="lgo.png" class="lgo" width="40px"><h2><b>Noxepedia</b></h2></span>
        <h3>Create your account here!</h3>
        <form action="" method="POST">
        <input type="text" name="name" placeholder="Your Name" class="form-control" id=""> <br /><br />

        <input type="text" name="username" placeholder="Username"class="form-control" id=""> <br /><br />

        <input type="password" name="password" placeholder="Password"class="form-control" id=""> <br /><br />

        <input type="hidden" name="roles" class="form-control" id="" value="Customer"><br /> <br />  
        
        <button type="submit" name="register">Register</button>
        <div class="login">
            <small>Sudah mempunyai akun? <br />
            <a href="../login/index.php">Login</a></small>
        </div>
    </form>
</div>
</body>
</html>
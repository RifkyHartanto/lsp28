<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <span><img src="lgo.png" class="lgo" width="40px"><h2><b>Noxepedia</b></h2></span>
        <h3>Log In your account</h3>
        <form action="process.php" method="POST">
        <input type="text" name="username" placeholder="Username" class="form-control" id=""> <br /><br />

        <input type="password" name="password" placeholder="Password" class="form-control" id=""> <br /><br />
        
        <button type="submit" name="login">Login</button>

        <div class="register">
            <small>Belum punya akun? <br />
            <a href="../register/index.php">Daftar Disini</a></small>
        </div>
        </form>
    </div>
</body>
</html>
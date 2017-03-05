<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Página de Login</title>
    <link type="image/png" rel="shortcut icon" href="img/favicon.png"/>
    <link type="text/css" rel="stylesheet" href="http://fonts.googleapis.com/css?family=Open+Sans:400,700">
    <link type="text/css" rel="stylesheet" href="css/style.css">
    <link type="text/css" rel="stylesheet" href="css/font-awesome.min.css">
  </head>

  <body>
      <div id="login">
          %if message:
            <p><font color="red">{{message}}</font></p>
          %end
        <form action="/login" method="POST">
          <span class="fontawesome-user"></span>
          <input type="text" name="email" placeholder="Email">
          <i class="fa fa-lock" aria-hidden="true"></i>
          <input type="password" name="password" placeholder="Senha">
          <input type="submit" class="submit" name ="login" value="Login">
        </form>
      </div>
  </body>
</html>

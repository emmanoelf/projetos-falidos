<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Cadastro de usuário</title>
    <link rel="shortcut icon" type="image/png" href="img/favicon.png"/>
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Open+Sans:400,700">
    <link rel="stylesheet" href="css/style.css">
  </head>

  <body>
    <nav>
      <ul>
        <li><img src="img/logo.png" id="logo" alt="melhor logo que você vai ver na vida" /></li>
        <li class="dropdown">
          <a href="javascript:void(0)" class="dropbtn">Cadastro</a>
          <div class="dropdown-content">
            <a href="/user_registration">Usuários</a>
            <a href="/project_registration">Projetos falidos</a>
          </div>
        <li><a href="/all_users">Listagem</a></li>
      </ul>
    </nav>
      <div id="cadastro">
          %if message:
            <p><font color="green">{{message}}</font></p>
          %end
        <form action="/user_registration" method="POST" name='form-cadastro'>
          <label>Nome: </label>
          <input type="text" name="name" placeholder="Insira seu nome">
          <label>Email: </label>
          <input type="text" name="email" placeholder="Insira seu email">
          <label>Usuário:</label>
          <input type="text" name="user_name" placeholder="Insira o usuário desejado">
          <label>Senha: </label>
          <input type="password" name="password" placeholder="Escolha sua senha">
          <input type="submit" name="register" class="submit" value="Cadastrar">
          <input type="reset" class="reset" value="Limpar">
        </form>
  </body>
</html>

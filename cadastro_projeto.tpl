<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Cadastro de projeto falido</title>
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
        <li><a href="/all_projects">Listagem</a></li>
      </ul>
    </nav>
      <div id="cadastro">
          %if message:
            <p><font color="green">{{message}}</font></p>
          %end
        <form action="/project_registration" method="POST" name='form-cadastro'>
          <label>Nome do projeto: </label>
          <input name="project_name" type="text" id="nome-projeto" placeholder="Insira o nome do projeto falido">
          <label>Quem deu a idéia? </label>
          <select name="guilty">
            <option value="campa">Campa</option>
            <option value="emmanoel">Emmanoel</option>
            <option value="muttley">Muttley</option>
          </select>
          <br>
          <label>Ainda há esperança?</label>
          <select name="hope">
            <option value="sim">Sim</option>
            <option value="nao">Não</option>
          </select>
          <br>
          <input name="register" type="submit" class="submit" value="Cadastrar">
          <input type="reset" class="reset" value="Limpar">
        </form>
  </body>
</html>

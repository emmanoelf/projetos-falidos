<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Culpado da existência do projeto</title>
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
                    <a href="cadastro-usuario.html">Usuários</a>
                    <a href="cadastro-projeto.html">Projetos falidos</a>
                  </div>
                <li><a href="#">Listagem</a></li>
            </ul>
        </nav>
        <div class="table-responsive espacamento-top">
            <table align="center">
                <th>
                    <td>Nome</td>
                    <td>Culpado</td>
                    <td>Existe esperança?</td>
                </th>
                %for row in rows:
                    <tr>
                        %for data in row:
                            <td>{{data}}</td>
                        %end
                    </tr>
                %end
            </table>
        </div>
	</body>
</html>
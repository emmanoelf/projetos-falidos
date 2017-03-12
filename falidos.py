"""Module that defines our server"""
import argparse
import hashlib
from bottle import *
from db_abstraction import Worker


def verify_login():
    """Function that verifys if the user
    didn't authenticate checking the cookie logged
    and redirecting to authentication_failure
    after that"""
    if request.get_cookie('logged') is None:
        redirect('/authentication_failure')


@route('/css/<filename>')
def stylesheets(filename):
    """Route to map the static files from
    /css folder"""
    return static_file(filename, root='./css')


@route('/fonts/<filename>')
def fonts(filename):
    """Route to map the static files from
    /fonts folder"""
    return static_file(filename, root='./fonts')


@route('/img/<filename>')
def imgs(filename):
    """Route to map the static files from
    /img folder"""
    return static_file(filename, root='./img')


@route('/')
def home_page():
    """Route to shows the home_page template"""
    return template('home_page.tpl')


@route('/authentication_failure')
def authentication_failure():
    """Route to shows the aviso_auth template"""
    return template('aviso_auth.tpl')


@route('/login', method=['GET', 'POST'])
def index():
    """Function that maps the login route,
    verify the credencials inserted by the user
    and allow the acess to the hole system giving
    the logged cookie or deny it"""
    if request.params.get('login', ''):
        email = request.params.get('email', '')
        password = hashlib.sha256()
        password.update(request.params.get('password', '').encode())
        result = Worker('falidos.db',
                        'SELECT password FROM user WHERE email = ?',
                        (email,)).query()

        if result[0][0] == password.hexdigest():
            response.set_cookie('logged', 'true',
                                path='/', max_age=300)
            redirect('/project_registration')
        else:
            return template('index.tpl',
                            message="Usuário ou senha incorretos")
    else:
        return template('index.tpl', message=None)


@route('/project_registration', method=['GET', 'POST'])
def project_registration():
    """Function that maps the project_registration
    route and insert new projects to the database"""
    verify_login()

    if request.params.get('register', ''):
        project_name = request.params.get('project_name')
        guilty = request.params.get('guilty')
        hope = request.params.get('hope')

        Worker('falidos.db',
               'INSERT INTO project (name, guilty, hope) VALUES (?,?,?)',
               (project_name.encode(), guilty, hope)).insert()

        return template('cadastro_projeto.tpl',
                        message='''O projeto {}
                         foi cadastrado com sucesso!'''.format(project_name))
    else:
        return template('cadastro_projeto.tpl', message=None)


@route('/user_registration', method=['GET', 'POST'])
def user_registration():
    """Function that maps the user_registration
    route and insert new users to the database"""
    verify_login()

    if request.params.get('register', ''):
        name = request.params.get('name')
        email = request.params.get('email')
        user_name = request.params.get('user_name')
        password = hashlib.sha256()
        password.update(request.params.get('password', '').encode())

        Worker('falidos.db',
               '''INSERT INTO user (name, email, user, password)
               VALUES (?,?,?,?)''',
               (name, email, user_name, password.hexdigest())).insert()

        return template('cadastro_usuario.tpl',
                        message='''O usuário {}
                         foi cadastrado com sucesso!'''.format(user_name))
    else:
        return template('cadastro_usuario.tpl', message=None)


@route('/all_projects', method=['GET', 'POST'])
def all_projects():
    """Function that maps the all_projects
    route and returns all the projects
    from the database"""
    verify_login()

    result = Worker('falidos.db', 'SELECT * FROM project').query()

    return template('todos_projetos.tpl', rows=result)


@route('/all_users', method=['GET', 'POST'])
def all_users():
    """Function that maps the all_users
    route and returns all the users
    from the database"""
    verify_login()

    result = Worker('falidos.db',
                    'SELECT name, email, user FROM user').query()

    return template('todos_usuarios.tpl', rows=result)


@route('/create_db')
def create_db():
    """Function that maps
    create_db route and create the db"""
    import sqlite3
    con = sqlite3.connect('falidos.db')
    con.execute('''CREATE TABLE user (id INTEGER PRIMARY KEY,
                name char(40) NOT NULL,
                email char(30) NOT NULL,
                user char(10) NOT NULL,
                password char(32) NOT NULL)''')

    con.execute('''CREATE TABLE project (id INTEGER PRIMARY KEY,
                name char(40) NOT NULL,
                guilty char(10) NOT NULL,
                hope boolean NOT NULL)''')

    con.execute('''INSERT INTO user (name, email, user, password)
                VALUES ('admin', 'admin@admin', 'admin',
                '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4')''')
    con.commit()


@error(404)
def error_404():
    """Function that maps all
    the 404 errors and returns to
    the user error_404 template"""
    return template('erro_404.tpl')

if __name__ == '__main__':

    PARAMETERS = {
        "host": "localhost",
        "port": 8080,
        "debug": True,
        "reloader": True,
    }

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--host",
                        help="The host where the app is goinna run.")
    PARSER.add_argument("--port", type=int,
                        help="The port where the app is gonna run.")
    PARSER.add_argument("--debug", type=bool,
                        help="Option debug True or False")
    PARSER.add_argument("--reloader", type=bool,
                        help='''Property that enables the aplication
                        to restart when this file is changed''')

    ARGS = vars(PARSER.parse_args())

    for argument in ARGS.keys():
        if ARGS[argument]:
            PARAMETERS[argument] = ARGS[argument]

    run(host=PARAMETERS["host"], port=PARAMETERS["port"],
        debug=PARAMETERS["debug"], reloader=PARAMETERS["reloader"])

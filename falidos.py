from bottle import *
import argparse
from db_abstraction import worker
import hashlib

def verify_login():
	if request.get_cookie('logged') == None:
		redirect('/authentication_failure')


@route('/css/<filename>')
def stylesheets(filename):
    return static_file(filename, root='./css')


@route('/fonts/<filename>')
def fonts(filename):
	return static_file(filename, root='./fonts')


@route('/img/<filename>')
def imgs(filename):
	return static_file(filename, root='./img')


@route('/')
def home_page():
	return template('home_page.tpl')


@route('/authentication_failure')
def authentication_failure():
	return template('aviso_auth.tpl')


@route('/login', method=['GET', 'POST'])
def index():

	if request.params.get('login', ''):
		email = request.params.get('email', '')
		password = hashlib.sha256()
		password.update(request.params.get('password', '').encode())
		result =worker('falidos.db', 
			'SELECT password FROM user WHERE email = ?', (email,)).query()

		if result[0][0] == password.hexdigest():
			response.set_cookie('logged', 'true', 
				path='/', max_age=300)
			redirect('/project_registration')
		else:
			return template('index.tpl', message="Usuário ou senha incorretos")
	else:
		return template('index.tpl', message=None)


@route('/project_registration', method=['GET', 'POST'])
def project_registration():
	
	verify_login()

	if request.params.get('register', ''):
		project_name = request.params.get('project_name')
		guilty = request.params.get('guilty')
		hope = request.params.get('hope')
		
		result = worker('falidos.db', 
			'INSERT INTO project (name, guilty, hope) VALUES (?,?,?)', 
			(project_name.encode(), guilty, hope)).insert()

		return template('cadastro_projeto.tpl',
		message='O projeto {} foi cadastrado com sucesso!'.format(project_name))
	else:
		return template('cadastro_projeto.tpl', message=None)	


@route('/user_registration', method=['GET', 'POST'])
def user_registration():
	
	verify_login()

	if request.params.get('register', ''):
		name = request.params.get('name')
		email = request.params.get('email')
		user_name = request.params.get('user_name')
		password = hashlib.sha256()
		password.update(request.params.get('password', '').encode())

		result = worker('falidos.db', 
			'INSERT INTO user (name, email, user, password) VALUES (?,?,?,?)', 
			(name, email, user_name, password.hexdigest())).insert()
		
		return template('cadastro_usuario.tpl',	
			message='O usuário {} foi cadastrado com sucesso!'.format(user_name))
	else:
		return template('cadastro_usuario.tpl', message=None)	


@route('/all_projects', method=['GET', 'POST'])
def all_projects():

	verify_login()

	result = worker('falidos.db','SELECT * FROM project').query()

	return template('todos_projetos.tpl', rows=result)



@route('/all_users', method=['GET', 'POST'])
def all_users():

	verify_login()

	result = worker('falidos.db', 
		'SELECT name, email, user FROM user').query()
	
	return template('todos_usuarios.tpl', rows=result)

@route('/create_db')
def create_db():
	import sqlite3
	con = sqlite3.connect('falidos.db') # Warning: This file is created in the current directory
	con.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name char(40) NOT NULL, email char(30) NOT NULL, user char(10) NOT NULL, password char(32) NOT NULL)")
	con.execute("CREATE TABLE project (id INTEGER PRIMARY KEY, name char(40) NOT NULL, guilty char(10) NOT NULL, hope boolean NOT NULL)")
	con.execute('''INSERT INTO user (name, email, user, password) VALUES ('admin', 'admin@admin', 'admin', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4')''')
	con.commit()

@error(404)
def error_404():
	return template('erro_404.tpl')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--port", type=int,
		help="specify the port where the app is gonna run.")
	parser.add_argument("--db",
		help="specify the database to be used.")
	args = parser.parse_args()

	if args.port:
		run(host='0.0.0.0', port=args.port)
	else:
		run(host='localhost', port=8080, debug=True, reloader=True)

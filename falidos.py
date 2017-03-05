from bottle import *
import argparse
import sqlite3
import hashlib

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


@route('/login', method=['GET', 'POST'])
def index():

	if request.params.get('login', ''):
		email = request.params.get('email', '')
		password = hashlib.sha256()
		password.update(request.params.get('password', '').encode())
		connection = sqlite3.connect('falidos.db')
		cursor = connection.cursor()
		cursor.execute('SELECT password FROM user WHERE email = ?', (email,))
		result = cursor.fetchone()
		cursor.close()

		if result[0] == password.hexdigest():
			redirect('/project_registration')
		else:
			return template('index.tpl', message="Usuario ou senha incorretos")
	else:
		return template('index.tpl', message=None)


@route('/project_registration', method=['GET', 'POST'])
def project_registration():
	
	if request.params.get('register', ''):
		project_name = request.params.get('project_name')
		guilty = request.params.get('guilty')
		hope = request.params.get('hope')
		connection = sqlite3.connect('falidos.db')
		cursor = connection.cursor()
		cursor.execute('''INSERT INTO project (name, guilty, hope) 
			VALUES (?,?,?)''', (project_name.encode(), guilty, hope))
		connection.commit()
		cursor.close()
		return template('cadastro_projeto.tpl',
			message='O projeto {} foi cadastrado com sucesso!'.format(project_name))
	else:
		return template('cadastro_projeto.tpl', message=None)	


@route('/user_registration', method=['GET', 'POST'])
def user_registration():
	
	if request.params.get('register', ''):
		name = request.params.get('name')
		email = request.params.get('email')
		user_name = request.params.get('user_name')
		password = hashlib.sha256()
		password.update(request.params.get('password', '').encode())

		connection = sqlite3.connect('falidos.db')
		cursor = connection.cursor()
		cursor.execute('''INSERT INTO user (name, email, user, password) 
			VALUES (?,?,?,?)''', (name, email, user_name, password.hexdigest()))
		connection.commit()
		cursor.close()
		return template('cadastro_usuario.tpl',
			message='O projeto {} foi cadastrado com sucesso!'.format(user_name))
	else:
		return template('cadastro_usuario.tpl', message=None)	


@route('/all_projects', method=['GET', 'POST'])
def all_projects():
	connection = sqlite3.connect('falidos.db')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM project')
	result = cursor.fetchall()
	cursor.close()

	return template('todos_projetos.tpl', rows=result)



@route('/all_users', method=['GET', 'POST'])
def all_users():
	connection = sqlite3.connect('falidos.db')
	cursor = connection.cursor()
	cursor.execute('SELECT name, email, user FROM user')
	result = cursor.fetchall()
	cursor.close()
	
	return template('todos_usuarios.tpl', rows=result)

@route('/create_db')
def create_db():
	import sqlite3
	con = sqlite3.connect('falidos.db') # Warning: This file is created in the current directory
	con.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name char(40) NOT NULL, email char(30) NOT NULL, user char(10) NOT NULL, password char(32) NOT NULL)")
	con.execute("CREATE TABLE project (id INTEGER PRIMARY KEY, name char(40) NOT NULL, guilty char(10) NOT NULL, hope boolean NOT NULL)")
	con.commit()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--port", type=int,
		help="specify the port where the app is gonna run.")
	args = parser.parse_args()

	if args.port:
		run(host='0.0.0.0', port=args.port)
	else:
		run(host='localhost', port=8080, debug=True, reloader=True)

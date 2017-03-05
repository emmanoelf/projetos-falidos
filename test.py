import falidos
from bottle import *

def test_index():
	assert falidos.index() == template('index.tpl')


if __name__ == '__main__':
	test_index()
'''Classe que abstrai conexoes
com sqlite3 e futuramente postgresql'''

import sqlite3


class Worker(object):
    '''Classe que recebe por parametro
    o a tabela, o trecho e os parametros
    para execucao de acoes com o
    banco de dados'''
    def __init__(self, table, statement, params=tuple()):
        self.table = table
        self.statement = statement
        self.params = params


    def query(self):
        '''Metodo responsavel por consultar
        o banco de dados e retornar o resultado'''
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()
        result = cursor.execute(self.statement, self.params).fetchall()
        cursor.close()
        return result


    def insert(self):
        '''Metodo responsavel por inserir dados no
        banco de dados'''
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()
        cursor.execute(self.statement, self.params)
        conn.commit()
        cursor.close()

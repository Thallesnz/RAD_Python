# LIBS NECESSARIAS
import sqlite3

# Classe Main do SQL
class SQL_Main():

    # Conectar banco de dados
    def func_conectar_banco(self):
        self.conectar = sqlite3.connect("banco\\banco.db")
        self.cursor =  self.conectar.cursor()
    
    # Desconectar banco
    def func_desconectar_banco(self):
        self.conectar.close()

    # Criar Tabela de Agendamentos & Grupos
    def func_criartabela_professores(self):
        self.func_conectar_banco()
        if self.cursor:
            try:
                self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Professores(
                        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        Nome VARCHAR(225) NOT NULL, 
                        Cpf VARCHAR(100) NOT NULL, 
                        Rg VARCHAR(100) NOT NULL,
                        Data VARCHAR(50) NOT NULL,
                        Cep VARCHAR(30) NOT NULL,
                        Estado VARCHAR(50) NOT NULL,
                        Endereco VARCHAR(125) NOT NULL,
                        Complemento VARCHAR(40) NOT NULL,
                        Email VARCHAR(225) NOT NULL, 
                        Senha VARCHAR(25) NOT NULL,
                        Unidade VARCHAR(50) NOT NULL,
                        Telefone VARCHAR(50) NOT NULL);
                    """)
                self.conectar.commit()
                print("Tabela de usuários criada dentro do banco de dados")
            except sqlite3.OperationalError as e:
                print(f"Erro ao criar tabela professores: {e}")

        #DEBUG
        self.func_desconectar_banco()

    # Grupos
    def func_criartabela_grupos(self):
        self.func_conectar_banco()
        if self.cursor:
            try:
                self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Grupos(
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        grupo VARCHAR(100) NOT NULL,
                        tema VARCHAR(225) NOT NULL, 
                        integrantes VARCHAR(355) NOT NULL);
                    """)
                self.conectar.commit()
                print("Tabela de Grupos criada dentro do banco de dados")
            except sqlite3.OperationalError as e:
                print(f"Erro ao criar tabela Grupos: {e}")

        self.func_desconectar_banco()        

    # Apresentação
    def func_criartabela_apresentacao(self):
        self.func_conectar_banco()
        if self.cursor:
            try:
                self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Apresentacao(
                        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        tema VARCHAR(225) NOT NULL, 
                        grupo VARCHAR(355) NOT NULL,
                        professor VARCHAR(225) NOT NULL,
                        data VARCHAR(35) NOT NULL,
                        hora VARCHAR(35) NOT NULL);
                    """)
                self.conectar.commit()
                print("Tabela de Agendamentos criada dentro do banco de dados")
            except sqlite3.OperationalError as e:
                print(f"Erro ao criar tabela Apresentacao: {e}")

        self.func_desconectar_banco()
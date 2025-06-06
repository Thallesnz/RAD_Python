# Libs
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

# LOGS 
def salvar_log(mensagem):
    with open("logs.txt", "a", encoding="utf-8") as arquivo:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{timestamp}] {mensagem}\n")

# Classe SQL Cadastros
class SQL_CadProfessores():
    def func_cadastrar_professor(self, nome, cpf, rg, data, cep, estado, endereco, complemento, email, senha, unidade, telefone):

        # Pegar Dados
        self.var_nome = nome
        self.var_cpf = cpf
        self.var_rg = rg
        self.var_data = data
        self.var_cep = cep
        self.var_estado = estado
        self.var_endereco = endereco
        self.var_complemento = complemento
        self.var_email = email
        self.var_senha = senha
        self.var_unidade = unidade
        self.var_telefone = telefone

        # Postar dados no SQL
        self.conectar = sqlite3.connect("banco\\banco.db")
        self.cursor =  self.conectar.cursor()
        self.cursor.execute("""
            SELECT * FROM Professores Where (Cpf =? OR Rg =? OR Email =?)""", (self.var_cpf, self.var_rg, self.var_email))
        self.check_dados = self.cursor.fetchone()

        # Verificar se o cadastro ja existe.
        if self.check_dados:

            # Dados
            cpf_db = self.check_dados[2]
            rg_db = self.check_dados[3]
            email_db = self.check_dados[9]

            if(self.var_cpf in cpf_db):
                messagebox.showerror(title="Sistema de cadastro", message="Ja existe um usuário cadastrado com este CPF!\nTroque o cpf que está cadastrando!")
            elif(self.var_rg in rg_db):
                messagebox.showerror(title="Sistema de cadastro", message="Ja existe um usuário cadastrado com este RG!\nTroque o RG que está cadastrando!")
            elif(self.var_email in email_db):
                messagebox.showerror(title="Sistema de cadastro", message="Ja existe um usuário cadastrado com este Email!\nTroque o Email que está cadastrando!")
            else:
                # Executar comando SQL
                self.cursor.execute("""
                    INSERT INTO Professores (Nome, Cpf, Rg, Data, Cep, Estado, Endereco, Complemento, Email, Senha, Unidade, Telefone) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                    (self.var_nome, self.var_cpf, self.var_rg, self.var_data, self.var_cep, self.var_estado,
                    self.var_endereco, self.var_complemento, self.var_email, self.var_senha, self.var_unidade, self.var_telefone))
                            
                self.conectar.commit()
                messagebox.showinfo(title="Sistema de cadastro", message="Conta criada com sucesso!")
                self.conectar.close()            
                salvar_log(f"O usuário {self.var_nome} acabou de ser criado no sistema") 
        else:
            
            # Verificações
            try:
                if(self.var_nome == "" or self.var_cpf == "" or self.var_rg == "" or self.var_data == "" or self.var_cep == "" or self.var_estado == "" or self.var_endereco == ""
                or self.var_complemento == "" or self.var_email == "" or self.var_senha == "" or self.var_unidade == "" or self.var_telefone == ""):
                    messagebox.showerror(title="Sistema de cadastro", message="Evite deixar algum campo em branco!\nPreencha todos os campos da tela de cadastro!")
                else:

                    # Executar comando SQL
                    self.cursor.execute("""
                        INSERT INTO Professores (Nome, Cpf, Rg, Data, Cep, Estado, Endereco, Complemento, Email, Senha, Unidade, Telefone) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                        (self.var_nome, self.var_cpf, self.var_rg, self.var_data, self.var_cep, self.var_estado,
                        self.var_endereco, self.var_complemento, self.var_email, self.var_senha, self.var_unidade, self.var_telefone))

                    self.conectar.commit()
                    messagebox.showinfo(title="Sistema de cadastro", message="Conta criada com sucesso!")
                    self.conectar.close()
                    salvar_log(f"O usuário {self.var_nome} acabou de ser criado no sistema")
            except:
                self.conectar.close()

# Classe da tela principal
class Screen_CadProfessor(SQL_CadProfessores):

    # Main
    def __init__(self, master):

        # Configurações da tela
        super().__init__()
        self.tela_cadprofessor = Toplevel(master)     
        self.configuracao_janela()

    # Configuração da janela
    def configuracao_janela(self):
        
        # Titulo & Tamanho Janela
        self.tela_cadprofessor.title("Cadastro de professores")
        self.tela_cadprofessor.grab_set() 

        # Estilo da tela
        style = ttk.Style()
        style.theme_use("vista") # ou 'alt', 'default', 'vista'
        style.configure("TButton", font=("Segoe UI", 10), padding = 10, foreground="#000000", background="#ffffff")

        # Configurar de tamanho da tela
        x_frm_padrao = 820
        y_frm_padrao = 380
        x_tela = self.tela_cadprofessor.winfo_screenwidth()
        y_tela = self.tela_cadprofessor.winfo_screenheight()
        x = (x_tela // 2) - (x_frm_padrao // 2)
        y = (y_tela // 2) - (y_frm_padrao // 2)       
        self.tela_cadprofessor.geometry(f"{x_frm_padrao}x{y_frm_padrao}+{x}+{y}")
        self.tela_cadprofessor.resizable(False, False)
        self.tela_cadprofessor.configure(background="#ffffff")
        self.tela_cadprofessor.overrideredirect(True)

        # Frame
        fmr_cad = ttk.Frame(self.tela_cadprofessor, width=800, height=360,borderwidth=1,style="TButton")
        fmr_cad.place(x=10, y= 10)

        # Nome
        lbl_nome = ttk.Label(self.tela_cadprofessor, text=f"Nome", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_nome.place(x=45, y=50)
        etr_nome = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_nome.place(x=33, y=78,height=23,width=240)
        
        # CPF
        lbl_cpf = ttk.Label(self.tela_cadprofessor, text=f"CPF", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_cpf.place(x=308, y=50)
        etr_cpf = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_cpf.place(x=300, y=78,height=23,width=130)     

        # RG
        lbl_rg = ttk.Label(self.tela_cadprofessor, text=f"RG", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_rg.place(x=478, y=50)
        etr_rg = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_rg.place(x=470, y=78,height=23,width=130)     

        # Data 
        lbl_data = ttk.Label(self.tela_cadprofessor, text=f"Data de nascimento", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_data.place(x=630, y=50)
        etr_data = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_data.place(x=622, y=78,height=23,width=165) 

        # Cep
        lbl_cep= ttk.Label(self.tela_cadprofessor, text=f"CEP", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_cep.place(x=45, y=118)
        etr_cep = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_cep.place(x=33, y=150,height=23,width=100)

        # Estado
        lbl_estado= ttk.Label(self.tela_cadprofessor, text=f"Estado", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_estado.place(x=158, y=118)
        etr_estado = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_estado.place(x=150, y=150,height=23,width=125)

        # Endereço
        lbl_endereco = ttk.Label(self.tela_cadprofessor, text=f"Endereço", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_endereco.place(x=308, y=118)
        etr_endereco = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_endereco.place(x=300, y=150,height=23,width=300)    

        # Complemento
        lbl_complemento = ttk.Label(self.tela_cadprofessor, text=f"Complemento", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_complemento.place(x=630, y=118)
        etr_complemento = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_complemento.place(x=622, y=150,height=23,width=165) 

        # Email
        lbl_email = ttk.Label(self.tela_cadprofessor, text=f"Email", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_email.place(x=45, y=180)
        etr_email = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_email.place(x=33, y=208,height=23,width=350)

        # Senha
        lbl_senha = ttk.Label(self.tela_cadprofessor, text=f"Senha de acesso", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_senha.place(x=408, y=180)
        etr_senha = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_senha.place(x=400, y=208,height=23,width=200)   

        # Unidade 
        lbl_unidade = ttk.Label(self.tela_cadprofessor, text=f"Unidade", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_unidade.place(x=630, y=180)
        etr_unidade = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_unidade.place(x=622, y=208,height=23,width=165)  

        # Telefone 
        lbl_telefone = ttk.Label(self.tela_cadprofessor, text=f"Telefone", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_telefone.place(x=45, y=255)
        etr_telefone = ttk.Entry(self.tela_cadprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_telefone.place(x=33, y=285,height=23,width=165)

        # Limpar Campos
        def limpar_campos():
            etr_nome.delete(0, "end")  
            etr_cpf.delete(0, "end")  
            etr_rg.delete(0, "end")  
            etr_data.delete(0, "end")  
            etr_cep.delete(0, "end")  
            etr_estado.delete(0, "end")  
            etr_endereco.delete(0, "end")  
            etr_complemento.delete(0, "end")  
            etr_email.delete(0, "end") 
            etr_senha.delete(0, "end")  
            etr_unidade.delete(0, "end")  
            etr_telefone.delete(0, "end")

        # Criar Botao
        btn_entrar = ttk.Button(self.tela_cadprofessor, text="Criar conta", style="TButton", command=lambda: [self.func_cadastrar_professor(
            etr_nome.get(), etr_cpf.get(), etr_rg.get(), etr_data.get(), etr_cep.get(), etr_estado.get(), etr_endereco.get(), etr_complemento.get(),
            etr_email.get(), etr_senha.get(), etr_unidade.get(), etr_telefone.get()), limpar_campos(), salvar_log(f"Um usario com login {etr_email.get()} acabou de ser criado no banco de dados")])
        btn_entrar.place(x=550, y=265,height=60)
    
        # Sair
        btn_sair = ttk.Button(self.tela_cadprofessor, text="Fechar", command=self.func_sair, style="TButton")
        btn_sair.place(x=690, y=265,height=60) 
        
    # Fechar Janela
    def func_sair(self):
        self.tela_cadprofessor.destroy()
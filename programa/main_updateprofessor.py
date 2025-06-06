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
class SQL_UpdateProfessores():
    def func_update_professor(self, oldemail, nome, cpf, rg, data, cep, estado, endereco, complemento, email, senha, unidade, telefone):

        # Pegar Dados
        self.oldemail = oldemail
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
        try:
            if(self.var_nome == "" or self.var_cpf == "" or self.var_rg == "" or self.var_data == "" or self.var_cep == "" or self.var_estado == "" or self.var_endereco == ""
            or self.var_complemento == "" or self.var_email == "" or self.var_senha == "" or self.var_unidade == "" or self.var_telefone == ""):
                messagebox.showerror(title="Sistema de cadastro", message="Evite deixar algum campo em branco!\nPreencha todos os campos da tela de atualização!")
            else:
                # Executar comando SQL
                self.cursor.execute("""
                    UPDATE Professores SET Nome = ?, Cpf = ?, Rg = ?, Data = ?, Cep = ?, Estado = ?, Endereco = ?, Complemento = ?, Email = ?, Senha = ?, Unidade = ?, Telefone = ?  WHERE Email = ?
                    """, (self.var_nome, self.var_cpf, self.var_rg, self.var_data, self.var_cep, self.var_estado, self.var_endereco
                    , self.var_complemento, self.var_email, self.var_senha, self.var_unidade, self.var_telefone, self.oldemail))                            
                self.conectar.commit()
                salvar_log(f"O usuário {self.oldemail} atualizou os dados no banco de dados")
                messagebox.showinfo(title="Sistema de cadastro", message="Cadastro atualizado com sucesso!")
                self.conectar.close()            
                self.tela_updateprofessor.destroy() 
        except:
            self.conectar.close()   
        # else:
        #     messagebox.showerror(title="Sistema de cadastro", message="Erro...\nNão conseguimos conectar ao banco de dados tente novamente!")

# Classe da tela principal
class Screen_UpdateProfessor(SQL_UpdateProfessores):

    # Main
    def __init__(self, master, emailuser):

        # Configurações da tela
        super().__init__()
        self.tela_updateprofessor = Toplevel(master)     
        self.configuracao_janela(emailuser)

    # Configuração da janela
    def configuracao_janela(self, emailuser):
        
        # Titulo & Tamanho Janela
        self.tela_updateprofessor.title("Cadastro de professores")
        self.tela_updateprofessor.grab_set() 
        self.email_conectado = emailuser

        # Estilo da tela
        style = ttk.Style()
        style.theme_use("vista") # ou 'alt', 'default', 'vista'
        style.configure("TButton", font=("Segoe UI", 10), padding = 10, foreground="#000000", background="#ffffff")

        # Configurar de tamanho da tela
        x_frm_padrao = 820
        y_frm_padrao = 380
        x_tela = self.tela_updateprofessor.winfo_screenwidth()
        y_tela = self.tela_updateprofessor.winfo_screenheight()
        x = (x_tela // 2) - (x_frm_padrao // 2)
        y = (y_tela // 2) - (y_frm_padrao // 2)       
        self.tela_updateprofessor.geometry(f"{x_frm_padrao}x{y_frm_padrao}+{x}+{y}")
        self.tela_updateprofessor.resizable(False, False)
        self.tela_updateprofessor.configure(background="#ffffff")
        self.tela_updateprofessor.overrideredirect(True)

        # Dados no SQL
        self.conectar = sqlite3.connect("banco\\banco.db")
        self.cursor =  self.conectar.cursor()
        self.cursor.execute("""
            SELECT * FROM Professores Where (Email =?)""", (self.email_conectado, ))
        self.check_dados = self.cursor.fetchone()

        # Dados
        nome_db = self.check_dados[1]
        cpf_db = self.check_dados[2]
        rg_db = self.check_dados[3]
        data_db = self.check_dados[4]
        cep_db = self.check_dados[5]
        estado_db = self.check_dados[6]
        endereco_db = self.check_dados[7]
        complemento_db = self.check_dados[8]
        email_db = self.check_dados[9]
        senha_db = self.check_dados[10]
        unidade_db = self.check_dados[11]
        telefone_db = self.check_dados[12]

        # Frame
        fmr_cad = ttk.Frame(self.tela_updateprofessor, width=800, height=360,borderwidth=1,style="TButton")
        fmr_cad.place(x=10, y= 10)

        # Nome
        lbl_nome = ttk.Label(self.tela_updateprofessor, text=f"Nome", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_nome.place(x=45, y=50)
        etr_nome = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_nome.place(x=33, y=78,height=23,width=240)
        
        # CPF
        lbl_cpf = ttk.Label(self.tela_updateprofessor, text=f"CPF", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_cpf.place(x=308, y=50)
        etr_cpf = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_cpf.place(x=300, y=78,height=23,width=130)     

        # RG
        lbl_rg = ttk.Label(self.tela_updateprofessor, text=f"RG", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_rg.place(x=478, y=50)
        etr_rg = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_rg.place(x=470, y=78,height=23,width=130)     

        # Data 
        lbl_data = ttk.Label(self.tela_updateprofessor, text=f"Data de nascimento", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_data.place(x=630, y=50)
        etr_data = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_data.place(x=622, y=78,height=23,width=165) 

        # Cep
        lbl_cep= ttk.Label(self.tela_updateprofessor, text=f"CEP", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_cep.place(x=45, y=118)
        etr_cep = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_cep.place(x=33, y=150,height=23,width=100)

        # Estado
        lbl_estado= ttk.Label(self.tela_updateprofessor, text=f"Estado", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_estado.place(x=158, y=118)
        etr_estado = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_estado.place(x=150, y=150,height=23,width=125)

        # Endereço
        lbl_endereco = ttk.Label(self.tela_updateprofessor, text=f"Endereço", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_endereco.place(x=308, y=118)
        etr_endereco = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_endereco.place(x=300, y=150,height=23,width=300)    

        # Complemento
        lbl_complemento = ttk.Label(self.tela_updateprofessor, text=f"Complemento", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_complemento.place(x=630, y=118)
        etr_complemento = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_complemento.place(x=622, y=150,height=23,width=165) 

        # Email
        lbl_email = ttk.Label(self.tela_updateprofessor, text=f"Email", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_email.place(x=45, y=180)
        etr_email = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_email.place(x=33, y=208,height=23,width=350)

        # Senha
        lbl_senha = ttk.Label(self.tela_updateprofessor, text=f"Senha de acesso", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_senha.place(x=408, y=180)
        etr_senha = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_senha.place(x=400, y=208,height=23,width=200)   

        # Unidade 
        lbl_unidade = ttk.Label(self.tela_updateprofessor, text=f"Unidade", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_unidade.place(x=630, y=180)
        etr_unidade = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_unidade.place(x=622, y=208,height=23,width=165)  

        # Telefone 
        lbl_telefone = ttk.Label(self.tela_updateprofessor, text=f"Telefone", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_telefone.place(x=45, y=255)
        etr_telefone = ttk.Entry(self.tela_updateprofessor, width=32, font=("Microsoft yahei ui light", 10))
        etr_telefone.place(x=33, y=285,height=23,width=165)

        ## UPDATE ENTRYS
        etr_nome.insert(0, nome_db)
        etr_cpf.insert(0, cpf_db)
        etr_rg.insert(0, rg_db)
        etr_data.insert(0, data_db)
        etr_cep.insert(0, cep_db)
        etr_estado.insert(0, estado_db)
        etr_endereco.insert(0, endereco_db)
        etr_complemento.insert(0, complemento_db)
        etr_email.insert(0, email_db)
        etr_senha.insert(0, senha_db)
        etr_unidade.insert(0, unidade_db)
        etr_telefone.insert(0, telefone_db)

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
        btn_entrar = ttk.Button(self.tela_updateprofessor, text="Atualizar cadastro", style="TButton", command=lambda: self.func_update_professor(
            self.email_conectado, etr_nome.get(), etr_cpf.get(), etr_rg.get(), etr_data.get(), etr_cep.get(), etr_estado.get(), etr_endereco.get(), etr_complemento.get(),
            etr_email.get(), etr_senha.get(), etr_unidade.get(), etr_telefone.get()))
        btn_entrar.place(x=550, y=265,height=60)

        # Sair
        btn_sair = ttk.Button(self.tela_updateprofessor, text="Fechar", command=self.func_sair, style="TButton")
        btn_sair.place(x=690, y=265,height=60) 
        
    # Fechar Janela
    def func_sair(self):
        self.tela_updateprofessor.destroy()
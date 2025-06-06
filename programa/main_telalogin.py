# Libs
import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from main_bancodados import SQL_Main 
from main_cadprofessor import Screen_CadProfessor
import datetime

# PATH DIR
dir_programa = os.path.dirname(__file__)

# LOGS 
def salvar_log(mensagem):
    with open("logs.txt", "a", encoding="utf-8") as arquivo:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{timestamp}] {mensagem}\n")

# Class Tela de Login
class Screen_Login():

    # Main
    def __init__(self, reload_menu):

        if(reload_menu == 1):
            # Configurações
            self.tela_login = Tk() 
            self.config_telalogin()   
            self.sql_login = SQL_Main()
            self.sql_login.func_criartabela_professores()
            self.sql_login.func_criartabela_grupos()
            self.sql_login.func_criartabela_apresentacao()
            self.tela_login.mainloop()
        else:
            # Configurações
            self.tela_login = Tk() 
            self.config_telalogin()   
            self.sql_login = SQL_Main()
            self.sql_login.func_criartabela_professores()
            self.sql_login.func_criartabela_grupos()
            self.sql_login.func_criartabela_apresentacao()
            self.tela_login.mainloop()

    # Configuração da tela #
    def config_telalogin(self):

        # Titulo & Tamanho Janela
        self.tela_login.title("Tela de login")

        # Estilo da tela
        style = ttk.Style()
        style.theme_use("vista") # ou 'alt', 'default', 'vista'
        style.configure("TButton", font=("Segoe UI", 12), padding = 5, background="#ffffff", foreground="#000000")
        img_id = Image.open(dir_programa+"\\img\\img_login.png")
        icon_id = ImageTk.PhotoImage(img_id)
        img_icon = Label(self.tela_login, image=icon_id,border=0, background="#ffffff")
        img_icon.place(x=350, y=30)

        # Configurar de tamanho da tela
        x_frm_padrao = 750
        y_frm_padrao = 420
        x_tela = self.tela_login.winfo_screenwidth()
        y_tela = self.tela_login.winfo_screenheight()
        x = (x_tela // 2) - (x_frm_padrao // 2)
        y = (y_tela // 2) - (y_frm_padrao // 2)       
        self.tela_login.geometry(f"{x_frm_padrao}x{y_frm_padrao}+{x}+{y}")
        self.tela_login.resizable(False, False)
        self.tela_login.configure(background="#ffffff")

        # Info & Frame
        fmr_login = ttk.Frame(self.tela_login, width=338, height=400,borderwidth=2,style="TButton")
        fmr_login.place(x=10, y= 10)
        lbl_topo = ttk.Label(self.tela_login, text=f"Bem vindo", font=("Microsoft yahei ui light", 24), foreground="#00CCFF", background="#ffffff", anchor='center')
        lbl_topo.place(x=100, y=45)
        lbl_topo2 = ttk.Label(self.tela_login, text=f"Efetue seu login na nossa plataforma\npara utilizar nossos serviços.", font=("Microsoft yahei ui light", 12), foreground="#00CCFF", background="#ffffff", anchor=CENTER, justify=CENTER)
        lbl_topo2.place(x=35, y=80)

        # Email 
        lbl_email = ttk.Label(self.tela_login, text=f"Email", font=("Microsoft yahei ui light", 13), background="#ffffff")
        lbl_email.place(x=45, y=180)
        etr_email = ttk.Entry(self.tela_login, width=32, font=("Microsoft yahei ui light", 10))
        etr_email.place(x=33, y=208,height=23,width=290)
        etr_email.insert(0, "Digite o seu email aqui")
        etr_email.config(foreground="gray")
            
        # Senha
        lbl_senha = ttk.Label(self.tela_login, text=f"Senha", font=("Microsoft yahei ui light", 13), background="#ffffff")
        lbl_senha.place(x=45, y=250)
        etr_senha = ttk.Entry(self.tela_login, width=32, font=("Microsoft yahei ui light", 10))
        etr_senha.place(x=33, y=278,height=23,width=290)
        etr_senha.insert(0, "Digite a sua senha aqui")
        etr_senha.config(foreground="gray")

        # Botões
        btn_entrar = ttk.Button(self.tela_login, text="Entrar", style="TButton", command=lambda: [self.func_efetuar_login(etr_email.get(), etr_senha.get())])
        btn_entrar.place(x=45, y=350,height=45)
        btn_sair = ttk.Button(self.tela_login, text="Sair", command=self.func_sair , style="TButton")
        btn_sair.place(x=205, y=350,height=45)

        # Check Mostrar senha Def & Var
        var_checkbox_status = IntVar()
        def func_checkbox():
            if var_checkbox_status.get() == 1: etr_senha.config(foreground="black", show="")
            elif var_checkbox_status.get() == 0: etr_senha.config(foreground="black", show="*")
        
        # Check Mostrar senha
        checkbox_senha = Checkbutton(self.tela_login, command=func_checkbox, variable=var_checkbox_status, onvalue=1, offvalue=0, text="Mostrar senha" , font=("Microsoft yahei ui light", 10), background="#ffffff")
        checkbox_senha.place(x=33, y=310) 

        # CRIAR CONTA        
        btn_cadastro = ttk.Button(self.tela_login, text="Cria uma conta", command=self.abrir_cadastro)
        btn_cadastro.place(x=600, y=370,height=40)
        
        # Defs adicionais
        def email_remove_text(event):
            if etr_email.get() == "Digite o seu email aqui":
                etr_email.delete(0, "end")
                etr_email.config(foreground="black")
        def email_add_text(event):
            if not etr_email.get():
                etr_email.insert(0, "Digite o seu email aqui")
                etr_email.config(foreground="gray")
        def senha_remove_text(event):
            if etr_senha.get() == "Digite a sua senha aqui":
                etr_senha.delete(0, "end")  
                if var_checkbox_status.get() == 1:
                    etr_senha.config(foreground="black", show="")
                elif var_checkbox_status.get() == 0:
                    etr_senha.config(foreground="black", show="*")
            else:
                if var_checkbox_status.get() == 1:
                    etr_senha.config(foreground="black", show="")
                elif var_checkbox_status.get() == 0:
                    etr_senha.config(foreground="black", show="*")
        def senha_add_text(event):
            if not etr_senha.get():
                etr_senha.insert(0, "Digite a sua senha aqui")
                etr_senha.config(foreground="gray", show="")

        # Focus Entrys
        etr_email.bind("<FocusIn>", email_remove_text)
        etr_email.bind("<FocusOut>", email_add_text)
        etr_senha.bind("<FocusIn>", senha_remove_text)
        etr_senha.bind("<FocusOut>", senha_add_text)
        
    # Fechar Janela
    def func_sair(self):
        self.tela_login.destroy()

    def abrir_cadastro(self):
        Screen_CadProfessor(self.tela_login)

    def func_efetuar_login(self, email, senha):

        # Dados Para O SQL
        self.var_email = email
        self.var_senha = senha

        if(self.var_email == "" or self.var_senha == ""):
            messagebox.showerror(title="Sistema de login", message="Evite deixar algum campo em branco!\nPreencha todos os campos da tela de login!")
        else:   
            self.conectar = sqlite3.connect("banco\\banco.db")
            self.cursor = self.conectar.cursor()
            self.cursor.execute("""SELECT * FROM Professores Where (Email =? OR Senha =?)""", (self.var_email, self.var_senha))
            self.check_dados = self.cursor.fetchone()

            # Verificar se o cadastro ja existe.
            if self.check_dados:
                email_db = self.check_dados[9]
                senha_db = self.check_dados[10]

                if(self.var_email in email_db):
                    if(self.var_senha in senha_db):
                        messagebox.showinfo(title="Sistema de cadastro", message="Login efetuado com sucesso!")  
                        salvar_log(f"O usuário {email_db} acabou de entrar no sistema")
                        self.tela_login.destroy()    
                        from main_principal import Screen_Principal             
                        Screen_Principal(email_db)                        
                    else:
                        messagebox.showerror(title="Sistema de login", message="Erro..Digite novamente sua senha!\nE tente novamente efetuar o login")
                elif(self.var_senha in senha_db):
                    if(self.var_email in email_db):
                        messagebox.showinfo(title="Sistema de cadastro", message="Login efetuado com sucesso!")
                        salvar_log(f"O usuário {email_db} acabou de entrar no sistema")
                        self.tela_login.destroy()
                        from main_principal import Screen_Principal
                        Screen_Principal(email_db)        
                    else:
                        messagebox.showerror(title="Sistema de login", message="Erro..Digite novamente seu email!\nE tente novamente efetuar o login")
                else:
                    messagebox.showerror(title="Sistema de login", message="Erro..Digite novamente seu email e senha!\nE tente novamente efetuar o login")
            else:
                messagebox.showerror(title="Sistema de login", message="Erro..Digite novamente seu email e senha!\nE tente novamente efetuar o login")
                
            # Fechar Banco
            self.conectar.close()

# Criar Janela
if __name__ == "__main__":
    Screen_Login(0)
# Main Lib 
import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main_telalogin import Screen_Login
from main_updateprofessor import Screen_UpdateProfessor
from main_relatorio_agendamentos import Screen_RelatorioAgendamentos
from main_relatorio_grupos import Screen_RelatorioGrupos
import datetime

# LOGS 
def salvar_log(mensagem):
    with open("logs.txt", "a", encoding="utf-8") as arquivo:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{timestamp}] {mensagem}\n")

# Classe SQL Principal
class SQL_MenuPrincipal():
    def func_conectar(self):
        self.conectar = sqlite3.connect("banco\\banco.db")
        self.cursor =  self.conectar.cursor()
        return self.conectar 
    def func_desconectar(self):
        self.conectar.close()
    def func_inserir_apresentacao(self, tema, grupo, professor, data, hora):
        self.var_tema = tema
        self.var_grupo = grupo
        self.var_professor = professor
        self.var_data = data
        self.var_hora = hora

        # Verificações
        try:
            if(self.var_tema == "" or self.var_grupo == "" or self.var_professor == "" or self.var_data == "" or self.var_hora == ""):
                messagebox.showerror(title="Sistema de agendamento", message="Evite deixar algum campo em branco!\nPreencha todos os campos do agendamento de grupos!")
            else:
                # Executar comando SQL
                self.func_conectar()
                self.cursor.execute("""
                    INSERT INTO Apresentacao (tema, grupo, professor, data, hora) 
                    VALUES (?, ?, ?, ?, ?)""", (self.var_tema, self.var_grupo, self.var_professor, self.var_data, self.var_hora))

                self.conectar.commit()
                messagebox.showinfo(title="Sistema de agendamento", message="Agendamento realizado com sucesso!")
                self.func_desconectar()
        except:
            pass
    
    def func_atualizar_apresentacao(self, tema, grupo, professor, data, hora):        
        self.var_tema = tema
        self.var_grupo = grupo
        self.var_professor = professor
        self.var_data = data
        self.var_hora = hora

        # Verificações
        try:
            if(self.var_tema == "" or self.var_grupo == "" or self.var_professor == "" or self.var_data == "" or self.var_hora == ""):
                messagebox.showerror(title="Sistema de agendamento", message="Evite deixar algum campo em branco!\nPreencha todos os campos do agendamento de grupos!")
            else:
                # Executar comando SQL
                self.func_conectar()
                self.cursor.execute("""
                    UPDATE Apresentacao SET tema = ?, grupo = ?, professor = ?, data = ?, hora = ? WHERE grupo = ?
                    """, (self.var_tema, self.var_grupo, self.var_professor, self.var_data, self.var_hora, self.var_grupo))
                self.conectar.commit()
                messagebox.showinfo(title="Sistema de agendamento", message="Agendamento atualizado com sucesso!")
                self.func_desconectar()
        except:
            pass

    def func_deletar_all(self):
        self.func_conectar()
        self.cursor.execute("DELETE FROM Apresentacao")
        self.conectar.commit()
        messagebox.showinfo(title="Sistema de agendamento", message="Parabêns você limpou toda tabela de agendamentos!")
        self.func_desconectar()

    def func_deletar_all_grupos(self):
        self.func_conectar()
        self.cursor.execute("DELETE FROM Grupos")
        self.conectar.commit()
        messagebox.showinfo(title="Sistema de grupos", message="Parabêns você limpou toda tabela de grupos!")
        self.func_desconectar()

    def func_atualizar_grupos(self, grupo, tema, integrantes):        
        self.var_grupo = grupo
        self.var_tema = tema
        self.var_integrantes = integrantes

        # Verificações
        try:
            if(self.var_grupo == "" or self.var_tema == "" or self.var_integrantes == ""):
                messagebox.showerror(title="Sistema de grupos", message="Evite deixar algum campo em branco!\nPreencha todos os campos do grupo!")
            else:
                # Executar comando SQL
                self.func_conectar()
                self.cursor.execute("""
                    UPDATE Grupos SET grupo = ?, tema = ?, integrantes = ?
                    """, (self.var_grupo, self.var_tema, self.var_integrantes))
                self.conectar.commit()
                messagebox.showinfo(title="Sistema de grupos", message="Grupo atualizado com sucesso!")
                self.func_desconectar()
        except:
            pass

    def func_inserir_grupo(self, grupo, tema, integrantes):
        self.var_grupo = grupo
        self.var_tema = tema
        self.var_integrantes = integrantes

        # Verificações
        try:
            if(self.var_grupo == "" or self.var_tema == "" or self.var_integrantes == ""):
                messagebox.showerror(title="Sistema de grupos", message="Evite deixar algum campo em branco!\nPreencha todos os campos do cadastro de grupos!")
            else:
                # Executar comando SQL
                self.func_conectar()
                self.cursor.execute("""
                    INSERT INTO Grupos (grupo, tema, integrantes) 
                    VALUES (?, ?, ?)""", (self.var_grupo, self.var_tema, self.var_integrantes))

                self.conectar.commit()
                messagebox.showinfo(title="Sistema de grupos", message="Cadastro realizado com sucesso!")
                self.func_desconectar()
        except:
            pass

# Class Tela de Login
class Screen_Principal(SQL_MenuPrincipal):
    def __init__(self, email):

        # Configurações
        self.janela = Tk()        
        self.email_id = email
        self.config_telaprincipal()
        self.janela.mainloop()
        

    # Configuração da tela
    def config_telaprincipal(self):
        
        # Estilo da tela
        style = ttk.Style()
        style.theme_use("vista") # ou 'alt', 'default', 'vista'
        style.configure("TButton", font=("Segoe UI", 10), padding = 10, foreground="#000000", background="#ffffff")

        # Configurar de tamanho da tela
        self.janela.title("Menu Principal")
        x_frm_padrao = 900
        y_frm_padrao = 700
        x_tela = self.janela.winfo_screenwidth()
        y_tela = self.janela.winfo_screenheight()
        x = (x_tela // 2) - (x_frm_padrao // 2)
        y = (y_tela // 2) - (y_frm_padrao // 2)       
        self.janela.geometry(f"{x_frm_padrao}x{y_frm_padrao}+{x}+{y}")
        self.janela.resizable(False, False)
        self.janela.configure(background="#ffffff")
        self.janela.minsize(900, 700)

        # Menu ID
        menubar_id = Menu(self.janela)   

        # Arquivos
        menubar_file = Menu(menubar_id, tearoff=0)
        menubar_file.add_command(label="Editar Perfil", command=lambda: Screen_UpdateProfessor(self.janela, emailuser=self.email_id))
        menubar_file.add_separator()
        menubar_file.add_command(label="Sair", command=lambda:[self.janela.destroy(), Screen_Login(1)])
        menubar_id.add_cascade(label="Arquivo", menu=menubar_file)

        # Relatorios
        menubar_relatorio = Menu(menubar_id, tearoff=0)
        menubar_relatorio.add_command(label="Grupos agendados", command=lambda:Screen_RelatorioAgendamentos())
        menubar_relatorio.add_command(label="Grupos cadastrados", command=lambda: Screen_RelatorioGrupos())
        menubar_id.add_cascade(label="Relatórios", menu=menubar_relatorio)

        # Mostrar Menu
        self.janela.config(menu=menubar_id) 

        # Frames
        fmr_lagendamentos = ttk.Frame(self.janela, width=880, height=100,borderwidth=1,style="TButton")
        fmr_lagendamentos.place(x=10, y= 150, height=200)
        fmr_grupos = ttk.Frame(self.janela, width=880, height=100,borderwidth=1,style="TButton")
        fmr_grupos.place(x=10, y= 535, height=160)

        # Defs Adicionais
        def get_itens_agendamentos(event):
            selecionado = tabela.selection()
            if selecionado:
                tabela_dados = selecionado[0]
                tabela_itens = tabela.item(tabela_dados, "values")
                etr_tema.delete(0, "end")  
                etr_tema.insert(0, tabela_itens[0])
                etr_grupos.delete(0, "end")  
                etr_grupos.insert(0, tabela_itens[1])
                etr_data.delete(0, "end")  
                etr_data.insert(0, tabela_itens[3])
                etr_horario.delete(0, "end")  
                etr_horario.insert(0, tabela_itens[4])
        def get_itens_grupos(event):
            selecionado = grupos_tabela.selection()
            if selecionado:
                tabela_dados = selecionado[0]
                tabela_itens = grupos_tabela.item(tabela_dados, "values")
                etr_addgrupo.delete(0, "end")  
                etr_addgrupo.insert(0, tabela_itens[0])
                etr_addtema.delete(0, "end")  
                etr_addtema.insert(0, tabela_itens[1])
                etr_addintegrantes.delete(0, "end")  
                etr_addintegrantes.insert(0, tabela_itens[2])
        
        # Deletar itens
        def deletar_agendamento():
            selecionado = tabela.selection()
            if selecionado:
                resposta = messagebox.askyesno("Confirmação", "Deseja realmente deletar este agendamento?")
                if(resposta):
                    tabela_dados = selecionado[0]
                    tabela_itens = tabela.item(tabela_dados, "values")  
                    conectar = self.func_conectar()
                    cursor = conectar.cursor()  
                    cursor.execute("""DELETE FROM Apresentacao WHERE grupo = ?""", (tabela_itens[1], ))
                    conectar.commit()                
                    self.func_desconectar()
                    salvar_log(f"O usuário {self.email_id}  acabou de remover o agendamento do grupo {tabela_itens[1]} do banco de dados")
                    tabela.delete(tabela_dados)
                    messagebox.showinfo(title="Sistema de agendamento", message="Agendamento removido com sucesso!")
            else:
                messagebox.showerror(title="Sistema de agendamento", message="Erro...Selecione qual agendamento deseja remover!")
        def deletar_grupo():
            selecionado = grupos_tabela.selection()
            if selecionado:
                resposta = messagebox.askyesno("Confirmação", "Deseja realmente deletar este grupo?")
                if(resposta):
                    tabela_dados = selecionado[0]
                    tabela_itens = grupos_tabela.item(tabela_dados, "values")  
                    conectar = self.func_conectar()
                    cursor = conectar.cursor()  
                    cursor.execute("""DELETE FROM Grupos WHERE grupo = ?""", (tabela_itens[0], ))
                    conectar.commit()                
                    self.func_desconectar()
                    salvar_log(f"O usuário {self.email_id}  acabou de remover o grupo {tabela_itens[1]} do banco de dados")
                    grupos_tabela.delete(tabela_dados)
                    messagebox.showinfo(title="Sistema de grupos", message="Grupo removido com sucesso!")
            else:
                messagebox.showerror(title="Sistema de grupos", message="Erro...Selecione qual grupo deseja remover!")


        # FRAME
        tabela = ttk.Treeview(fmr_lagendamentos, columns=("tema", "grupo", "professor", "data", "hora"), show="headings")
        tabela.heading("tema", text="Tema do grupo")
        tabela.column("tema", anchor=CENTER)
        tabela.heading("grupo", text="Grupo")
        tabela.column("grupo", anchor=CENTER)
        tabela.heading("professor", text="Professor")
        tabela.column("professor", anchor=CENTER)
        tabela.heading("data", text="Data")
        tabela.column("data", width=138, stretch=True, anchor=CENTER)
        tabela.heading("hora", text="Hora marcada")
        tabela.column("hora", width=138, stretch=True, anchor=CENTER)
        tabela.pack(fill="both", expand=True)
        tabela.bind("<<TreeviewSelect>>", get_itens_agendamentos)        

        # Tabela de grupos cadastrados
        grupos_tabela = ttk.Treeview(fmr_grupos, columns=("grupo", "tema", "integrantes"), show="headings")
        grupos_tabela.heading("grupo", text="Grupo")
        grupos_tabela.column("grupo", width=138, stretch=True, anchor=CENTER)
        grupos_tabela.heading("tema", text="Tema")
        grupos_tabela.column("tema", width=260, stretch=True, anchor=CENTER)
        grupos_tabela.heading("integrantes", text="Integrantes", anchor=CENTER)
        grupos_tabela.column("integrantes", width=480, stretch=True, anchor=CENTER)
        grupos_tabela.pack(fill="both", expand=True, anchor=CENTER)
        grupos_tabela.bind("<<TreeviewSelect>>", get_itens_grupos)

        # Tema
        lbl_tema = ttk.Label(self.janela, text=f"Tema do grupo", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_tema.place(x=60, y=20)  
        etr_tema = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_tema.place(x=50, y=50,height=23,width=180)        

        # Grupos Cadastrados
        conectar = self.func_conectar()
        cursor = conectar.cursor()  
        cursor.execute("SELECT grupo FROM Grupos")
        dados = cursor.fetchall()
        nomes = [linha[0] for linha in dados]
        lbl_grupos = ttk.Label(self.janela, text=f"Grupos", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_grupos.place(x=250, y=20)  
        etr_grupos = ttk.Combobox(self.janela, width=32, font=("Microsoft yahei ui light", 10), state="readonly")
        etr_grupos['values'] = nomes
        etr_grupos.place(x=240, y=50,height=23,width=150)

        # Atualizar Nomes
        def atualizar_professores():
            conectar = self.func_conectar()
            cursor = conectar.cursor()               
            cursor.execute("SELECT Nome FROM Professores")
            dados = cursor.fetchall()
            nomes = [linha[0] for linha in dados]
            etr_professor.config(values=nomes)
            conectar.close()    
        
        # Professores
        cursor.execute("SELECT Nome FROM Professores")
        dados = cursor.fetchall()
        nomes = [linha[0] for linha in dados]
        conectar.close()
        lbl_professor = ttk.Label(self.janela, text=f"Professor", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_professor.place(x=420, y=20)  
        etr_professor = ttk.Combobox(self.janela, width=32, font=("Microsoft yahei ui light", 10), state="readonly")
        etr_professor['values'] = nomes
        etr_professor.place(x=410, y=50,height=23,width=150)
        etr_professor.bind('<<ComboboxSelected>>', atualizar_professores())

        # Data
        lbl_data = ttk.Label(self.janela, text=f"Data", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_data.place(x=592, y=20)
        etr_data = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_data.place(x=580, y=50,height=23,width=140)

        # Horario
        lbl_horario = ttk.Label(self.janela, text=f"Horário", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_horario.place(x=752, y=20)
        etr_horario = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_horario.place(x=740, y=50,height=23,width=115)

        # Botões
        btn_agendar = ttk.Button(self.janela, text="Agendar apresentação", style="TButton", command=lambda: [self.func_inserir_apresentacao(etr_tema.get(), etr_grupos.get(), etr_professor.get(), etr_data.get(), etr_horario.get()), atualizar_agendamentos(), salvar_log(f"O usuário {self.email_id} acabou de remover o agendamento do grupo {etr_grupos.get()} do banco de dados")])
        btn_agendar.place(x=80, y=90,height=45)
        btn_editar = ttk.Button(self.janela, text="Atualizar apresentação", style="TButton", command=lambda: [self.func_atualizar_apresentacao(etr_tema.get(), etr_grupos.get(), etr_professor.get(), etr_data.get(), etr_horario.get()), atualizar_agendamentos(), salvar_log(f"O usuário {self.email_id} acabou de atualizar o agendamento do grupo {etr_grupos.get()} do banco de dados")])
        btn_editar.place(x=270, y=90,height=45)
        btn_remover = ttk.Button(self.janela, text="Remover apresentação", style="TButton", command=lambda: [deletar_agendamento(), atualizar_agendamentos(), salvar_log(f"O usuário {self.email_id} acabou de remover o agendamento do grupo {etr_grupos.get()} do banco de dados")])
        btn_remover.place(x=455, y=90,height=45)
        btn_remover = ttk.Button(self.janela, text="Limpar apresentações", style="TButton", command=lambda: [self.func_deletar_all(), atualizar_agendamentos(), salvar_log(f"O usuário {self.email_id} acabou de limpar os dados de todos os agendamentos cadastrados")])
        btn_remover.place(x=660, y=90,height=45)

        # Labels dos grupos
        lbl_addgrupo = ttk.Label(self.janela, text=f"Grupo", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_addgrupo.place(x=70, y=400)
        etr_addgrupo = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_addgrupo.place(x=60, y=430,height=23,width=140)
        lbl_addtema = ttk.Label(self.janela, text=f"Tema do grupo", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_addtema.place(x=280, y=400)
        etr_addtema = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_addtema.place(x=270, y=430,height=23,width=160)
        lbl_addintegrantes = ttk.Label(self.janela, text=f"Integrantes do grupo", font=("Microsoft yahei ui light", 12), background="#ffffff")
        lbl_addintegrantes.place(x=475, y=400)
        etr_addintegrantes = ttk.Entry(self.janela, width=32, font=("Microsoft yahei ui light", 10))
        etr_addintegrantes.place(x=455, y=430,height=23,width=400)

        # Botões - Grupos
        btn_grupocad = ttk.Button(self.janela, text="Cadastrar grupo", style="TButton", command=lambda: [self.func_inserir_grupo(etr_addgrupo.get(), etr_addtema.get(), etr_addintegrantes.get()), atualizar_grupos(), salvar_log(f"O usuário {self.email_id} acabou de cadastrar o grupo {etr_addgrupo.get()} no banco de dados")])
        btn_grupocad.place(x=80, y=470,height=45)
        btn_editargrup = ttk.Button(self.janela, text="Atualizar grupo", style="TButton", command=lambda: [self.func_atualizar_grupos(etr_addgrupo.get(), etr_addtema.get(), etr_addintegrantes.get()), atualizar_grupos(), salvar_log(f"O usuário {self.email_id} acabou de atualizar os dados do grupo {etr_addgrupo.get()} no banco de dados")])
        btn_editargrup.place(x=270, y=470,height=45)
        btn_removergrup = ttk.Button(self.janela, text="Remover grupo", style="TButton", command=lambda: [deletar_grupo(), atualizar_grupos(), salvar_log(f"O usuário {self.email_id} acabou de remover os dados do grupo {etr_addgrupo.get()} no banco de dados")])
        btn_removergrup.place(x=455, y=470,height=45)
        btn_removergrup = ttk.Button(self.janela, text="Limpar grupos", style="TButton", command=lambda: [self.func_deletar_all_grupos(), atualizar_grupos(), salvar_log(f"O usuário {self.email_id} acabou de limpar os dados de todos os grupos cadastrados")])
        btn_removergrup.place(x=660, y=470,height=45)

        # Def Atualizar Frames
        def atualizar_agendamentos():
            conectar = self.func_conectar()
            cursor = conectar.cursor()               
            cursor.execute("SELECT tema, grupo, professor, data, hora FROM Apresentacao")
            tabela_dados = cursor.fetchall()
            for item in tabela.get_children(): 
                tabela.delete(item)
            for linha in tabela_dados:
                tabela.insert("", "end", values=linha)
            conectar.close()

        # Forçar atualização ao abrir a tela
        atualizar_agendamentos()

        # Def Atualizar Frames e ComboBox
        def atualizar_grupos():
            conectar = self.func_conectar()
            cursor = conectar.cursor()               
            cursor.execute("SELECT grupo, tema, integrantes FROM Grupos")
            tabela_dados = cursor.fetchall()
            nomes = [linha[0] for linha in tabela_dados]
            for item in grupos_tabela.get_children(): 
                grupos_tabela.delete(item)
            for linha in tabela_dados:
                grupos_tabela.insert("", "end", values=linha)
            etr_grupos.config(values=nomes)
            conectar.close()

        # Forçar atualização Grupos
        atualizar_grupos()
# Main Lib 
import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Screen_RelatorioAgendamentos():

    def __init__(self):

        # Configurações
        self.janela = Toplevel()         
        self.configurar_relatorio()

    def configurar_relatorio(self):

        # Estilo da tela
        style = ttk.Style()
        style.theme_use("vista") # ou 'alt', 'default', 'vista'
        style.configure("TButton", font=("Segoe UI", 10), padding = 10, foreground="#000000", background="#ffffff")

        # Configurar de tamanho da tela
        self.janela.title("Relatorio de trabalhos agendados")
        x_frm_padrao = 900
        y_frm_padrao = 630
        x_tela = self.janela.winfo_screenwidth()
        y_tela = self.janela.winfo_screenheight()
        x = (x_tela // 2) - (x_frm_padrao // 2)
        y = (y_tela // 2) - (y_frm_padrao // 2)       
        self.janela.geometry(f"{x_frm_padrao}x{y_frm_padrao}+{x}+{y}")
        self.janela.configure(background="#ffffff")
        self.janela.minsize(900, 630)
        self.janela.maxsize(900, 640)

        # Criar frame e relatórios
        fmr_lagendamentos = ttk.Frame(self.janela, width=880, height=100,borderwidth=1,style="TButton")
        fmr_lagendamentos.place(x=10, y= 25, height=600)
        
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

        # Def Atualizar Frames
        def atualizar_agendamentos():
            conectar = sqlite3.connect("banco\\banco.db")
            cursor =  conectar.cursor()
            cursor.execute("SELECT tema, grupo, professor, data, hora FROM Apresentacao")
            tabela_dados = cursor.fetchall()
            for item in tabela.get_children(): 
                tabela.delete(item)
            for linha in tabela_dados:
                tabela.insert("", "end", values=linha)
            conectar.close()

        # Forçar atualização ao abrir a tela
        atualizar_agendamentos()
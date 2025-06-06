# Main Lib 
import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Screen_RelatorioGrupos():

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
        self.janela.title("Relatorio de grupos cadastrados")
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
        fmr_grupos = ttk.Frame(self.janela, width=880, height=100,borderwidth=1,style="TButton")
        fmr_grupos.place(x=10, y= 25, height=600)
        
        # Tabela de grupos cadastrados
        grupos_tabela = ttk.Treeview(fmr_grupos, columns=("grupo", "tema", "integrantes"), show="headings")
        grupos_tabela.heading("grupo", text="Grupo")
        grupos_tabela.column("grupo", width=138, stretch=True, anchor=CENTER)
        grupos_tabela.heading("tema", text="Tema")
        grupos_tabela.column("tema", width=260, stretch=True, anchor=CENTER)
        grupos_tabela.heading("integrantes", text="Integrantes", anchor=CENTER)
        grupos_tabela.column("integrantes", width=480, stretch=True, anchor=CENTER)
        grupos_tabela.pack(fill="both", expand=True, anchor=CENTER)

        # Def Atualizar Frames
        def atualizar_grupos():
            conectar = sqlite3.connect("banco\\banco.db")
            cursor =  conectar.cursor()            
            cursor.execute("SELECT grupo, tema, integrantes FROM Grupos")
            tabela_dados = cursor.fetchall()
            for item in grupos_tabela.get_children(): 
                grupos_tabela.delete(item)
            for linha in tabela_dados:
                grupos_tabela.insert("", "end", values=linha)
            conectar.close()

        # Forçar atualização Grupos
        atualizar_grupos()
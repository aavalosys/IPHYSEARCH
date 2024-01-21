import tkinter as tk
from tkinter import ttk
from tkinter import *
import DB_EQUIPOS2 as db_eq
import os
import sys
import pandas
from pandas import ExcelWriter
import datetime

class App(Frame):
    def __init__(self):
        super().__init__()
        #self.geometry("240x100")
        self.master.title("API 2")
        self.id_op = 0
        self.res_consulta=[]
    
        self.create_widgets()

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self)
        self.tabl1 = Frame(self.tab_control)
        self.tabl2 = Frame(self.tab_control)
        self.tabl3 = Frame(self.tab_control)
        self.tab_control.add(self.tabl1, text='Equipos/Interface')
        self.tab_control.add(self.tabl2, text='      IP      ')
        self.tab_control.add(self.tabl3, text='     VRFS     ')
        
        ########################## TAB1
        self.lista_busqueda = ["a","","","","","","",""]
        self.lista_tipo_wo=[]
        
        self.ip_label = ttk.Label(self.tabl1, text="IP:")
        self.ip_label.grid(column=0, row=0, padx=(20,4), pady=(10,2), columnspan = 2)
        self.ip_entry = ttk.Entry(self.tabl1, width= 35)
        self.ip_entry.grid(column=0, row=1, padx=(20,4), pady=2, columnspan = 2)
        self.ip_entry.bind("<KeyRelease-Return>", self.buscar_ent)
        
        self.pais_label = ttk.Label(self.tabl1, text="País:")
        self.pais_label.grid(column=2, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.pais_combo = ttk.Combobox(self.tabl1, width= 35, values=["", "GT", "SV", "HN", "NIC", "CR", "PA"],state="readonly")
        self.pais_combo.grid(column=2, row=1, padx=4, pady=2, columnspan = 2)
        self.pais_combo.current(0)
        #self.pais_combo.bind("<<ComboboxSelected>>", self.pais_sel)
        
        self.id_label = ttk.Label(self.tabl1, text="Celda/Desc IF:")
        self.id_label.grid(column=4, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.desc_entry = ttk.Entry(self.tabl1, width= 35)
        self.desc_entry.grid(column=4, row=1, padx=4, pady=2, columnspan = 2)
        self.desc_entry.bind("<KeyRelease-Return>", self.buscar_ent)
        
        self.nemip_label = ttk.Label(self.tabl1, text="NEM/IP EQ:")
        self.nemip_label.grid(column=6, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.nemip_entry = ttk.Entry(self.tabl1, width= 35)
        self.nemip_entry.grid(column=6, row=1, padx=(4), pady=2, columnspan = 2)
        self.nemip_entry.bind("<KeyRelease-Return>", self.buscar_ent)
        
        self.sitio_label = ttk.Label(self.tabl1, text="Lugar:")
        self.sitio_label.grid(column=8, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.sitio_entry = ttk.Entry(self.tabl1, width= 35)
        self.sitio_entry.grid(column=8, row=1, padx=(4,20), pady=2, columnspan = 2)
        self.sitio_entry.bind("<KeyRelease-Return>", self.buscar_ent)
        
        self.busqueda_button = ttk.Button(self.tabl1, text="Buscar",command = self.buscar)
        self.busqueda_button.grid(column=0, row=3, pady=10,columnspan = 5)
        
        self.borrar_button = ttk.Button(self.tabl1, text="Borrar",command = self.borrar)
        self.borrar_button.grid(column=5, row=3, pady=10,columnspan = 5)
        
        
        self.tree1 = ttk.Treeview(self.tabl1,height = 5)
        self.tree1["columns"] = ("Val")
        self.tree1.heading("#0", text="Campo")
        self.tree1.heading("Val", text="Valor")
        self.tree1.grid(column=0, row= 7, padx=(20,5), pady=10, columnspan = 5,sticky='nsew')
        self.tree1.bind('<<TreeviewSelect>>', self.selectpais)
        self.tree1.bind("<KeyRelease-1>", self.copiar_tree1)
        self.tree1.bind("<KeyRelease-2>", self.copiar_tree1_2)
        self.tree1.bind("<KeyRelease-5>", self.copiar_exportar)
        
        self.tree2 = ttk.Treeview(self.tabl1,height = 5)
        self.tree2["columns"] = ("Val")
        self.tree2.heading("#0", text="Campo")
        self.tree2.heading("Val", text="Valor")
        self.tree2.grid(column=5, row= 7, padx=(5,20), pady=10, columnspan = 5,sticky='nsew')
        self.tree2.bind('<<TreeviewSelect>>', self.select2)
        
        self.sitio_wo = ttk.Label(self.tabl1, text="WO")
        self.sitio_wo.grid(column=0, row=8, padx=20, pady=10, columnspan = 10)
        self.lb_area_wo = ttk.Label(self.tabl1, text="Area:")
        self.lb_area_wo.grid(column=0, row=9, padx=20, pady=(0,10), columnspan = 2)
        self.areawo_combo = ttk.Combobox(self.tabl1, values=["", "WO", "FO", "AC", "TX", "CX", "OT"],state="readonly")
        self.areawo_combo.grid(column=2, row=9, padx=4, pady=(0,10), columnspan = 2)
        self.areawo_combo.current(0)
        self.areawo_combo.bind("<<ComboboxSelected>>", self.areawo_se)
        self.lb_area_wo = ttk.Label(self.tabl1, text="Tipo:")
        self.lb_area_wo.grid(column=5, row=9, padx=20, pady=(0,10), columnspan = 2)
        self.tipowo_combo = ttk.Combobox(self.tabl1, values=[""],state="readonly")
        self.tipowo_combo.grid(column=7, row=9, padx=4, pady=(0,10), columnspan = 2)
        self.tipowo_combo.current(0)
        self.tipowo_combo.bind("<<ComboboxSelected>>", self.wo_text)

        self.bx_text1 = Text(self.tabl1, height = 4, width=30)
        self.bx_text1.config(font=('courier', 8, 'normal'))
        self.bx_text1.grid(column=0,row=10, padx=(20,5), pady=(0,5), columnspan = 2 )
        self.bx_text1.bind("<KeyRelease-Escape>", self.wo_rep1)
        self.bx_text2 = Text(self.tabl1, height = 4, width=30)
        self.bx_text2.config(font=('courier', 8, 'normal'))
        self.bx_text2.grid(column=0,row=11, padx=(20,5), pady=5, columnspan = 2)
        self.bx_text3 = Text(self.tabl1, height = 4, width=30)
        self.bx_text3.config(font=('courier', 8, 'normal'))
        self.bx_text3.grid(column=0,row=12, padx=(20,5), pady=(5,10), columnspan = 2)
        
        self.pasar_button = ttk.Button(self.tabl1, text=">>",command = self.insertarwo)
        self.pasar_button.grid(column=2, row=11, pady=10)
        
        self.bx_WO = Text(self.tabl1, height = 17, width=110)
        self.bx_WO.config(font=('courier', 8, 'normal'))
        self.bx_WO.grid(column=3, row=10, padx=(5,20), pady=(0,10), columnspan = 8, rowspan = 3)
        self.bx_WO.bind("<KeyRelease-Escape>", self.copywoa)
        
        
        ####----------------------------TAB2------------------------
        
        
        self.ip_label2 = ttk.Label(self.tabl2, text="IP:")
        self.ip_label2.grid(column=0, row=0, padx=(20,4), pady=(10,2), columnspan = 2)
        self.ip_entry2 = ttk.Entry(self.tabl2, width= 35)
        self.ip_entry2.grid(column=0, row=1, padx=(20,4), pady=2, columnspan = 2)
        
        self.pais_label2 = ttk.Label(self.tabl2, text="País:")
        self.pais_label2.grid(column=2, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.pais_combo2 = ttk.Combobox(self.tabl2, width= 35, values=["", "GT", "SV", "HN", "NIC", "CR", "PA"],state="readonly")
        self.pais_combo2.grid(column=2, row=1, padx=4, pady=2, columnspan = 2)
        self.pais_combo2.current(0)
        #self.pais_combo.bind("<<ComboboxSelected>>", self.pais_sel)
        
        self.id_label2 = ttk.Label(self.tabl2, text="Estática:")
        self.id_label2.grid(column=4, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.estatica = ttk.Entry(self.tabl2, width= 35)
        self.estatica.grid(column=4, row=1, padx=4, pady=2, columnspan = 2)
        
        self.nemip_label2 = ttk.Label(self.tabl2, text="Nem/IP Equipo:")
        self.nemip_label2.grid(column=6, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.nemip_entry2 = ttk.Entry(self.tabl2, width= 35)
        self.nemip_entry2.grid(column=6, row=1, padx=(4), pady=2, columnspan = 2)
        
        
        self.sitio_label2 = ttk.Label(self.tabl2, text="Sitio:")
        self.sitio_label2.grid(column=8, row=0, padx=4, pady=(10,2), columnspan = 2)
        self.sitio_entry2 = ttk.Entry(self.tabl2, width= 35)
        self.sitio_entry2.grid(column=8, row=1, padx=(4,20), pady=2, columnspan = 2)
        
        self.busqueda_button2 = ttk.Button(self.tabl2, text="Buscar",command = self.busqueda2)
        self.busqueda_button2.grid(column=0, row=3, pady=10,columnspan = 5)
        
        self.borrar_button2 = ttk.Button(self.tabl2, text="Borrar",command = self.borrar2)
        self.borrar_button2.grid(column=5, row=3, pady=10,columnspan = 5)
        
        
        self.tree12 = ttk.Treeview(self.tabl2,height = 5)
        self.tree12["columns"] = ("IP","VRF","DESC")
        self.tree12.heading("#0", text="IF")
        self.tree12.heading("IP", text="IP")
        self.tree12.heading("VRF", text="VRF")
        self.tree12.heading("DESC", text="DESC")
        self.tree12.column('#0', width=42, anchor='w', minwidth=0)
        self.tree12.column('IP', width=42, anchor='w', minwidth=0)
        self.tree12.column('VRF', width=42, anchor='w', minwidth=0)
        self.tree12.column('DESC', width=42, anchor='w', minwidth=0)
        self.tree12.grid(column=0, row= 5, padx=(20,5), pady=10, columnspan = 5,sticky='nsew')
        self.tree12.bind('<<TreeviewSelect>>', self.ipte)
        
        self.tree22 = ttk.Treeview(self.tabl2,height = 5)
        self.tree22["columns"] = ("IP","GRP","SITIO")
        self.tree22.heading("#0", text="NEM")
        self.tree22.heading("IP", text="IP")
        self.tree22.heading("GRP", text="GRP")
        self.tree22.heading("SITIO", text="SITIO")
        self.tree22.column('#0', width=42, anchor='w', minwidth=0)
        self.tree22.column('IP', width=42, anchor='w', minwidth=0)
        self.tree22.column('GRP', width=42, anchor='w', minwidth=0)
        self.tree22.column('SITIO', width=42, anchor='w', minwidth=0)
        self.tree22.grid(column=5, row= 5, padx=(5,20), pady=10, columnspan = 5,sticky='nsew')
        self.tree22.bind('<<TreeviewSelect>>', self.est)
        
        
        
        
        
        self.tab_control.pack(expand=1, fill='both')
        self.pack(fill=BOTH, expand=1)
    
    def ipte(self,event):
        it1 = self.tree12.index(self.tree12.focus())
        self.tree22.delete(*self.tree22.get_children())
        if len(self.res_consulta[it1])> 6:
            self.tree22.insert("","end",text = self.res_consulta[it1][4],values = (self.res_consulta[it1][5],self.res_consulta[it1][6],self.res_consulta[it1][7],))
        else:
            self.tree22.insert("","end",text = self.res_consulta[it1][2],values = (self.res_consulta[it1][3],self.res_consulta[it1][4],self.res_consulta[it1][5],))

    
    def est(self,event):
        valor_sel=self.tree22.item(self.tree22.focus(),'values')
        self.clipboard_clear()
        self.clipboard_append(valor_sel[0])
    
    def copywoa(self,event):
        #print("a")
        #print(self.bx_WO.get("1.0","end"))
        self.clipboard_clear()
        self.clipboard_append(self.bx_WO.get("1.0","end"))
    
    def insertarwo(self):
        cadena =self.bx_WO.get("1.0","end")
        db_eq.insert_wo([13,cadena.encode()])
    
    def buscar_ent(self,event):
        self.buscar()
    
    def buscar(self):
        self.borrartree()
        self.res_consulta=[]
        lst_campos = ["PAIS","IP BUSCADA","PE","IP PE","VRF","IP NE","NEM NE","IF NE","DES IF NE"]
        self.id_op = 0
        #self.lista_busqueda
        IP_BUS = self.ip_entry.get().strip()
        sitio_desc = self.desc_entry.get().strip()
        nem_ip_eq = self.nemip_entry.get().strip()
        lugar = self.sitio_entry.get().strip()
        print("pais  " + self.pais_combo.get())
        if len(IP_BUS) > 5:
            self.res_consulta = db_eq.consulta_ip_acc(IP_BUS)
            if len(self.res_consulta) > 0:
                self.id_op = 1
                lista_busqueda=[]
                lista_busqueda = self.res_consulta[0]
                for contador in range(0,9):
                    self.tree1.insert("","end",text = lst_campos[contador],values = (self.res_consulta[0][contador],))
                cade1 = "ping -vpn "+ self.res_consulta[0][4] +" " + self.res_consulta[0][1]
                cade2 = "ping vrf " + self.res_consulta[0][4] +" "+ self.res_consulta[0][1]
                cade3 = "dis int desc " + self.res_consulta[0][7]
                cade4 = "sh int "+ self.res_consulta[0][7]+" desc"
                self.tree2.insert("","end",text = "Ping Huawei",values = (cade1,))
                self.tree2.insert("","end",text = "Ping Cisco",values =  (cade2,))
                self.tree2.insert("","end",text = "Desc int Hua",values = (cade3,))
                self.tree2.insert("","end",text = "Desc int Cis",values = (cade4,))

        elif len(sitio_desc)> 2:
            self.res_consulta = db_eq.consulta_desc_if(sitio_desc, self.pais_combo.get())
            if len(self.res_consulta)> 0:
                self.id_op = 2
                for contador in range(0,len(self.res_consulta)):
                    self.tree1.insert("","end",text = self.res_consulta[contador][0],values = (self.res_consulta[contador][1],))
                    self.tree1.insert("","end",text = self.res_consulta[contador][3],values = (self.res_consulta[contador][2],))
                    self.tree1.insert("","end",text = "Sitio",values = (self.res_consulta[contador][4],))
                    self.tree1.insert("","end",text = "",values = "")

        elif len(nem_ip_eq)> 4:
            self.id_op = 3
            self.res_consulta = db_eq.consulta_eq_ip_ne(nem_ip_eq, self.pais_combo.get())
            print(self.res_consulta)
            lst_campos2=["Nemonico","IP NE","GRUPO","SITIO"]
            if len(self.res_consulta)> 0:
                for co1 in range(0,len(self.res_consulta)):
                    for contador in range(0,4):
                        self.tree1.insert("","end",text = lst_campos2[contador],values = (self.res_consulta[co1][contador],))
                    self.tree1.insert("","end",text = "",values = "")
        elif len(lugar)> 2:
            self.id_op = 4
            self.res_consulta = db_eq.consulta_eq_sitio(self.pais_combo.get(), lugar)
            print(lugar)
            lst_campos3=["Nemonico","IP","Sitio"]
            if len(self.res_consulta)> 0:
                for cc in range(0,len(self.res_consulta)):
                    for co in range(0,3):
                        self.tree1.insert("","end",text = lst_campos3[co],values = (self.res_consulta[cc][co],))
                    self.tree1.insert("","end",text = "",values = "")
        else:
            self.id_op= 0
        #self.pais.insert("",resultado_bs[0][0])
            
            #self.tabla.configure(state='readonly')
    def busqueda2(self):
        self.borrartree2()
        self.res_consulta=[]
        ip_bus = self.ip_entry2.get().strip()
        pais = self.pais_combo2.get().strip()
        ip_est = self.estatica.get().strip()
        #estatica = self.estatica.get()
        #lugar = self.sitio_entry.get()
        #if len()
        if len(ip_bus) > 5:
            self.res_consulta = db_eq.consulta_ip_p(ip_bus,pais)
            for c in range(0,len(self.res_consulta)):
                        self.tree12.insert("","end",text = self.res_consulta[c][0],values = (self.res_consulta[c][1],self.res_consulta[c][2],self.res_consulta[c][3],))
        
        elif len(ip_est) > 5:
            self.res_consulta = db_eq.consulta_est_p(ip_est,pais)
            for c in range(0,len(self.res_consulta)):
                        self.tree12.insert("","end",text = self.res_consulta[c][0],values = (self.res_consulta[c][1],))
        
        
            
        #print(self.res_consulta)
                    
                    
    def areawo_se(self,event):
        lista_tipo_wo =db_eq.consulta_tipo_wo(self.areawo_combo.get())
        lst_tip_wo=[""]
        for rec in lista_tipo_wo:
            lst_tip_wo.append(rec[1])
        self.tipowo_combo["values"] = tuple(lst_tip_wo)
        self.tipowo_combo.current(0)
        
    def wo_text(self,event):
        self.bx_WO.delete("1.0","end")
        texto_wo=db_eq.consulta_text_wo(self.tipowo_combo.current())
        print(texto_wo[0][0].decode())
        #print(texto_wo)
        #self.bx_WO.delete(0,"end")
        self.bx_WO.insert(INSERT,texto_wo[0][0].decode())
    
    def borrar(self):
        self.ip_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')
        self.nemip_entry.delete(0, 'end')
        self.sitio_entry.delete(0, 'end')
        self.pais_combo.current(0)
        self.borrartree()
        self.id_op = 0

    def borrar2(self):
        self.ip_entry2.delete(0, 'end')
        self.estatica.delete(0, 'end')
        self.nemip_entry2.delete(0, 'end')
        self.sitio_entry2.delete(0, 'end')
        self.pais_combo2.current(0)
        self.borrartree2()
        self.id_op = 0
    
    def borrartree(self):
        self.tree1.delete(*self.tree1.get_children())
        self.tree2.delete(*self.tree2.get_children())

    def borrartree2(self):
        self.tree12.delete(*self.tree12.get_children())
        self.tree22.delete(*self.tree22.get_children())

    def selectItemtree(self,event):
        curItem = self.tree.focus()
        print (curItem)
        self.clipboard_clear()
        self.clipboard_append(curItem)
        
    def selectpais(self,event):
        valor_sel=self.tree1.item(self.tree1.focus(),'values')
        if len(valor_sel)> 0:
            print(valor_sel)
            self.opcion2()
            self.clipboard_clear()
            self.clipboard_append(valor_sel)
    
    def copiar_tree1(self, event):
        if self.id_op > 0:
            indice_t = self.tree1.index(self.tree1.focus())
            print(self.id_op)
            if self.id_op == 2:
                indice2 = int(indice_t/4)
            elif self.id_op == 3:
                indice2 = int(indice_t/5)
                self.tree2.delete(*self.tree2.get_children())
            elif self.id_op == 4:
                indice2 = int(indice_t/4)
            
            self.bx_text1.delete("1.0","end")
            self.bx_text1.insert(INSERT,self.res_consulta[indice2][3]+"\n")
            self.bx_text1.insert(INSERT,self.res_consulta[indice2][0]+"\n")
            self.bx_text1.insert(INSERT,self.res_consulta[indice2][1]+"\n")
            self.clipboard_clear()
            self.clipboard_append(self.res_consulta[indice2][3]+"\n"+self.res_consulta[indice2][0]+"\n"+self.res_consulta[indice2][1]+"\n")
    
    def copiar_tree1_2(self, event):
        if self.id_op > 0:
            indice_t = self.tree1.index(self.tree1.focus())
            print(self.id_op)
            if self.id_op == 2:
                indice2 = int(indice_t/4)
            elif self.id_op == 3:
                indice2 = int(indice_t/5)
                self.tree2.delete(*self.tree2.get_children())
            elif self.id_op == 4:
                indice2 = int(indice_t/4)
            self.bx_text2.delete("1.0","end")
            self.bx_text2.insert(INSERT,self.res_consulta[indice2][3]+"\n")
            self.bx_text2.insert(INSERT,self.res_consulta[indice2][0]+"\n")
            self.bx_text2.insert(INSERT,self.res_consulta[indice2][1]+"\n")
            self.clipboard_clear()
            self.clipboard_append(self.res_consulta[indice2][3]+"\n"+self.res_consulta[indice2][0]+"\n"+self.res_consulta[indice2][1]+"\n")
    
    def copiar_exportar(self, event):
        self.res_consulta=[]
        IP_BUS = self.ip_entry.get().strip()
        sitio_desc = self.desc_entry.get().strip()
        nem_ip_eq = self.nemip_entry.get().strip()
        lugar = self.sitio_entry.get().strip()
        diccionario=None
        if len(sitio_desc)> 2:
            self.res_consulta = db_eq.consulta_desc_if(sitio_desc, self.pais_combo.get())
            if len(self.res_consulta)> 0:
                diccionario ={'Nemónico':[], 'IP':[], 'Puerto':[], 'Etiqueta':[], 'Sitio':[] }
                lsts=[[],[],[],[],[]]
                for contador in range(0, len(self.res_consulta)):
                    #print(self.res_consulta[contador])
                    lsts[0].append(self.res_consulta[contador][0])
                    lsts[1].append(self.res_consulta[contador][1])
                    lsts[2].append(self.res_consulta[contador][2])
                    lsts[3].append(self.res_consulta[contador][3])
                    lsts[4].append(self.res_consulta[contador][4])
                diccionario['Nemónico'] = lsts[0]
                diccionario['IP'] = lsts[1]
                diccionario['Puerto'] = lsts[2]
                diccionario['Etiqueta'] = lsts[3]
                diccionario['Sitio'] = lsts[4]
                    #self.tree1.insert("","end",text = self.res_consulta[contador][0],values = (self.res_consulta[contador][1],))
                    #self.tree1.insert("","end",text = self.res_consulta[contador][3],values = (self.res_consulta[contador][2],))
                    #self.tree1.insert("","end",text = "Sitio",values = (self.res_consulta[contador][4],))
                    #self.tree1.insert("","end",text = "",values = "")
        elif len(nem_ip_eq)> 4:
            self.res_consulta = db_eq.consulta_eq_ip_ne(nem_ip_eq, self.pais_combo.get())
            diccionario ={'Nemónico':[], 'IP':[],'Sitio':[],'Grupo': [] }
            lsts=[[], [], [], []]
            if len(self.res_consulta)> 0:
                for co1 in range(0, len(self.res_consulta)):
                    lsts[0].append(self.res_consulta[co1][0])
                    lsts[1].append(self.res_consulta[co1][1])
                    lsts[2].append(self.res_consulta[co1][3])
                    lsts[3].append(self.res_consulta[co1][2])
                diccionario['Nemónico'] = lsts[0]
                diccionario['IP'] = lsts[1]
                diccionario['Sitio'] = lsts[2]
                diccionario['Grupo'] = lsts[3]
                    #for contador in range(0,4):
                    #    self.tree1.insert("","end",text = lst_campos2[contador],values = (self.res_consulta[co1][contador],))
                    #self.tree1.insert("","end",text = "",values = "")
        elif len(lugar)> 2:
            self.res_consulta = db_eq.consulta_eq_sitio(self.pais_combo.get(), lugar)
            diccionario ={'Nemónico':[], 'IP':[],'Sitio':[],'Grupo': [] }
            lsts=[[], [], [], []]
            if len(self.res_consulta)> 0:
                for cc in range(0,len(self.res_consulta)):
                    lsts[0].append(self.res_consulta[cc][0])
                    lsts[1].append(self.res_consulta[cc][1])
                    lsts[2].append(self.res_consulta[cc][2])
                    lsts[3].append(self.res_consulta[cc][4])
                diccionario['Nemónico'] = lsts[0]
                diccionario['IP'] = lsts[1]
                diccionario['Sitio'] = lsts[2]
                diccionario['Grupo'] = lsts[3]
            
                        #self.tree1.insert("","end",text = lst_campos3[co],values = (self.res_consulta[cc][co],))
                    #self.tree1.insert("","end",text = "",values = "")
        llave = []
        for key in diccionario.keys():
            llave.append(key)
        print(diccionario)
        if len(diccionario) > 0:            
            df = pandas.DataFrame(diccionario)
            df = df[llave]
            x = datetime.datetime.now()
            nombre_archivo = 'Información_'+ x.strftime("%d%m%y_%H%M") +'.xlsx'
            writer =ExcelWriter(nombre_archivo)
            df.to_excel(writer, 'Datos', index=False)
            writer.save()
            if os.stat(nombre_archivo).st_size > 400:#valida peso
                os.startfile(nombre_archivo)#si es un archivo con informacion lo abre
            else:
                os.remove(nombre_archivo) 
    
    def wo_rep1(self, event):
        self.clipboard_clear()
        self.clipboard_append(self.bx_text1.get("1.0","end"))
        print(self.bx_text1.get("1.0","end"))
    #self.bx_text1.bind("<KeyRelease-Escape>", self.wo_rep1)
    
    def select2(self,event):
        valor_sel=self.tree2.item(self.tree2.focus(),'values')
        encabezado_sel=self.tree2.item(self.tree2.focus(),'text')
        print(encabezado_sel)
        if len(valor_sel)> 0:
            self.clipboard_clear()
            if self.id_op == 3:
                print(encabezado_sel)
                self.clipboard_append(encabezado_sel)
            else:
                print(valor_sel)
                self.clipboard_append(valor_sel[0])
    
    def opcion2(self):
        indice_t = self.tree1.index(self.tree1.focus())
        print(self.id_op)
        if self.id_op == 2:
            indice2 = int(indice_t/4)
            self.tree2.delete(*self.tree2.get_children())
            cade3 = "dis int desc " + self.res_consulta[indice2][2]
            cade4 = "sh int "+ self.res_consulta[indice2][2]+" desc"
            self.tree2.insert("","end",text = "Desc int Hua",values = (cade3,))
            self.tree2.insert("","end",text = "Desc int Cis",values = (cade4,))
        elif self.id_op == 3:
            indice2 = int(indice_t/5)
            self.tree2.delete(*self.tree2.get_children())
            res1 = db_eq.get_if_equipos(self.res_consulta[indice2][4])
            for a in res1:
                self.tree2.insert("","end",text = a[2],values = (a[3],))
        elif self.id_op == 4:
            indice2 = int(indice_t/4)
            #get_if_equipos
        #print(self.res_consulta[])
    
    def handle_click(self,event):
        print(self.tabla.get())
 
if __name__ == "__main__":
    root = Tk()
    #root.resizable(0,0)
    ej = App()
    root.mainloop()
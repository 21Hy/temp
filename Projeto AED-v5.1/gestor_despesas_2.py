import tkinter as tk
from tkinter import ttk

class Ver():
    def __init__(self):
        self.gestor_despesas()
        
    def modificar_geometria(self, largura, altura,widget):
        # geometria centrada da janela
        w=largura; h=altura
        screen_width = widget.winfo_screenwidth()
        screen_height = widget.winfo_screenheight()
        x = (screen_width/2)-(w/2)
        y = (screen_height/2-50)-(h/2)
        widget.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def gestor_despesas(self):
        self.master = tk.Tk()
        self.master.resizable(False,False)
        self.modificar_geometria(1200,600,self.master)
        self.master.config(bg='light blue')

        # defenir a grid:
        for index in [0,1,2,3,4,5,6,7]:
            self.master.columnconfigure(index,weight= 1,uniform='a')
            self.master.rowconfigure(index,weight=1,uniform='a')


        #.................. Tabela/Gráfico Widget
        self.tabela_grafico_book = ttk.Notebook(self.master)
        self.tabela_grafico_book.grid(
            row=0,rowspan=8,column=0,columnspan=6,padx=(10, 10),pady=(20, 10),sticky="nsew"
        )
        #.................. gráfico
        self.grafico_widget = ttk.Frame(
            self.tabela_grafico_book, padding=(10, 10)
        )
        self.tabela_grafico_book.add(self.grafico_widget, text='Gráfico')
        self.grafico_widget_label_1 = ttk.Label(
            self.grafico_widget,text='Estou aqui'
        )
        self.grafico_widget_label_1.pack()

        #.................. Tabela
        self.tabela_widget = ttk.Frame(
            self.tabela_grafico_book, padding=(10, 10)
        )
        self.tabela_grafico_book.add(self.tabela_widget, text='Tabela')
        
        #.................. User Widget
        self.user_widget = ttk.Frame(self.master)
        self.user_widget.grid(
            row=0,rowspan=8,column=6,columnspan=2,padx=(10, 10),pady=(20, 10),sticky="nsew"
        )
        self.user_widget_b= tk.Button(
            self.user_widget,text='estou aqui', command=self.adicionar_despesas
        )
        self.user_widget_b.pack()
        self.user_widget_b2= tk.Button(
            self.user_widget,text='estou aqui', command=self.adicionar_limite_mensal
        )
        self.user_widget_b2.pack()
        self.master.mainloop()

    def adicionar_despesas(self):
        self.top= tk.Toplevel()
        self.modificar_geometria(300,300,self.top)
        # defenir a grid:
        for index in [0,1]:
            self.top.columnconfigure(index,weight= 1,uniform='a')
        for index in [0,1,2,3,4,5,6]:
            self.top.rowconfigure(index,weight=1,uniform='a')
        # Frame 1
        self.top_frame1 = ttk.Frame(
            self.top, style='self.top_frame1.TFrame'
        )
        self.top_frame1.grid(
            row=0,rowspan=1,column=0,columnspan=2,sticky="nsew"
        )
        self.top_frame1_label = ttk.Label(
            self.top_frame1,text='Categoria: ',font=('Arial', 12),background ='#156969'
        )
        self.top_frame1_label.grid(
            row=0,column=0,sticky="nsew"
        )
        self.top_frame1_entry = ttk.Combobox(
            self.top_frame1,font=('Arial', 12)
        )
        self.top_frame1_entry.grid(
            row=0,column=2,sticky="sew"
        )
        # Frame 2
        self.top_frame2 = ttk.Frame(
            self.top, style='self.top_frame2.TFrame'
        )
        self.top_frame2.grid(
            row=1,rowspan=1,column=0,columnspan=2,sticky="nsew"
        )
        self.top_frame2_label = ttk.Label(
            self.top_frame2,text='Data: ',font=('Arial', 12),background ='#156969'
        )
        self.top_frame2_label.grid(
            row=0,column=0,sticky="nsew",ipadx=18
        )
        self.top_frame2_entry = ttk.Entry(
            self.top_frame2,font=('Arial', 12)
        )
        self.top_frame2_entry.grid(
            row=0,column=2,sticky="sew",ipadx=9
        )
        # Frame 3
        self.top_frame3 = ttk.Frame(
            self.top, style='self.top_frame3.TFrame'
        )
        self.top_frame3.grid(
            row=2,column=0,columnspan=2,sticky="nsew"
        )
        self.top_frame3_label = ttk.Label(
            self.top_frame3,text='Valor(€):',font=('Arial', 12),background ='#156969'
        )
        self.top_frame3_label.grid(
            row=0,column=0,sticky="nsew",ipadx=9
        )
        self.top_frame3_entry = ttk.Entry(
            self.top_frame3,font=('Arial', 12)
        )
        self.top_frame3_entry.grid(
            row=0,column=2,sticky="sew",ipadx=9
        )
        # Frame 4
        self.top_frame4 = ttk.Frame(
            self.top, style='self.top_frame4.TFrame'
        )
        self.top_frame4.grid(
            row=3,column=0,rowspan=2,columnspan=2,sticky="nsew"
        )
        self.top_frame4_label = ttk.Label(
            self.top_frame4,text='Descrição:',font=('Arial', 12),background ='#156969'
        )
        self.top_frame4_label.grid(
            row=0,column=0,sticky="sw",pady=(20,0)
        )
        # Frame 5
        self.top_frame5 = ttk.Frame(
            self.top, style='self.top_frame1.TFrame'
        )
        self.top_frame5.grid(
            row=4,column=0,rowspan=1,columnspan=2,sticky="nsew"
        )
        self.top_frame5_entry = tk.Text(
            self.top_frame5
        )
        self.top_frame5_entry.grid(
            row=0,column=0,sticky="n"
        )
        # Frame 6
        self.top_frame6 = tk.Frame(
            self.top,bg='#518585'
        )
        self.top_frame6.grid(
            row=5,column=0,rowspan=1,columnspan=2,sticky="nsew"
        )
        self.top_frame6_button = tk.Button(
            self.top_frame6, text='Adicionar',font=('Arial', 12),command=self.eliminar
        )
        self.top_frame6_button.pack(ipadx=102, ipady=5,pady=5)
        # Frame 7
        self.top_frame7 = tk.Frame(
            self.top,bg='#518585'
        )
        self.top_frame7.grid(
            row=6,column=0,rowspan=1,columnspan=2,sticky="nsew"
        )
        self.top_frame7_button = tk.Button(
            self.top_frame7, text='Voltar',font=('Arial', 12),command=self.top.destroy
        )
        self.top_frame7_button.pack(ipadx=115, ipady=5,pady=5)
        
        #.................. Widegts Styling
        self.style = ttk.Style()
        self.style.configure('self.top_frame1.TFrame',background ='#518585')
        self.style.configure('self.top_frame2.TFrame',background ='#518585')
        self.style.configure('self.top_frame3.TFrame',background ='#518585')
        self.style.configure('self.top_frame4.TFrame',background ='#518585')
        self.style.configure('self.top_frame6.TFrame',background ='#518585')
        self.style.configure('self.top_frame7.TFrame',background ='#518585')


    def eliminar(self):
        self.top_frame1_entry.delete(0, 'end')
        self.top_frame2_entry.delete(0, 'end')
        self.top_frame3_entry.delete(0, 'end')
        self.top_frame5_entry.delete(0, 'end')

    def adicionar_limite_mensal(self):
        self.top2= tk.Toplevel()
        self.modificar_geometria(400,200,self.top2)

        self.slide = tk.Scale(self.top2)
        self.slide.pack()
        self.top2_label = ttk.Label(self.top2, text=self.slide.get())
        self.top2_label.pack()








Ver()

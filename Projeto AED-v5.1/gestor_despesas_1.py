import tkinter as tk
from tkinter import ttk

class Ver():
    def __init__(self):
        self.gestor_despesas()
        
    def modificar_geometria(self, largura, altura):
        # geometria centrada da janela
        w=largura; h=altura
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width/2)-(w/2)
        y = (screen_height/2)-(h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def gestor_despesas(self):
        self.master = tk.Tk()
        self.master.resizable(False,False)
        self.modificar_geometria(1200,500)
        self.master.config(bg='#A9907E')

        # defenir a grid:
        for index in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
            self.master.columnconfigure(index,weight= 1,uniform='a')
            self.master.rowconfigure(index,weight=1,uniform='a')


        #.................. Tabela/Gráfico Widget
        self.tabela_grafico_book = ttk.Notebook(self.master)
        self.tabela_grafico_book.grid(
            row=0,rowspan=10,column=2,columnspan=8,padx=(10, 10),pady=(20, 10),sticky="nsew"
        )
        #......... gráfico
        self.grafico_widget = ttk.Frame(
            self.tabela_grafico_book, padding=(10, 10)
        )
        self.tabela_grafico_book.add(self.grafico_widget, text='Gráfico')
        self.grafico_widget_label_1 = ttk.Label(
            self.grafico_widget,text='Estou aqui'
        )
        self.grafico_widget_label_1.pack()

        #......... tabela
        self.tabela_widget = ttk.Frame(
            self.tabela_grafico_book, padding=(10, 10)
        )
        self.tabela_grafico_book.add(self.tabela_widget, text='Tabela')

        #.................. Filtros Widget
        self.filtros_widget = ttk.LabelFrame(text="Filtros", padding=(20, 10))
        self.filtros_widget.grid(
            row=0,rowspan=14,column=0,columnspan=2,padx=(10, 10),pady=(20, 10),sticky="nsew"
        )
        self.filtros_widget_radio_1 = ttk.Radiobutton(
            self.filtros_widget, text="Decresc.", value=1
        )
        self.filtros_widget_radio_1.grid(pady=5, sticky='nswe')
        self.filtros_widget_radio_2 = ttk.Radiobutton(
            self.filtros_widget, text="Cresc.", value=1
        )
        self.filtros_widget_radio_2.grid(pady=5,sticky='nswe')
        self.filtros_widget_radio_3 = ttk.Radiobutton(
            self.filtros_widget, text="A...Z", value=1
        )
        self.filtros_widget_radio_3.grid(pady=5,sticky='nswe')
        self.filtros_widget_button_1 = ttk.Button(
            self.filtros_widget, text='Enter'
        )
        self.filtros_widget_button_1.grid(pady=5,sticky="w")
        self.filtros_widget_label_1 = ttk.Label(
            self.filtros_widget, text='Categoria:'
        )
        self.filtros_widget_label_1.grid(pady=5,sticky='w')
        self.filtros_widget_entry_1 = ttk.Entry(self.filtros_widget)
        self.filtros_widget_entry_1.grid(pady=5,sticky="w")
        self.filtros_widget_label_2 = ttk.Label(
            self.filtros_widget, text='Data:'
        )
        self.filtros_widget_label_2.grid(pady=5,sticky='w')
        self.filtros_widget_entry_2 = ttk.Entry(self.filtros_widget)
        self.filtros_widget_entry_2.grid(pady=5,sticky="w")
        self.filtros_widget_button_2 = ttk.Button(
            self.filtros_widget, text='Enter'
        )
        self.filtros_widget_button_2.grid(pady=5,sticky="nesw")



        #.................. Despesas Widget
        self.despesas_widget = ttk.Frame(self.master, style='self.despesas_widget.TFrame')
        self.despesas_widget.grid(
            row=0,rowspan=14,column=10,columnspan=4,padx=(10, 10),pady=(20, 10),sticky="nsew"
        )
        self.despesas_widget_label_1 = ttk.Label(
            self.despesas_widget,text='Adicionar Despesas',font=('Arial', 18)
        )
        self.despesas_widget_label_1.pack(pady=5)
        self.despesas_widget_label_2 = ttk.Label(
            self.despesas_widget,text='Categoria:',font=('Arial', 12)
        )
        self.despesas_widget_label_2.pack(pady=10)

        self.despesas_widget_entry_1 = ttk.Combobox(
            self.despesas_widget,font=('Arial', 12)
        )
        self.despesas_widget_entry_1.pack(pady=3)
        self.despesas_widget_label_3 = ttk.Label(
            self.despesas_widget,text='Valor(€):',font=('Arial', 12)
        )
        self.despesas_widget_label_3.pack(pady=5)
        self.despesas_widget_entry_2 = ttk.Entry(
            self.despesas_widget,font=('Arial', 12)
        )
        self.despesas_widget_entry_2.pack(pady=3)
        self.despesas_widget_label_4 = ttk.Label(
            self.despesas_widget,text='Data:',font=('Arial', 12)
        )
        self.despesas_widget_label_4.pack(pady=5)
        self.despesas_widget_entry_3 = ttk.Entry(
            self.despesas_widget,font=('Arial', 12)
        )
        self.despesas_widget_entry_3.pack(pady=3)
        self.despesas_widget_label_5 = ttk.Label(
            self.despesas_widget,text='Descrição:',font=('Arial', 12)
        )
        self.despesas_widget_label_5.pack(pady=5)
        self.despesas_widget_entry_4 = tk.Text(
            self.despesas_widget,font=('Arial', 10),width=26, height=2
        )
        self.despesas_widget_entry_4.pack(pady=3)
        self.despesas_widget_button_1 = ttk.Button(
            self.despesas_widget, text='Enter'
        )
        self.despesas_widget_button_1.pack(pady=5, ipadx=55)
        #..... Limite Mensal
        self.despesas_widget_frame1 = ttk.LabelFrame(
            self.despesas_widget,text='Limite Mensal',width=200,height=150,padding=(10, 10)
        )
        self.despesas_widget_frame1.pack(pady=5)
        self.despesas_widget_label_6 = ttk.Label(
            self.despesas_widget_frame1,text='Valor(€):',font=('Arial', 12)
        )
        self.despesas_widget_label_6.grid(sticky='w')
        self.despesas_widget_entry_5 = ttk.Entry(  
            self.despesas_widget_frame1,font=('Arial', 10)
        )
        self.despesas_widget_entry_5.grid(sticky='e')
        self.despesas_widget_button_2 = ttk.Button(
            self.despesas_widget_frame1, text='Enter'
        )
        self.despesas_widget_button_2.grid(sticky="wnse")



        #.................. Dicas Widget
        self.dicas_widget = ttk.LabelFrame(text="Dicas", padding=(20, 10))
        self.dicas_widget.grid(
            row=10,rowspan=4,column=2,columnspan=8,padx=(10, 10),pady=(20, 10),sticky="nsew"
        )
        self.dicas_widget_label_1 = ttk.Label(
            self.dicas_widget,text='Estou aqui'
        )
        self.dicas_widget_label_1.pack()

        #.................. Widegts Styling
        self.style = ttk.Style()
        self.style.configure('self.despesas_widget.TFrame', background = '#675D50')

        self.master.mainloop()

Ver()
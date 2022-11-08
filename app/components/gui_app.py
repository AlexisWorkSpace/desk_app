import tkinter as tk
from tkinter import ttk

def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu = menu_bar, width=300, height=300)
    
    main_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(Label = 'Inicio', menu = main_menu)

    main_menu.add_command(Label = 'Crear registro DB')
    main_menu.add_command(Label = 'Eliminar registro DB')
    main_menu.add_command(Label = 'Salir', command = root.destroy)

    menu_bar.add_cascade(menu = 'Consultas')
    menu_bar.add_cascade(menu = 'Configuracion')
    menu_bar.add_cascade(menu = 'Ayuda')

    '''
    para agregar comandos a la cascada de de cada menu se debe utilizar el comando .add_command()

    ej: main_menu.add_command(Label = 'lo que se queira utilizar')
    '''

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=300)
        self.root = root
        self.pack()

        self.elem_field()
        self.disabled_fields()
        self.data_tab()

    def elem_field(self):
         self.name_label = tk.Label(self, text = '''nombre de lo que ira en la base de datos''')
         self.name_label.config(font = ('Arial', 12, 'bold'))
         self.name_label.grid(
                 row = 0, 
                 column = 0, 
                 padx = 10, 
                 pady = 10)

         self.sec_name_label = tk.Label(self, text = '''nombre de lo que ira en la base de datos''')
         self.sec_name_label.config(font = ('Arial', 12, 'bold'))
         self.sec_name_label.grid(
                 row = 1, 
                 column = 0, 
                 padx = 10, 
                 pady = 10)

         self.third_name_label = tk.Label(self, text = '''nombre de lo que ira en la base de datos''')
         self.third_name_label.config(font = ('Arial', 12, 'bold'))
         self.third_name_label.grid(
                 row = 2, 
                 column = 0, 
                 padx = 10, 
                 pady = 10)

         self.name = tk.StringVar()
         self.entry_name = tk.Entry(self, textvariable = self.name)
         self.entry_name.config(
                 width = 50,
                 font = ('Arial', 12))
         self.entry_name.grid(
                 row = 0, 
                 column = 1, 
                 padx = 10, 
                 pady = 10,
                 columnspan = 2)

         self.sec_name = tk.StringVar()
         self.sec_entry_name = tk.Entry(self, textvariable = self.sec_name)
         self.sec_entry_name.config(
                 width = 50, 
                 font = ('Arial', 12))
         self.sec_entry_name.grid(
                 row = 1, 
                 column = 1, 
                 padx = 10, 
                 pady = 10,
                 columnspan = 2)

         self.third_name = tk.StringVar()
         self.third_entry_name = tk.Entry(self, textvariable = self.third_name)
         self.third_entry_name.config(
                 width = 50, 
                 font = ('Arial', 12))
         self.third_entry_name.grid(
                 row = 2, 
                 column = 1, 
                 padx = 10, 
                 pady = 10,
                 columnspan = 2)

         self.new_button = tk.Button(self, text = 'Nuevo elemento', command = self.enable_fields)
         self.new_button.config(
                 width = 20, 
                 font = ('Arial', 12, 'bold'), 
                 fg = '#FFFFFF', 
                 bg = '#00FF00', 
                 cursor = 'hand2'
                 activebackground = '#35BD6F')
         self.new_button.grid(
                 row = 3, 
                 column = 0, 
                 padx = 10, 
                 pady =10)

         self.save_button = tk.Button(self, text = 'guardar elemento', command = self.data_upload)
         self.save_button.config(
                 width = 20, 
                 font = ('Arial', 12, 'bold'), 
                 fg = '#FFFFFF', 
                 bg = '#FF0000', 
                 cursor = 'hand2'
                 activebackground = '#3586DF')
         self.save_button.grid(
                 row = 3, 
                 column = 1, 
                 padx = 10, 
                 pady =10)

         self.cancel_button = tk.Button(self, text = 'Cancelar', command = self.disabled_fields)
         self.cancel_button.config(
                  width = 20, 
                 font = ('Arial', 12, 'bold'), 
                 fg = '#FFFFFF', 
                 bg = '#0000FF', 
                 cursor = 'hand2'
                 activebackground = '#E15370')
         self.cancel_button.grid(
                 row = 3, 
                 column = 2, 
                 padx = 10, 
                 pady =10)

    def enable_fields(self):
        self.entry_name.config(state = 'normal')
        self.sec_entry_name.config(state = 'normal')
        self.third_entry_name.config(state = 'normal')

        self.delete_button.config(state = 'normal')
        self.cancel_button.config(state = 'normal')

  

    def disabled_fields(self):
        self.name.set('')
        self.sec_name.set('')
        self.third_name.set('')

        self.entry_name.config(state = 'disabled')
        self.sec_entry_name.config(state = 'disabled')
        self.third_entry_name.config(state = 'disabled')

        self.delete_button.config(state = 'disabled')
        self.cancel_button.config(state = 'disabled')

    def data_upload(self):

        self.disabled_fields()

    def data_tab(self):
        self.table = ttk.Treeview(
                self, 
                column = ('name', 'sec_name', 'third_name'))
        self.table.grid(row = 4, column = 0, columnspan = 4)
        
        self.table.heading('#0', text = 'ID')
        self.table.heading('#1', text = 'name')
        self.table.heading('#2', text = 'sec_name')
        self.table.heading('#3', text = 'third_name')

        self.tabla.insert('', 0, text = '1', 
                values = ('algo', 'otra cosa', 'otra mas'))



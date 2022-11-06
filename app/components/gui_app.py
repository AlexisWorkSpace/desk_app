import tkinter as tk

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

    def elem_field(self):
         self.name_label = tk.Label(self, text = '''nombre de lo que ira en la base de datos''')
         self.name_label.config(font = ('Arial', 12, 'bold'))
         self.name_label.grid(row = 0, column = 0, padx = 10, pady = 10)


         self.sec_name_label = tk.Label(self, text = '''nombre de lo que ira en la base de datos''')
         self.sec_name_label.config(font = ('Arial', 12, 'bold'))
         self.sec_name_label.grid(row = 1, column = 0, padx = 10, pady = 10)

         self.third_name_label = tk.Label(self, text = '''nombre de lo que ira en la base de datos''')
         self.third_name_label.config(font = ('Arial', 12, 'bold'))
         self.third_name_label.grid(row = 2, column = 0, padx = 10, pady = 10)

         self.entry_name = tk.Entry(self)
         self.entry_name.config(width = 50, state = 'disabled', font = ('Arial', 12))
         self.entry_name.grid(row = 0, column = 1, padx = 10, pady = 10)

         self.sec_entry_name = tk.Entry(self)
         self.sec_entry_name.config(width = 50, state = 'disabled', font = ('Arial', 12))
         self.sec_entry_name.grid(row = 1, column = 1, padx = 10, pady = 10)

         self.third_entry_name = tk.Entry(self)
         self.third_entry_name.config(width = 50, state = 'disabled', font = ('Arial', 12))
         self.third_entry_name.grid(row = 2, column = 1, padx = 10, pady = 10)

         self.new_button = tk.Button(self, text = 'Nuevo elemento')
         self.new_button.config(width = 20, font = ('Arial', 12, 'bold'), fg = 'white', bg = '#00FF00')
         self.new_button.grid(row = 4, column = 0, padx = 10m pady =10)




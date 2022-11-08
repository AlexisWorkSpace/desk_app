from .db_connect import Connection
from tkinter import messagebox

def create_tab():
    con = Connection()

    sql =   '''
            CREATE TABLE database(
                id_db INTEGER,
                name VARCHAR(100),
                sec_name VARCHAR(100),
                third_name VARCHAR(100)

                PRIMARY KEY(id_db AUTOINCREMENT)
            )
            '''

    try: 
        con.cursor.execute(sql)
        con.close_db()
        title = 'Crear registro'
        message = 'Tabla creada correctamente'
        messagebox.showinfo(title, message)
    except: 
        title = 'Crear registro'
        message = 'Tabla creada previamente'
        messagebox.showwarning(title, message)


def delete_tab():
    con = Connection()

    sql = 'DROP TABLE'

    try:
        con.cursor.execute(sql)
        con.close_db()
        con.cursor.execute(sql)
        con.close_db()
        title = 'Borrar registro'
        message = 'Tabla eliminada correctamente'
        messagebox.showinfo(title, message)
    except:
        title = 'Borrar registro'
        message = 'Tabla ya eliminada previamente'
        messagebox.showerror(title, message)

class DB:
    def __init__(self, name, sec_name, third_name):
        self.id_db = None
        self.class_name = name
        self.class_sec_name = sec_name
        self.class_third_name = third_name

    def __str__(self):
        return f'DB[{self.class_name}, {self.class_sec_name, }, {self.class_third_name}]'

def save(db):
    con = Connection()

    sql =  f"""INSERT INTO db (name, sec_name, third_name)
               VALUES('{db.class_name}', '{db.class_sec_name}', '{db.class_third_name}')
            """

    try:
        con.cursor.execute(sql)
        con.close_db()
    except:
        title = 'coneccion al registro'
        message = 'registro no creado'
        messagebox.showerror(title, message)


import tkinter as tk
from components.gui_app import Frame

def main():
    root = tk.Tk() # esta clase generara la interfaz de la aplicacion

    root.title('[+] inserte titulo de aplicacion') # modifica el titlulo de la aplicacion
    root.iconbitmap(''' aqui se debe especificar la ruta del icono, el mismo se alojara en la carpeta assets''') # metodo capaz de invocar el incono de la aplicacion
    # el siguiente metodo permitira o negara la odificacion del tamaño de la ventana
    # los parametros otorgados a la funcion indicaran si se puede o no modificar lo mismo
    # en caso de ser .resizable(0, 0) no se podra modificar el tamaño de la app, en caso de ser (1, 0) se podra modificar solo hacia los lados
    # en caso de ser (0, 1), solo podra modificarse de arriba a abajo, y en caso de ser (1, 1) se podra modificar en todas direcciones
    root.resizable(1, 1)

    app = Frame(root = root)

    root.mainloop() # esto permitira que la aplicacion se mantega corriendo

if __name__ == '__main__':
    main()

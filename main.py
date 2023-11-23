import tkinter as tk

class Gui(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Inventario de invernadero")
        self.geometry("400x300")

        # Crea un marco principal para los checkboxes
        checkbox_container = tk.Frame(self)
        checkbox_container.grid(row=0, column=0, columnspan=3, rowspan=2, padx=10, pady=10)

        # Crea las variables de control para los checkboxes
        self.zanahoria_var = tk.IntVar()
        self.papa_var = tk.IntVar()
        self.pimenton_var = tk.IntVar()
        self.lechuga_var = tk.IntVar()
        self.tomate_var = tk.IntVar()
        self.albahaca_var = tk.IntVar()

        # Crea los checkboxes para cada cultivo dentro de un marco con fondo gris y borde negro
        self.create_checkbox(checkbox_container, "Zanahoria", 0, 0, self.zanahoria_var)
        self.create_checkbox(checkbox_container, "Papa", 0, 1, self.papa_var)
        self.create_checkbox(checkbox_container, "Pimentón", 0, 2, self.pimenton_var)
        self.create_checkbox(checkbox_container, "Lechuga", 1, 0, self.lechuga_var)
        self.create_checkbox(checkbox_container, "Tomate", 1, 1, self.tomate_var)
        self.create_checkbox(checkbox_container, "Albahaca", 1, 2, self.albahaca_var)

        # Crea los botones para guardar y salir
        self.guardar_button = tk.Button(self, text="Guardar", command=self.guardar)
        self.salir_button = tk.Button(self, text="Salir", command=self.quit)

        # Coloca los botones en la ventana
        self.guardar_button.grid(row=2, column=0, columnspan=3)
        self.salir_button.grid(row=3, column=0, columnspan=3)

    def create_checkbox(self, container, text, row, column, var):
        checkbox_frame = tk.Frame(container, bg="gray", bd=2, relief=tk.SOLID)  # Fondo gris, borde negro
        checkbox_frame.grid(row=row, column=column, padx=5, pady=5, sticky="w")

        checkbox = tk.Checkbutton(checkbox_frame, text=text, variable=var, bg="gray", bd=0, highlightthickness=0)
        checkbox.configure(borderwidth=0, indicatoron=0, width=len(text)+2, height=2, relief=tk.SOLID, overrelief=tk.RAISED)
        checkbox.pack(side=tk.LEFT)

    def guardar(self):
        zanahoria = self.zanahoria_var.get()
        papa = self.papa_var.get()
        pimenton = self.pimenton_var.get()
        lechuga = self.lechuga_var.get()
        tomate = self.tomate_var.get()
        albahaca = self.albahaca_var.get()

        # Imprime los valores en la consola
        print("Zanahoria:", zanahoria)
        print("Papa:", papa)
        print("Pimentón:", pimenton)
        print("Lechuga:", lechuga)
        print("Tomate:", tomate)
        print("Albahaca:", albahaca)

if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
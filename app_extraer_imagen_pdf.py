import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.messagebox import showerror, showinfo
from archivoDAO import ArchivoDAO
from archivo import Archivo


class App(tk.Tk):
    COLOR_VENTANA = '#221831'
    

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configudar_grid()
        self.mostrar_formulario()
        self.mostrar_titulo()


    def configurar_ventana(self):
        self.geometry('500x300')
        self.resizable(0,0)
        self.title('Extraer Imagenes de un pdf')
        self.configure(background=self.COLOR_VENTANA)
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')

    def configudar_grid(self):
        self.grid_columnconfigure(0,weight=1)

    def mostrar_titulo(self):
        titulo = ttk.Label(self, text= "APP EXTRAER IMAGENES DE PDF", foreground='#d3d7e7', font=('Arial', 20),background=self.COLOR_VENTANA)
        titulo.grid(column=0,row=0, pady= 30)

        
    def mostrar_formulario(self):
        ruta_l = ttk.Label(self, background=self.COLOR_VENTANA, foreground='#d3d7e7',text='Busca la ruta del archivo aqui:', font=('Arial',11))
        self.boton_buscar = ttk.Button(self, text='Buscar', command= self.buscar)

        self.ruta_e = ttk.Entry(self, width=60, background='#99b3c6')
        procesar = ttk.Button(self,text='Procesar', command=self.procesar,)

        # mostrar los componentes crreados en el grid
        ruta_l.grid(column=0,row=1,pady=10)
        self.boton_buscar.grid(column=0, row=2)
        self.ruta_e.grid(column=0,row=3,pady=10)
        procesar.grid(column=0, row=4, pady= 20)

        self.estilos.configure('TButton',background='#465779', foreground='#d3d7e7')
        self.estilos.map('TButton',background=[('active','#d3d7e7')], foreground=[('active','#221831')])


    def procesar(self):
        ArchivoDAO.existe_carpeta()
        ruta = self.ruta_e.get()
        try:
            if ruta is not None:
                archivo = Archivo(pdf_path=ruta)
                ArchivoDAO.extraer(archivo)
                showinfo(title='Exito!!', message='Se extrajeron las imagenes del archivo')
            else:
                showerror(title='Error!!', message='No se ha seleccionado el archivo')
        except:
            showerror(title='Error!!', message='La ruta del archivo no es valida')
            self.limpiar_ruta()

    def buscar(self):
        self.limpiar_ruta()
        self.ruta_c = filedialog.askopenfilename(title='Busca el archivo', initialdir=r'C:\Users\BRAYA\Downloads', filetypes=(('Archivos pdf','*.pdf'),))
        ruta = self.ruta_c
        self.ruta_e.insert(0,ruta)

    def limpiar_ruta(self):
        self.ruta_e.delete(0,tk.END)
        

if __name__ == '__main__':
    app = App()
    app.mainloop()

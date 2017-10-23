import tkinter as tk
import time
from datetime import datetime
import tkinter.messagebox as tkm
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog

class Janela_Principal():
    
    def __init__(self):
        
        self.app_config = dict()
        self.app_config['width_button'] = 200
        self.app_config['height_button'] = 150
        self.app_config['window_xpos'] = 100
        self.app_config['window_ypos'] = 100
        
        window_width  = self.app_config['width_button'] * 1
        window_height = self.app_config['height_button'] * 3

        self.window = tk.Tk()
        self.window.geometry("{}x{}+{}+{}".format(window_width, 
                                                  window_height, 
                                                  self.app_config['window_xpos'], 
                                                  self.app_config['window_ypos']))
        self.window.title("BruNardo")
        self.window.resizable(False, False)
    
        # Geometria da pagina
        self.window.rowconfigure(0, minsize = window_height)
        self.window.columnconfigure(0, minsize = window_height)
        
        # Menu Principal
        self.menu_principal = Menu_Principal(self)
    
        #Emissor
        self.emissor_window = Emissor_window(self)
    
        #Receptor
        self.receptor_window = Receptor_window(self)
    
        # Iniciar menu
        self.menu_principal.mostrar()
                
    def mostrar_emissor(self):
        self.emissor_window.mostrar()
        
    def mostrar_receptor(self):
        self.receptor_window.mostrar()
        
    def iniciar(self):
        self.window.mainloop()

class Menu_Principal():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window1 = tk.Frame(self.janela_principal.window)
        self.window1.grid(row = 0, column = 0, sticky = "nsew")
        self.window1.configure(background = 'white')
        
        # Geometria da pagina        
        self.window1.rowconfigure(0, minsize = self.janela_principal.app_config['height_button'])
        self.window1.rowconfigure(1, minsize = self.janela_principal.app_config['height_button'])
        self.window1.rowconfigure(2, minsize = self.janela_principal.app_config['height_button'])

        self.window1.columnconfigure(0, minsize = self.janela_principal.app_config['width_button'])
                
        #self.Logo = ImageTk.PhotoImage(Image.open("./interface_imgs/Logo.png"))
        self.Logo_label = tk.Label(self.window1)
        self.Logo_label.grid(row = 0, column = 0, sticky = "nsew",height = 4, width = 30)
        
        self.button_Emissor = tk.Button(self.window1, text = "Enviar Texto",background = "blue", height = 4, width = 30)        
        self.button_Emissor.grid(row = 1, column = 0)
        self.button_Emissor.configure(command = self.rodaEmissor)

        self.button_Receptor = tk.Button(self.window1, text = "Receber Texto",background = "blue", height = 4, width = 30)        
        self.button_Receptor.grid(row = 2, column = 0)
        self.button_Receptor.configure(command = self.rodaReceptor)

    def mostrar(self):
        self.window1.tkraise()
    
    def rodaReceptor(self):
        self.janela_principal.mostrar_receptor()
        
    def rodaEmissor(self):
        self.janela_principal.mostrar_emissor()     

class Emissor_window():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window2 = tk.Frame(self.janela_principal.window)
        self.window2.grid(row = 0, column = 0, sticky = "nsew")

        self.window2.rowconfigure(0)
        self.window2.columnconfigure(0)

    def mostrar(self):
        self.janela_principal.mostrar_emissor()

class Receptor_window():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window3 = tk.Frame(self.janela_principal.window)
        self.window3.grid(row = 0, column = 0, sticky = "nsew")
        self.window3.configure(background = 'white')
        
        self.window3.rowconfigure(0)
        self.window3.columnconfigure(0)

    def mostrar(self):
        self.janela_principal.mostrar_receptor()

app = Janela_Principal()
app.iniciar()
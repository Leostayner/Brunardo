#Criado por Leonardo Medeiros
import tkinter as tk
import time
from datetime import datetime
import tkinter.messagebox as tkm
#from PIL import ImageTk
from PIL import Image
from tkinter import filedialog

class Janela_Principal():
    
    def __init__(self):
        
        self.app_config = dict()
        self.app_config['width_button'] = 200
        self.app_config['height_button'] = 150
        self.app_config['window_xpos'] = 100
        self.app_config['window_ypos'] = 100
        
        self.window_width  = self.app_config['width_button'] * 2
        self.window_height = self.app_config['height_button'] * 3

        self.window = tk.Tk()
        self.window.geometry("{}x{}+{}+{}".format(self.window_width, 
                                                  self.window_height, 
                                                  self.app_config['window_xpos'], 
                                                  self.app_config['window_ypos']))
        self.window.title("BruNardo")
        self.window.resizable(False, False)
    
        # Geometria da pagina
        self.window.rowconfigure(0, minsize = self.window_height)
        self.window.columnconfigure(0, minsize = self.window_height)
        
        # Menu Principal
        self.menu_principal = Menu_Principal(self)
    
        # Iniciar menu
        self.menu_principal.mostrar()
                     
    def iniciar(self):
        self.window.mainloop()

class Menu_Principal():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window1 = tk.Frame(self.janela_principal.window)
        self.window1.grid(row = 0, column = 0, sticky = "nsew")
        self.window1.configure(background = 'white')
        
	    #Variavel
        self.var = 1

        # Geometria da pagina        
        self.window1.rowconfigure(0, minsize = self.janela_principal.app_config['height_button'] - 50)
        self.window1.rowconfigure(1, minsize = self.janela_principal.app_config['height_button'])
        self.window1.rowconfigure(2, minsize = self.janela_principal.app_config['height_button'])

        self.window1.columnconfigure(0, minsize = self.janela_principal.window_width)
                
        #self.Logo = ImageTk.PhotoImage(Image.open("./interface_imgs/Logo.png"))
        self.Logo_label = tk.Label(self.window1)
        self.Logo_label.grid(row = 0, column = 0, sticky = "nsew")
        

        #self.txt = tk.Text(self.window1, height = 15, width = 30)
        #self.txt.grid(row = 1, column = 0, sticky = "nsew")
        #self.txt.configure(state = "disabled")

        self.scrool = tk.Scrollbar(self.window1)
        
        self.txt = tk.Text(self.window1, height=4, width=50)
        self.txt.grid(row = 1, column = 0)
        self.scrool.grid(row = 1, column = 0)
        self.scrool.config(command= self.txt.yview)
        self.txt.config(yscrollcommand= self.scrool.set)
        quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
        self.txt.insert("end", quote)


#        self.button2 = tk.Radiobutton(self.window1)
#        self.button2.configure(variable = self.var, value = 2)
#        self.button2.grid(row = 2, column = 0)


    def mostrar(self):
        self.window1.tkraise()
    
app = Janela_Principal()
app.iniciar()

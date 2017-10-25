
import tkinter as tk
import time
from datetime import datetime
import tkinter.messagebox as tkm
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog
import recepcao as rc
import transmissao as tr

class Janela_Principal():
    
    def __init__(self):
        
        self.app_config = dict()
        self.app_config['width_button'] = 200
        self.app_config['height_button'] = 150
        self.app_config['window_xpos'] = 100
        self.app_config['window_ypos'] = 100
        
        self.window_width  = 400
        self.window_height = 500    

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
        self.ment = tk.StringVar()

        # Geometria da pagina        
        self.window1.rowconfigure(0, minsize = self.janela_principal.window_height * 1/5 )
        self.window1.rowconfigure(1, minsize = self.janela_principal.window_height * 3/5 )
        self.window1.rowconfigure(2, minsize = self.janela_principal.window_height * 0.5/5 )
        self.window1.rowconfigure(3, minsize = self.janela_principal.window_height * 0.5/5 )


        self.window1.columnconfigure(0, minsize = self.janela_principal.window_width * 10/20)
        self.window1.columnconfigure(1, minsize = self.janela_principal.window_width * 9/20)
        self.window1.columnconfigure(2, minsize = (self.janela_principal.window_width * 1/20) - 2)
                
        self.Logo = ImageTk.PhotoImage(Image.open("./interface_imgs/Logo.png"))
        self.Logo_label = tk.Label(self.window1, image = self.Logo )
        self.Logo_label.grid(row = 0, column = 0, columnspan = 3, sticky = "nsew", )
       
        self.txt = tk.Text(self.window1, borderwidth = 3, height = 15, width = 20)
        self.txt.config(font = ("consolas", 12))
        self.txt.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew", padx = 2, pady = 2)

        self.scrollb = tk.Scrollbar(self.window1, command = self.txt.yview)
        self.scrollb.grid(row = 1, column = 2, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

        self.entry = tk.Entry(self.window1, borderwidth = 3, textvariable = self.ment)
        self.entry.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew", padx = 2, pady = 2) 
        
        self.button = tk.Button(self.window1, text = "Emissor")
        self.button.grid(row = 3, column = 0, sticky = "nsew")
        self.button.configure(command = self.enviar)

        self.button2 = tk.Button(self.window1, text = "Receptor")
        self.button2.grid(row = 3, column = 1, columnspan = 2, sticky = "nsew")
        self.button2.configure(command = self.receber)

        self.button3 = tk.Button(self.window1, background = "gray")
        self.button3.grid(row = 2, column = 2,sticky = "nsew", pady = 2)
        self.button3.configure(command = self.emitir)

    def mostrar(self):
        self.window1.tkraise()
    
    def enviar(self):
        self.button2.configure(state = "normal")
        self.button.configure(state = "disable")
        print("enviar")

    def receber(self):
        print("receber")
        self.button.configure(state = "normal")
        self.button2.configure(state = "disable")

    def emitir(self):
        print(self.ment.get())
        tr.transmissao(self.ment.get())  
        self.txt.insert("end", self.ment.get()+ '\n')
        self.entry.delete(0, 'end')

           

        


app = Janela_Principal()
app.iniciar()

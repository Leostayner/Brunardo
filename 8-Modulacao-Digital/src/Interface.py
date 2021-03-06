import threading
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
        
        self.window_width  = 350
        self.window_height = 450    

        self.window = tk.Tk()
        self.window.geometry("{}x{}+{}+{}".format(self.window_width, 
                                                  self.window_height, 
                                                  self.app_config['window_xpos'], 
                                                  self.app_config['window_ypos']))
        self.window.title("BruNardo")
        #self.window.resizable(False, False)
    
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

        # inicializa
        self.rx = rc.recepcao()
        
	    #Variavel
        self.var = 1
        self.ment = tk.StringVar()

        # Geometria da pagina        
        self.window1.rowconfigure(0, minsize = self.janela_principal.window_height * 2/8 - 20)
        self.window1.rowconfigure(1, minsize = self.janela_principal.window_height * 5/8 )
        self.window1.rowconfigure(2, minsize = self.janela_principal.window_height * 1/8 )
    

        self.window1.columnconfigure(0, minsize = self.janela_principal.window_width * 10/20 - 5)
        self.window1.columnconfigure(1, minsize = self.janela_principal.window_width * 9/20)
        self.window1.columnconfigure(2, minsize = (self.janela_principal.window_width * 1/20) - 2)
                
        self.Logo = ImageTk.PhotoImage(Image.open("./interface_imgs/brunardio2.png"))
        self.Logo_label = tk.Label(self.window1, image = self.Logo)
        self.Logo_label.grid(row = 0, column = 0, columnspan = 3, sticky = "nsew")
       
        self.txt = tk.Text(self.window1, borderwidth = 3, height = 15, width = 20)
        self.txt.config(font = ("typewriter", 12))
        self.txt.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew", padx = 2, pady = 2)

        self.scrollb = tk.Scrollbar(self.window1, command = self.txt.yview, borderwidth = 3)
        self.scrollb.grid(row = 1, column = 2, sticky='nsew',  padx = 2, pady = 2)
        self.txt['yscrollcommand'] = self.scrollb.set

        self.entry = tk.Entry(self.window1, borderwidth = 3, textvariable = self.ment)
        self.entry.grid(row = 2, column = 0, columnspan = 3, sticky = "nsew", padx = 2, pady = 2) 
        
        self.entry.bind("<Return>",self.emitir)

        #self.button3 = tk.Button(self.window1, background = "gray")
        #self.button3.grid(row = 2, column = 2,sticky = "nsew", pady = 2)
        #self.button3.configure(command = self.emitir)

        self.threadStart()

    def mostrar(self):
        self.window1.tkraise()
    
    def emitir(self,event):
        print(self.ment.get())
        tr.transmissao(self.ment.get())  
        self.txt.insert("end", self.ment.get()+ '\n')
        self.entry.delete(0, 'end')

    def threadStart(self):
        """ Starts RX thread (generate and run)
        """
        print("iniciado")
        self.thread = threading.Thread(target=self.thread, args=())
        self.thread.start()

    def thread(self):
        """ RX thread, to send data in parallel with the code
        """
        while True:
            print("Tred")
            self.texto = self.rx.get()
            print("Caracter: ", self.texto)
            self.txt.insert("end", self.texto)
            time.sleep(0.001)

app = Janela_Principal()
app.iniciar()

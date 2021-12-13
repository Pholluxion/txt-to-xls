'''

    1. Install requirements.txt run ' pip install -r requirements.txt '


'''

from tkinter import *
from tkinter import filedialog
import os


class Decodificator(Frame):


    def __init__(self, main_window):

        '''
        
        '''

        super().__init__(main_window)

        main_window.geometry("500x600")
        main_window.iconphoto(False, PhotoImage(file = "assets/logo.png"))
        # main_window.resizable(False,False)
        main_window.title("Decodificador")

        self.pathFile = StringVar()
        self.pathOutput = StringVar()
        self.pathFile.set("Ruta archivo .txt")
        self.pathOutput.set("Ruta de salida")

        self.buttonGetFile = Button(main_window,text="Abrir archivo",bg="light blue",command=self.getPathFile).pack(expand=True,fill = BOTH, padx=10, pady=10)
        self.labelPathFile = Label(main_window,textvariable= self.pathFile,width=280).pack(expand=True, padx=10, pady=10)
        self.buttonGetDes  = Button(main_window,text="Directorio destino",bg="light blue",command=self.getPathOut).pack(expand=True,fill = BOTH, padx=10, pady=10)
        self.labelPathFile = Label(main_window,textvariable= self.pathOutput,width=280).pack(expand=True, padx=10, pady=10)
        self.buttonDecod   = Button(main_window,text="Decodificar archivo",bg="pale green").pack(fill = BOTH,expand=True, padx=10, pady=50)
        self.labelDeveloper = Label(main_window,text= "Created by Carlos Daniel Peñaloza Torres\n2021",justify='center',width=280).pack(expand=True, padx=10, pady=10)

    def getPathFile(self):

        '''
        get 
        '''

        archivo_abierto=filedialog.askopenfilename(initialdir = "/",
            title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
            ("all files","*.*")))
        self.pathFile.set(archivo_abierto)

    def getPathOut(self):

        '''
        
        '''

        directorio=filedialog.askdirectory()
        if directorio!="":
            os.chdir(directorio)
        self.pathOutput.set(directorio)



if __name__ == '__main__':

    root = Tk()
    app = Decodificator(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
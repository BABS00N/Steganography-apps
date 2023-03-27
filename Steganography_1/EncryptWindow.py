import tkinter as tk
import math
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
#----------------------------
winEncr=tk.Tk()
winEncr.title('Шифратор')
picture = tk.PhotoImage(file='ico.png')
winEncr.iconphoto(False, picture)
winEncr.config(bg='gray')
winEncr.geometry("500x600")
winEncr.resizable(False,False)
#----------------------------
global textValue
textValue = ''
#explorer window function
def browseFiles():
    filenameF = filedialog.askopenfilename(initialdir = "/",
                                          title = "Выберите файл",
                                          filetypes = (("Image files",
                                                        "*.jpeg*"),
                                                       ("Image files",
                                                        "*.jpg*"),
                                                        ("Image files",
                                                        "*.png*")))
    # Путь к файлу
    fileExplorer_label.configure(text="Открытый файл: "+filenameF[:22]+'\n'+filenameF[22:61])
    global adressLoad
    adressLoad = str(filenameF)

def browseSave():
    filenameS = filedialog.askdirectory(initialdir = "/",
                                          title = "Выберите путь сохранения")
    # Путь к файлу
    saveExplorer_label.configure(text="Путь сохранения: " + filenameS[:22] + '\n' + filenameS[22:61])
    global adressSave
    adressSave = str(filenameS)

def encrypt():
    textValue = textArea.get("1.0","end-1c")
    file_name = fileName.get()
    if textValue == '':
        errorLabel.configure(text="Вы не ввели текст для зашифровки!")
        return
    elif file_name == '':
        errorLabel.configure(text="Вы не указали название зашифрованного изображения!")
        return

    import Encryptor
    Encryptor.encode(adressLoad, adressSave, textValue,file_name)
#----------------------------
textArea_lb = tk.Label(winEncr, text='Шифруемый текст',
                bg='gray',
                fg='white',
                font=('Arial',15),
                padx=34,
                height = 2,
                anchor = 'sw')
fileExplorer_label = Label(winEncr,
                            text = "Выберите изображение",
                            width=37,
                            height = 2,
                            bg = 'white',
                            fg = "blue")
saveExplorer_label = Label(winEncr,
                            text = "Укажите путь сохранения",
                            width=37,
                            height = 2,
                            bg = 'white',
                            fg = "blue")
fileName_lb = Label(winEncr, text='Укажите название файла и его расширение (*.png, *.jpg, *.jpeg)',
                bg='gray',
                fg='white',
                font=('Arial',11),
                padx=35,
                height = 2,
                #anchor = ''
                    )
errorLabel = Label(winEncr,
                   text = "",
                   width=37,
                   height = 2,
                   bg = 'white',
                   fg = "red")
#----------------------------
buttonExplore = Button(winEncr,
                        text = "Поиск...",
                        font=('Arial',12),
                        padx=33,pady = 4,
                        command = browseFiles)
buttonExplore2 = Button(winEncr,
                        text = "Поиск...",
                        font=('Arial',12),
                        padx=33,pady = 4,
                        command = browseSave)
buttonEncypt = Button(winEncr,
                      text = "Зашифровать",
                      font=('Arial',12),
                      padx=9,pady = 4,
                      command=encrypt)
#----------------------------
textArea = tk.Text(winEncr,
                   height = 5,
                   width = 53,
                   pady=5)
fileName = tk.Entry(winEncr)
#----------------------------
winEncr.grid_columnconfigure(0,minsize=300)
winEncr.grid_columnconfigure(1,minsize=200)

winEncr.grid_rowconfigure(1,minsize=110)
winEncr.grid_rowconfigure(2,minsize=50)
winEncr.grid_rowconfigure(3,minsize=50)
#winEncr.grid_rowconfigure(5,minsize=50)

textArea_lb.grid(row=0,column=0,columnspan=2,stick='w')
textArea.grid(row=1,column=0,columnspan=2)
fileExplorer_label.grid(row=2,column=0,stick='e')
buttonExplore.grid(row=2,column=1)
saveExplorer_label.grid(row=3,column=0,stick='e')
buttonExplore2.grid(row=3,column=1)
fileName_lb.grid(row=4,column=0,stick='w',columnspan=2)
fileName.grid(row=5,column=0,stick='e')
buttonEncypt.grid(row=5,column=1)
errorLabel.grid(row=6,column=0,columnspan=2)
#----------------------------
winEncr.mainloop()

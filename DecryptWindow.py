import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

winDecr=tk.Tk()
winDecr.title('Шифратор')
picture = tk.PhotoImage(file='ico.png')
winDecr.iconphoto(False, picture)
winDecr.config(bg='gray')
winDecr.geometry("500x600")
winDecr.resizable(False,False)
#----------------------------
global textValue
textValue = ''
#explorer window function
def browseFiles(fileExplorer_label):
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

def browseFiles1():
    browseFiles(fileExplorer_label1)

def browseFiles2():
    browseFiles(fileExplorer_label2)

def decrypt():
    return 0
#----------------------------
fileExplorer_label1 = Label(winDecr,
                        text = "Выберите зашифрованное изображение",
                        width=37,
                        height = 2,
                        bg = 'white',
                        fg = "blue")
fileExplorer_label2 = Label(winDecr,
                        text="Выберите оригинальное изображение",
                        width=37,
                        height=2,
                        bg='white',
                        fg="blue")
#----------------------------
textArea = tk.Text(winDecr, height=5,width=53,font="Arial 11")
textArea.insert("end", "Здесь будет расшифрованное сообщение")
#----------------------------
buttonExplore1 = Button(winDecr,
                        text = "Поиск...",
                        font=('Arial',12),
                        padx=33,pady = 4,
                        command = browseFiles1)
buttonExplore2 = Button(winDecr,
                        text = "Поиск...",
                        font=('Arial',12),
                        padx=33,pady = 4,
                        command = browseFiles2)
buttonDecrypt = Button(winDecr,
                      text = "Зашифровать",
                      font=('Arial',12),
                      padx=9,pady = 4,
                      command=decrypt)
#----------------------------
winDecr.grid_columnconfigure(0,minsize=300)
winDecr.grid_columnconfigure(1,minsize=200)

winDecr.grid_rowconfigure(2,minsize=50)
winDecr.grid_rowconfigure(3,minsize=50)
winDecr.grid_rowconfigure(4,minsize=110)
#----------------------------
fileExplorer_label1.grid(row=2,column=0,stick='e')
buttonExplore1.grid(row=2,column=1)
fileExplorer_label2.grid(row=3,column=0,stick='e')
buttonExplore2.grid(row=3,column=1)
textArea.grid(row=4,column=0,stick='',columnspan=2)
#----------------------------
winDecr.mainloop()

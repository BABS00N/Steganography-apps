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
# def browseFiles(fileExplorer_label):
#     filenameF = filedialog.askopenfilename(initialdir = "/",
#                                           title = "Выберите файл",
#                                           filetypes = (("Image files",
#                                                         "*.jpeg*"),
#                                                        ("Image files",
#                                                         "*.jpg*"),
#                                                         ("Image files",
#                                                         "*.png*")))
#     # Путь к файлу
#     fileExplorer_label.configure(text="Открытый файл: "+filenameF[:22]+'\n'+filenameF[22:61])
#     global adressLoad
#     adressLoad = str(filenameF)
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Выберите файл",
                                          filetypes = (("Image files",
                                                        "*.jpeg*"),
                                                       ("Image files",
                                                        "*.jpg*"),
                                                        ("Image files",
                                                        "*.png*")))
    # Путь к файлу
    fileExplorer_label.configure(text="Открытый файл: "+filename[:22]+'\n'+filename[22:61])
    global adressLoad
    adressLoad = str(filename)

def decrypt():
    import Decryptor
    keyword = keyArea.get("1.0","end-1c")
    textArea.delete(1.0, END)
    textArea.insert("end",Decryptor.decrypt(adressLoad,keyword))
    #Decryptor.decrypt(keyword)
#----------------------------
fileExplorer_label = Label(winDecr,
                        text = "Выберите зашифрованное изображение",
                        width=37,

                        height = 2,
                        bg = 'white',
                        fg = "blue")
keyArea_label = Label(winDecr,
                        font="Arial 11",
                        text="Введите ключ",
                        width=12,
                        padx=10,
                        height=1,
                        bg='gray',
                        fg="white")
#----------------------------
textArea = tk.Text(winDecr, height=5,width=53,font="Arial 11")
textArea.insert("end", "Здесь будет расшифрованное сообщение")

keyArea = tk.Text(winDecr, height=1,width=39,font="Arial 11",padx=0)
#----------------------------
buttonExplore = Button(winDecr,
                        text = "Поиск...",
                        font=('Arial',12),
                        padx=33,pady = 4,
                        command = browseFiles)

buttonDecrypt = Button(winDecr,
                      text = "Расшифровать",
                      font=('Arial',12),
                      padx=3,pady = 4,
                      command=decrypt)
#----------------------------
winDecr.grid_columnconfigure(0,minsize=150)
winDecr.grid_columnconfigure(1,minsize=150)
winDecr.grid_columnconfigure(2,minsize=200)

winDecr.grid_rowconfigure(1,minsize=10)
winDecr.grid_rowconfigure(2,minsize=45)
winDecr.grid_rowconfigure(3,minsize=40)
winDecr.grid_rowconfigure(4,minsize=100)
winDecr.grid_rowconfigure(5,minsize=55)
#----------------------------
fileExplorer_label.grid(row=2,column=0,stick='e',columnspan=2)
buttonExplore.grid(row=2,column=2)
keyArea_label.grid(row=3,column=0,stick='e')
keyArea.grid(row=3,column=1,columnspan=2,stick='w')
textArea.grid(row=4,column=0,stick='',columnspan=3)
buttonDecrypt.grid(row=5,column=2)
#----------------------------
winDecr.mainloop()

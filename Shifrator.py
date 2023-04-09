import tkinter as tk
from PIL import Image, ImageTk

#--------------------------------
title='Шифратор'
winChoice=tk.Tk()
winChoice.title(title)
photo = tk.PhotoImage(file='ico.png')
winChoice.iconphoto(False, photo)
winChoice.config(bg='gray')

winChoice.geometry("500x600")
winChoice.resizable(False,False)
#--------------------------------
lbInfo = tk.Label(winChoice, text='Выберите режим работы приложения'
                    ,bg='white',
                    fg='black',
                    font=('Arial',19,'bold'),
                    padx=20,
                    anchor='center')
#--------------------------------
def winEncrypt():
    winChoice.destroy()
    import EncryptWindow

def winDecrypt():
    winChoice.destroy()
    import DecryptWindow as De
#--------------------------------
encrypt = tk.Button(winChoice, text='Зашифровать'
                    ,bg='white',
                    fg='black',
                    font=('Arial',20,'bold'),
                    width=14,
                    anchor='center',
                    command=winEncrypt)

decrypt = tk.Button(winChoice, text='Расшифровать'
                    ,bg='white',
                    fg='black',
                    font=('Arial',20,'bold'),
                    width=14,
                    anchor='center',
                    command=winDecrypt)
#--------------------------------
lbInfo.grid(row=0,column=0,columnspan=2)
encrypt.grid(row=1,column=0,stick='we')
decrypt.grid(row=1,column=1,stick='we')
#--------------------------------
winChoice.mainloop()
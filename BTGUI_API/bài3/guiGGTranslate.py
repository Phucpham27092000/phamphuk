import requests
import tkinter as tk
from tkinter.ttk import *
from tkinter.scrolledtext import *
from PIL import Image,ImageTk
from googletrans import Translator, LANGUAGES
from GGtrans import *

def Clear():
    scrollText1.delete(1.0, tk.END)
    scrollText2.config(state='normal')
    scrollText2.delete(1.0, tk.END)
    scrollText2.config(state='disabled')
    
A = list(LANGUAGES.values())
B = list(LANGUAGES.keys())
def Translating():
    scrollText2.config(state='normal')
    scrollText2.delete(1.0, tk.END)
    scrollText2.config(state='disabled')    

    text = str(scrollText1.get("1.0", "end-1c"))
    oldLang = str(combobox1.get())      
    targetLang = str(combobox2.get())      
    
    for i in range(len(A)):
        if oldLang == A[i]:
            old_Lang = B[i]

    for i in range(len(A)):
        if targetLang == A[i]:
            target_Lang = B[i]
    if str(combobox1.get()) == "Auto detect":
        vanbanDaDich = dichVanBan(text, target_Lang)
    else:
        vanbanDaDich = dichVanBan2(text, old_Lang, target_Lang)
    scrollText2.config(state='normal')
    scrollText2.insert(tk.END, vanbanDaDich)
    scrollText2.config(state='disabled')

root = tk.Tk()
root.title("Language Translator")
root.geometry("800x500")
root.maxsize(800,500)
root.minsize(800,500)

img_path = "GGdich.jpg"
newImg_path = "newGGdich.jpg"
img = Image.open(img_path)
newImg = img.resize((100,100))
newImg.save(newImg_path)
img_tk = ImageTk.PhotoImage(newImg)

pict = tk.Label(root, image=img_tk)
pict.place(x=340,y=20)

Auto = list(LANGUAGES.values())
Auto.insert(0, "Auto detect")
combobox1 = Combobox(root, width=29, height=10, font=('Arial',15,'bold'))
combobox1['values'] = Auto
combobox1.place(x=20, y=150)

scrollText1 = ScrolledText(root,width=40, height=10, border=5)
scrollText1.place(x=20, y=200)

combobox2 = Combobox(root, width=29, height=10, font=('Arial',15,'bold'))
combobox2['values'] = list(LANGUAGES.values())
combobox2.place(x=430, y=150)

scrollText2 = ScrolledText(root, width=40, height=10, border=5)
scrollText2.config(state='disabled')
scrollText2.place(x=430, y=200)

Dich = tk.Button(root, text="Translate", font=('Arial',15,'bold'), width=10, command=Translating)
Dich.place(x=250, y=400)

Xoa = tk.Button(root, text="Clear", font=('Arial',15,'bold'), width=10, command=Clear)
Xoa.place(x=400, y=400)

root.mainloop()


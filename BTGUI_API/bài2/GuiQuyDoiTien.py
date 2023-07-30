import requests
import tkinter as tk
from tkinter.ttk import *
from tkinter.scrolledtext import *
from PIL import Image,ImageTk
from CurrencyConverter import *
from datetime import datetime 

def clear():
    scrollText.config(state='normal')
    scrollText.delete(1.0,tk.END)
    scrollText.config(state='disabled')
    new_amount.set("")

def search():
    SoTienCanDoi = old_amount.get()
    tienTeCu = combobox1.get()
    tienTeMoi = combobox2.get()
    Converter(SoTienCanDoi, tienTeCu, tienTeMoi)

    new_amount.set(DATA[3])
    # print(DATA)
    # print(DATA[3])
    currenttime = datetime.now()    

    scrollText.config(state='normal')
    scrollText.insert(tk.END, str(SoTienCanDoi) + " " + tienTeCu + " equals " + str(DATA[3]) + " " +tienTeMoi + "\n")
    scrollText.insert(tk.END, "Last time update: " + str(currenttime))
    scrollText.config(state='disabled')
    DATA.clear()
    # print(DATA)

root = tk.Tk()
root.title("Currency Converter")
root.geometry("800x500")
root.maxsize(800,500)
root.minsize(800,500)

TheTitle = tk.Label(root, text="USD Currency Converter", font=("Arial",20,"bold"), justify='center')
TheTitle.place(x=250, y=20)
amount = tk.Label(root,text="Amount", font=("Arial",15,"bold"), width=10, justify='left')
amount.place(x=0,y=50)

old_amount = tk.IntVar()
new_amount = tk.IntVar()
textbox1 = tk.Entry(root, textvariable=old_amount, font=("Arial",15), border=3 ,width=25)
textbox1.place(x=20, y=100)
textbox1.delete(0,tk.END)

textbox2= tk.Entry(root, textvariable=new_amount, font=("Arial",15), border=3 ,width=25)
textbox2.place(x=20,y=180)
textbox2.delete(0,tk.END)
textbox2.config(state="disabled")

combobox1 = Combobox(root, wid=24, height=10, font=("Arial",15))
combobox1['values'] = ("USD","VND","EUR","JPY","GBP","AUD","SGD","HKD", "NZD")
combobox1.place(x=480, y=100)

combobox2 = Combobox(root, wid=24, height=10, font=("Arial",15))
combobox2['values'] = ("USD","VND","EUR","JPY","GBP","AUD","SGD","HKD", "NZD")
combobox2.place(x=480, y=180)
#"USD (Đô la Mỹ)","VND (Việt Nam Đồng)","EUR (Euro)","JPY (Yên Nhật)","GBP (Bảng Anh)",
#"AUD (Đô la Úc)","SGD (Đô la Singapore)","HKD (Đô la Hồng Kông)", "NZD (Đô la New Zealand)"

Search = tk.Button(root, text="Search", font=("Arial",15,"bold"), width=10, command=search)
Search.place(x=20, y=260)

Clear = tk.Button(root, text="Clear", font=("Arial",15,"bold"), width=10, command=clear)
Clear.place(x=20, y=360)

scrollText = ScrolledText(root, width=70, height=10)
scrollText.place(x=200, y=260)
scrollText.config(state='disabled')

img_path = "converter.jpg"
newImg_path = "newConverter.jpg"

img = Image.open(img_path)
newImg = img.resize((110,110))
newImg.save(newImg_path)
img_tk = ImageTk.PhotoImage(newImg)

Pic = tk.Label(root, image=img_tk)
Pic.place(x=330,y=100)
root.mainloop()
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from ChucNang import *

giaodien = tkinter.Tk()
giaodien.title("Quản lý học viên - PythonBKACAD")
giaodien.geometry('900x700')
giaodien.configure(bg='DodgerBlue4')

# FUNCTIONS----------------------------------------------------
SQL = tkinter.StringVar()
def checkConnection():
    SQL.set(checkConnect())

def getDATA():  
    box.config(state='normal')
    box.delete("1.0",tkinter.END)
    for i in getAllData(): 
        box.insert(tkinter.END,str(i) + "\n")    
    box.config(state='disabled')
    
Confirm = tkinter.StringVar()
def addDATA():
    addname = Ten.get()
    addage = Tuoi.get()
    addsex = combobox.get()
    addcountry = Quequan.get()
    addenglish = TiengAnh.get()
    addinfo = Thongtin.get()
    createData(addname,addage,addsex,addcountry,addenglish,addinfo)
    textbox1.delete('0', tkinter.END)
    textbox2.delete('0', tkinter.END)
    combobox.delete('0', tkinter.END)
    textbox3.delete('0', tkinter.END)
    textbox4.delete('0', tkinter.END)
    textbox5.delete('0', tkinter.END)
    Confirm.set("Added successfully!")

ID = tkinter.IntVar()
def deleteDATA():    
    xoaByID = tkinter.Label(giaodien, text="Enter ID", fg='white', bg='DodgerBlue4', font=15, pady=5, width=30)
    xoaByID.grid(column=2,row=9)
    findID1 = tkinter.Entry(giaodien, width=5, textvariable=ID, font=15)
    findID1.grid(column=3,row=9)    
    nutXoa = tkinter.Button(giaodien, text="Xóa", fg='black', bg='white', font=15, width=5, command=XoaDATA)
    nutXoa.grid(column=3,row=8)   

def XoaDATA():
    deleteID = ID.get()
    deleteDatabyID(deleteID)
    Confirm.set("Deleted successfully!")

def updateDATA():
    suaByID = tkinter.Label(giaodien, text="Enter ID", fg='white', bg='DodgerBlue4', font=15, pady=5, width=30)
    suaByID.grid(column=2,row=9)
    findID1 = tkinter.Entry(giaodien, width=5, textvariable=ID, font=15)
    findID1.grid(column=3,row=9)    
    nutSua = tkinter.Button(giaodien, text="Thay đổi", fg='black', bg='white', font=15, width=5, command=suaDATA)
    nutSua.grid(column=3,row=8)      

def suaDATA():
    updateID = ID.get()
    newname = Ten.get()
    newage = Tuoi.get()
    newsex = combobox.get()
    newcountry = Quequan.get()
    newenglish = TiengAnh.get()
    newinfo = Thongtin.get()
    updateDatabyID(updateID,newname,newage,newsex,newcountry,newenglish,newinfo)
    textbox1.delete('0', tkinter.END)
    textbox2.delete('0', tkinter.END)
    combobox.delete('0', tkinter.END)
    textbox3.delete('0', tkinter.END)
    textbox4.delete('0', tkinter.END)
    textbox5.delete('0', tkinter.END)
    
    Confirm.set("Updates successfully!")

# LAYOUT------------------------------------------------------------------------------------------------------------------------------------
Title = tkinter.Label(giaodien, text="CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", fg='white', bg='DodgerBlue4', font=("Times New Roman",20), pady=10)
Title.grid(column=4,row=0)

Name = tkinter.Label(giaodien, text='Name', fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Name.grid(column=2, row=1)
Ten = tkinter.StringVar()
textbox1 = tkinter.Entry(giaodien, width=30, textvariable=Ten, font=15)
textbox1.grid(column=4, row=1)

Age = tkinter.Label(giaodien, text="Age", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Age.grid(column=2, row=2)
Tuoi = tkinter.IntVar()
textbox2 = tkinter.Entry(giaodien, width=30, textvariable=Tuoi, font=15)
textbox2.grid(column=4, row=2)

Sex = tkinter.Label(giaodien, text="Sex", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Sex.grid(column=2, row=3)
combobox = Combobox(giaodien, width=28, height=10, font=15)
combobox['values'] = ('Nam','Nữ')
combobox.grid(column=4, row=3)

Country = tkinter.Label(giaodien, text="Country", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Country.grid(column=2, row=4)
Quequan = tkinter.StringVar()
textbox3 = tkinter.Entry(giaodien, width=30, textvariable=Quequan, font=15)
textbox3.grid(column=4, row=4)

English = tkinter.Label(giaodien, text="English", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
English.grid(column=2, row=5)
TiengAnh = tkinter.IntVar()
textbox4 = tkinter.Entry(giaodien, width=30, textvariable=TiengAnh, font=15)
textbox4.grid(column=4, row=5)

Information = tkinter.Label(giaodien, text="Information", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Information.grid(column=2, row=6)
Thongtin = tkinter.IntVar()
textbox5 = tkinter.Entry(giaodien, width=30, textvariable=Thongtin, font=15)
textbox5.grid(column=4, row=6)
        
box = ScrolledText(giaodien, width = 50, height = 10)
box.grid(column=4, row=10, padx=10, pady=10)
box.config(state='disabled') 

check = tkinter.Label(giaodien, textvariable=SQL, fg='white', width=20, font=15, bg='DodgerBlue4')
check.grid(column=4, row=12) 

res = tkinter.Label(giaodien, textvariable=Confirm, fg='white', width=20, font=15, bg='DodgerBlue4')
res.grid(column=4,row=9)

# BUTTONS----------------------------------------------------------------------------------------
themHV = tkinter.Button(giaodien, text="Thêm học viên", fg='black', bg='white', font=15, width=20, command=addDATA)
themHV.grid(column=2, row=7, padx=5, pady=5)
# 
hienThiHV = tkinter.Button(giaodien, text="Hiển thị học viên", fg='black', bg='white', font=15, width=20, command=getDATA)
hienThiHV.grid(column=4, row=7, padx=5, pady=5)
# 
xoaHV = tkinter.Button(giaodien, text="Xóa học viên", fg='black', bg='white', font=15, width=20, command=deleteDATA)
xoaHV.grid(column=2, row=8, padx=5, pady=5)

suaHV = tkinter.Button(giaodien, text="Sửa học viên", fg='black', bg='white', font=15, width=20, command=updateDATA)
suaHV.grid(column=4, row=8, padx=5, pady=5)

ktraKetnoi = tkinter.Button(giaodien, text="Kiểm tra kết nối", fg='black', bg='white', font=15, width=20, command=checkConnection)
ktraKetnoi.grid(column=4, row=11, padx=5, pady=5)

giaodien.mainloop()
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from Chucnang import *

win = tkinter.Tk()
win.title("Quản lý nhân viên - PythonBKACAD")
win.geometry('900x700')
win.configure(bg='DodgerBlue4')

# FUNCTION----------------------------------------
SQL = tkinter.StringVar()
Confirm = tkinter.StringVar()
ID = tkinter.IntVar()

def checkConnection():
    SQL.set(checkConnect())

def getDATA():
    box.config(state='normal')
    box.delete('1.0',tkinter.END)
    for i in getData():
        box.insert(tkinter.END, str(i) + '\n')
    box.config(state='disabled')

def addDATA():
    addname = Ten.get()
    addage = Tuoi.get()
    addsex = combobox.get()
    addcountry = Quequan.get()
    addposition = ChucVu.get()
    addworkdays = SoNgayLam.get()
    createData(addname, addage, addsex, addcountry, addposition, addworkdays)
    textbox1.delete('0', tkinter.END)
    textbox2.delete('0', tkinter.END)
    combobox.delete('0', tkinter.END)
    textbox3.delete('0', tkinter.END)
    textbox4.delete('0', tkinter.END)
    textbox5.delete('0', tkinter.END)
    Confirm.set("Added successfully!")

def deleteDATA():
    xoaByID = tkinter.Label(win, text="Enter ID", fg='white', bg='DodgerBlue4', font=15, pady=5, width=30)
    xoaByID.grid(column=2,row=9)
    findID = tkinter.Entry(win, width=5, textvariable=ID, font=15)
    findID.grid(column=3,row=9)    
    nutXoa = tkinter.Button(win, text="Xóa", fg='black', bg='white', font=15, width=5, command=xoaDATA)
    nutXoa.grid(column=3,row=8)  

def xoaDATA():
    deleteID = ID.get()
    deleteData(deleteID)
    Confirm.set("Deleted successfully!")

def updateDATA():
    suaByID = tkinter.Label(win, text="Enter ID", fg='white', bg='DodgerBlue4', font=15, pady=5, width=30)
    suaByID.grid(column=2,row=9)
    findID = tkinter.Entry(win, width=5, textvariable=ID, font=15)
    findID.grid(column=3,row=9)    
    nutSua = tkinter.Button(win, text="Thay đổi", fg='black', bg='white', font=15, width=5, command=suaDATA)
    nutSua.grid(column=3,row=8)

def suaDATA():
    updateID = ID.get()
    newname = Ten.get()
    newage = Tuoi.get()
    newsex = combobox.get()
    newcountry = Quequan.get()
    newposition = ChucVu.get()
    newworkdays = SoNgayLam.get()
    updateData(updateID,newname,newage,newsex,newcountry,newposition,newworkdays)
    textbox1.delete('0', tkinter.END)
    textbox2.delete('0', tkinter.END)
    combobox.delete('0', tkinter.END)
    textbox3.delete('0', tkinter.END)
    textbox4.delete('0', tkinter.END)
    textbox5.delete('0', tkinter.END)
    Confirm.set("Updates successfully!")

# LAYOUT------------------------------------------
Title = tkinter.Label(win, text="CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN", fg='white', bg='DodgerBlue4', font=("Times New Roman",20), pady=10)
Title.grid(column=4,row=0)

Name = tkinter.Label(win, text='Name', fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Name.grid(column=2, row=1)
Ten = tkinter.StringVar()
textbox1 = tkinter.Entry(win, width=30, textvariable=Ten, font=15)
textbox1.grid(column=4, row=1)

Age = tkinter.Label(win, text="Age", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Age.grid(column=2, row=2)
Tuoi = tkinter.IntVar()
textbox2 = tkinter.Entry(win, width=30, textvariable=Tuoi, font=15)
textbox2.grid(column=4, row=2)

Sex = tkinter.Label(win, text="Sex", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Sex.grid(column=2, row=3)
combobox = Combobox(win, width=28, height=10, font=15)
combobox['values'] = ('Nam','Nữ')
combobox.grid(column=4, row=3)

Country = tkinter.Label(win, text="Country", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
Country.grid(column=2, row=4)
Quequan = tkinter.StringVar()
textbox3 = tkinter.Entry(win, width=30, textvariable=Quequan, font=15)
textbox3.grid(column=4, row=4)

position = tkinter.Label(win, text="Position", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
position.grid(column=2, row=5)
ChucVu = tkinter.StringVar()
textbox4 = tkinter.Entry(win, textvariable=ChucVu, width=30, font=15)
textbox4.grid(column=4, row=5)

workdays = tkinter.Label(win, text="Workdays", fg='white', bg='DodgerBlue4', font=15, pady=5, width=20)
workdays.grid(column=2, row=6)
SoNgayLam = tkinter.IntVar()
textbox5 = tkinter.Entry(win, textvariable=SoNgayLam, width=30, font=15)
textbox5.grid(column=4, row=6)

box = ScrolledText(win, width = 50, height = 10)
box.grid(column=4, row=10, padx=10, pady=10)
box.config(state='disabled') 

check = tkinter.Label(win, textvariable=SQL, fg='white', width=20, font=15, bg='DodgerBlue4')
check.grid(column=4, row=12) 

res = tkinter.Label(win, textvariable=Confirm, fg='white', width=20, font=15, bg='DodgerBlue4')
res.grid(column=4,row=9)
# BUTTONS-----------------------------------------
themNV = tkinter.Button(win, text="Thêm nhân viên", fg='black', bg='white', font=15, width=20, command=addDATA)
themNV.grid(column=2, row=7, padx = 5, pady = 5)

hienthiNV = tkinter.Button(win, text="Hiển thị nhân viên", fg='black', bg='white', font=15, width=20, command=getDATA)
hienthiNV.grid(column=4, row=7, padx = 5, pady = 5)

xoaNV = tkinter.Button(win, text="Xóa nhân viên", fg='black', bg='white', font=15, width=20, command=deleteDATA)
xoaNV.grid(column=2, row=8, padx = 5, pady = 5)

suaNV = tkinter.Button(win, text="Sửa nhân viên", fg='black', bg='white', font=15, width=20, command=updateDATA)
suaNV.grid(column=4, row=8, padx = 5, pady = 5)

ktraKetnoi = tkinter.Button(win, text="Kiểm tra kết nối", fg='black', bg='white', font=15, width=20, command=checkConnection)
ktraKetnoi.grid(column=4, row=11, padx=5, pady=5)

xepTheoTen = tkinter.Button(win, text="Sắp xếp theo tên", fg='black', bg='white', font=15, width=20, command=sortByName)
xepTheoTen.grid(column=5, row=7, padx=5, pady=5)

xepTheoLuong = tkinter.Button(win, text="Sắp xếp theo lương", fg='black', bg='white', font=15, width=20, command=sortBySalary)
xepTheoLuong.grid(column=5, row=8, padx=5, pady=5)

win.mainloop()
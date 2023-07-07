import tkinter
from tkinter.ttk import *
from tkinter.scrolledtext import *

giaodien = tkinter.Tk()
giaodien.title("Quản lý học viên - PythonBKACAD")
giaodien.geometry('800x800')
giaodien.configure(bg='DodgerBlue4')


Title = tkinter.Label(giaodien, text="CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", fg='white', bg='DodgerBlue4', font=("Times New Roman",20), pady=10)
Title.grid(column=3,row=0)

Name = tkinter.Label(giaodien, text='Name', fg='white', bg='DodgerBlue4', font=15, pady=10, width=20)
Name.grid(column=2, row=1)
Ten = tkinter.StringVar()
textbox1 = tkinter.Entry(giaodien, width=30, textvariable=Ten, font=15)
textbox1.grid(column=3, row=1)

Age = tkinter.Label(giaodien, text="Age", fg='white', bg='DodgerBlue4', font=15, pady=10, width=20)
Age.grid(column=2, row=2)
Tuoi = tkinter.IntVar()
textbox2 = tkinter.Entry(giaodien, width=30, textvariable=Tuoi, font=15)
textbox2.grid(column=3, row=2)

Country = tkinter.Label(giaodien, text="Country", fg='white', bg='DodgerBlue4', font=15, pady=10, width=20)
Country.grid(column=2, row=3)
Quequan = tkinter.StringVar()
textbox3 = tkinter.Entry(giaodien, width=30, textvariable=Country, font=15)
textbox3.grid(column=3, row=3)

Sex = tkinter.Label(giaodien, text="Sex", fg='white', bg='DodgerBlue4', font=15, pady=10, width=20)
Sex.grid(column=2, row=4)
combobox = Combobox(giaodien, width=42, height=10)
combobox['values'] = ('Nam','Nữ')
combobox.grid(column=3, row=4)

English = tkinter.Label(giaodien, text="English", fg='white', bg='DodgerBlue4', font=15, pady=10, width=20)
English.grid(column=2, row=5)
TiengAnh = tkinter.IntVar()
textbox4 = tkinter.Entry(giaodien, width=30, textvariable=TiengAnh, font=15,)
textbox4.grid(column=3, row=5)

Information = tkinter.Label(giaodien, text="Information", fg='white', bg='DodgerBlue4', font=15, pady=10, width=20)
Information.grid(column=2, row=6)
Thongtin = tkinter.IntVar()
textbox5 = tkinter.Entry(giaodien, width=30, textvariable=Thongtin, font=15)
textbox5.grid(column=3, row=6)

themHV = tkinter.Button(giaodien, text="Thêm học viên", fg='black', bg='white', font=15, width=20)
themHV.grid(column=2, row=7, padx=10, pady=10)

hienThiHV = tkinter.Button(giaodien, text="Hiển thị học viên", fg='black', bg='white', font=15, width=20)
hienThiHV.grid(column=3, row=7, padx=10, pady=10)

xoaHV = tkinter.Button(giaodien, text="Xóa học viên", fg='black', bg='white', font=15, width=20)
xoaHV.grid(column=2, row=8, padx=10, pady=10)

suaHV = tkinter.Button(giaodien, text="Sửa học viên", fg='black', bg='white', font=15, width=20)
suaHV.grid(column=3, row=8, padx=10, pady=10)

box = ScrolledText(giaodien, width = 50, height = 10)
box.grid(column=3, row=9, padx=10, pady=10)

ktraKetnoi = tkinter.Button(giaodien, text="Kiểm tra kết nối", fg='black', bg='white', font=15, width=20)
ktraKetnoi.grid(column=3, row=10, padx=10, pady=10)

giaodien.mainloop()
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
import random

Lode = Tk()
Lode.title("Lô đề")
Lode.geometry("700x600")

def miniwindow():
    mini = tkinter.Toplevel(Lode)
    mini.title("Warning")
    mini.geometry("300x100")    
    outOfMoney = tkinter.Label(mini, text="Bạn không thể chơi tiếp", font=("Times New Roman",14), justify="center")
    outOfMoney.pack(padx=20, pady=20)

player_balance = 1000000
def play_de():
    XosoBox.config(state="normal")
    XosoBox.delete(1.0, tkinter.END)
    XosoBox.config(state="disabled")
    global player_balance    

    number = number2.get()
    point = point2.get()
    bet = point * 1000

    XosoBox.config(state="normal")

    lottery_list = []
    XosoBox.insert(tkinter.END, "Giải ĐB:   ")
    result0 = random.randint(10000,99999)        
    XosoBox.insert(tkinter.END, str(result0) + " ")
    last20 = int(str(result0)[-2:])
    lottery_list.append(last20)
    XosoBox.insert(tkinter.END, "\n")
    
    XosoBox.insert(tkinter.END, "       1:      ")
    result1 = random.randint(10000,99999)        
    XosoBox.insert(tkinter.END, str(result1) + " ")
    last21 = int(str(result1)[-2:])
    lottery_list.append(last21)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       2:      ")
    for i in range(2):
        result2 = random.randint(10000,99999)        
        XosoBox.insert(tkinter.END, str(result2) + " ")
        last22 = int(str(result2)[-2:])
        lottery_list.append(last22)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       3:      ")
    for i in range(6):
        result3 = random.randint(10000,99999)        
        XosoBox.insert(tkinter.END, str(result3) + " ")
        last23 = int(str(result3)[-2:])
        lottery_list.append(last23)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       4:      ")
    for i in range(4):
        result4 = random.randint(1000,9999)        
        XosoBox.insert(tkinter.END, str(result4) + " ")
        last24 = int(str(result4)[-2:])
        lottery_list.append(last24)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       5:      ")
    for i in range(6):
        result5 = random.randint(1000,9999)        
        XosoBox.insert(tkinter.END, str(result5) + " ")
        last25 = int(str(result5)[-2:])
        lottery_list.append(last25)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       6:      ")
    for i in range(3):
        result6 = random.randint(100,999)        
        XosoBox.insert(tkinter.END, str(result6) + " ")
        last26 = int(str(result6)[-2:])
        lottery_list.append(last26)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       7:      ")
    for i in range(4):
        result7 = random.randint(10,99)        
        XosoBox.insert(tkinter.END, str(result7) + " ")
        last27 = int(str(result7)[-2:]) 
        lottery_list.append(last27)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.config(state="disabled")  
    # print(lottery_list)
    # A = []
    result = int(str(number)[-2:])
    
    player_balance -= bet
    textbox5.config(state='normal')
    textbox5.delete(0, tkinter.END)
    textbox5.insert(tkinter.END, player_balance)
    textbox5.config(state='disabled')

    for i in range(len(lottery_list)):
        if result == lottery_list[i]:
            # A.append(lottery_list[i])        
            player_balance += bet
        
    textbox5.config(state='normal')
    textbox5.delete(0, tkinter.END)
    textbox5.insert(tkinter.END, player_balance)
    textbox5.config(state='disabled')
    # print(A) 
        
    if player_balance <= 0:
        textbox5.delete(0, tkinter.END)
        XosoBox.config(state="normal")
        XosoBox.delete(1.0, tkinter.END)
        XosoBox.config(state="disabled")
        miniwindow()

def play_lo():
    XosoBox.config(state="normal")
    XosoBox.delete(1.0, tkinter.END)
    XosoBox.config(state="disabled")
    global player_balance    

    number = number1.get()
    point = point1.get()
    bet = point * 23000

    XosoBox.config(state="normal")

    lottery_list = []
    XosoBox.insert(tkinter.END, "Giải ĐB:   ")
    result0 = random.randint(10000,99999)        
    XosoBox.insert(tkinter.END, str(result0) + " ")
    last20 = int(str(result0)[-2:])
    lottery_list.append(last20)
    XosoBox.insert(tkinter.END, "\n")
    
    XosoBox.insert(tkinter.END, "       1:      ")
    result1 = random.randint(10000,99999)        
    XosoBox.insert(tkinter.END, str(result1) + " ")
    last21 = int(str(result1)[-2:])
    lottery_list.append(last21)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       2:      ")
    for i in range(2):
        result2 = random.randint(10000,99999)        
        XosoBox.insert(tkinter.END, str(result2) + " ")
        last22 = int(str(result2)[-2:])
        lottery_list.append(last22)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       3:      ")
    for i in range(6):
        result3 = random.randint(10000,99999)        
        XosoBox.insert(tkinter.END, str(result3) + " ")
        last23 = int(str(result3)[-2:])
        lottery_list.append(last23)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       4:      ")
    for i in range(4):
        result4 = random.randint(1000,9999)        
        XosoBox.insert(tkinter.END, str(result4) + " ")
        last24 = int(str(result4)[-2:])
        lottery_list.append(last24)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       5:      ")
    for i in range(6):
        result5 = random.randint(1000,9999)        
        XosoBox.insert(tkinter.END, str(result5) + " ")
        last25 = int(str(result5)[-2:])
        lottery_list.append(last25)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       6:      ")
    for i in range(3):
        result6 = random.randint(100,999)        
        XosoBox.insert(tkinter.END, str(result6) + " ")
        last26 = int(str(result6)[-2:])
        lottery_list.append(last26)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.insert(tkinter.END, "       7:      ")
    for i in range(4):
        result7 = random.randint(10,99)        
        XosoBox.insert(tkinter.END, str(result7) + " ")
        last27 = int(str(result7)[-2:]) 
        lottery_list.append(last27)
    XosoBox.insert(tkinter.END, "\n")

    XosoBox.config(state="disabled")  
    # print(lottery_list)
    # A = []
    result = int(str(number)[-2:])
    
    player_balance -= bet
    textbox5.config(state='normal')
    textbox5.delete(0, tkinter.END)
    textbox5.insert(tkinter.END, player_balance)
    textbox5.config(state='disabled')

    for i in range(len(lottery_list)):
        if result == lottery_list[i]:
            # A.append(lottery_list[i])        
            player_balance += bet
        
    textbox5.config(state='normal')
    textbox5.delete(0, tkinter.END)
    textbox5.insert(tkinter.END, player_balance)
    textbox5.config(state='disabled')
    # print(A) 
        
    if player_balance <= 0:
        textbox5.delete(0, tkinter.END)
        XosoBox.config(state="normal")
        XosoBox.delete(1.0, tkinter.END)
        XosoBox.config(state="disabled")
        miniwindow()

Title = tkinter.Label(Lode, text="Trò chơi Lô đề", font=("Times New Roman",20))
Title.grid(column=3,row=1)
# Tang 1-------------------------------
Lo = tkinter.Label(Lode, text="I.Chơi Lô", font=("Times New Roman",14))
Lo.grid(column=1,row=2)

ChonSo1 = tkinter.Label(Lode, text="Chọn số:", font=("Times New Roman",14), justify="center")
ChonSo1.grid(column=1, row=3)
number1 = tkinter.IntVar()
textbox1 = tkinter.Entry(Lode, textvariable=number1, font=("Times New Roman",14),width = 20)
textbox1.grid(column=2, row=3)

ChonDiem1 = tkinter.Label(Lode, text="Đánh mấy điểm:", font=("Times New Roman",14), justify="center")
ChonDiem1.grid(column=3, row=3)
point1 = tkinter.IntVar()
textbox2 = tkinter.Entry(Lode, textvariable=point1, font=("Times New Roman",14),width = 20)
textbox2.grid(column=4, row=3)

Button1 = tkinter.Button(Lode, text="Chơi đi đừng sợ", font=("Times New Roman",12), command=play_lo)
Button1.grid(column=3,row=4)

oneEqual23 = tkinter.Label(Lode, text="1 điểm = 23.000 VND", font=("Times New Roman",10))
oneEqual23.grid(column=4,row=4)

# Tang 2-------------------------------
De = tkinter.Label(Lode, text="II.Chơi Đề", font=("Times New Roman",14))
De.grid(column=1,row=5)

ChonSo2 = tkinter.Label(Lode, text="Chọn số:", font=("Times New Roman",14), justify="center")
ChonSo2.grid(column=1, row=6)
number2 = tkinter.IntVar()
textbox3 = tkinter.Entry(Lode, textvariable=number2, font=("Times New Roman",14),width = 20)
textbox3.grid(column=2, row=6)

ChonDiem2 = tkinter.Label(Lode, text="Đánh mấy điểm:", font=("Times New Roman",14), justify="center")
ChonDiem2.grid(column=3, row=6)
point2 = tkinter.IntVar()
textbox4 = tkinter.Entry(Lode, textvariable=point2, font=("Times New Roman",14),width = 20)
textbox4.grid(column=4, row=6)

Button2 = tkinter.Button(Lode, text="Chơi đi đừng sợ", font=("Times New Roman",12), command=play_de)
Button2.grid(column=3,row=7)

oneEqual1 = tkinter.Label(Lode, text="1 điểm = 1.000 VND", font=("Times New Roman",10))
oneEqual1.grid(column=4,row=7)
# tâng 3---------------------------
XosoBox = ScrolledText(Lode, width = 50, height = 10, font=("Times New Roman",14))
XosoBox.grid(column=2,row=9,columnspan=3,pady=20)
XosoBox.config(state="disabled")

total = tkinter.Label(Lode, text="Tổng tiền: 1.000.000 VND", font=("Times New Roman",14))
total.grid(column=1,row=11,columnspan=2)

Sotienconlai = tkinter.Label(Lode, text="Số tiền còn lại:", font=("Times New Roman",14))
Sotienconlai.grid(column=1,row=12)
moneyLeft = StringVar()
textbox5 = tkinter.Entry(Lode, textvariable=moneyLeft, font=("Times New Roman",14))
textbox5.grid(column=2,row=12)
textbox5.config(state="disabled")
Lode.mainloop()

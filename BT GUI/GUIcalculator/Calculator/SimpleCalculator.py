import tkinter
from tkinter import *
from tkinter import ttk
# Functions-----------------------
class Calculator:
    calc_value = 0.0
    cong = False
    tru = False
    nhan = False 
    chia = False
    chiadu = False

    def num_press(self, value):
        giatriSo = self.Ketqua.get()
        if value != "C":
            giatriSo += value
            self.Ketqua.delete(0, END)
            self.Ketqua.insert(0, giatriSo)
        else:
            giatriSo = ""
            self.Ketqua.delete(0, END)
            self.Ketqua.insert(0, giatriSo)
       
    def isFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def math_press(self, value):
        if self.isFloat(str(self.Ketqua.get())):
            self.cong = False
            self.tru = False
            self.nhan = False 
            self.chia = False
            self.chiadu = False
            self.calc_value = float(self.giatri.get())
            if value == "+":
                self.cong = True
            elif value == "-":
                self.tru = True
            elif value == "*":
                self.nhan = True
            elif value == "%":
                self.chiadu = True
            else:
                self.chia = True
            self.Ketqua.delete(0, END)

    def equal_button(self):
        if self.cong or self.tru or self.nhan or self.chia or self.chiadu:
            if self.cong:
                equaltion = self.calc_value + float(self.giatri.get())
            elif self.tru:
                equaltion = self.calc_value - float(self.giatri.get())
            elif self.nhan:
                equaltion = self.calc_value * float(self.giatri.get())            
            elif self.chiadu:
                equaltion = self.calc_value % float(self.giatri.get())
            else:
                equaltion = self.calc_value / float(self.giatri.get())
            self.Ketqua.delete(0, END)
            self.Ketqua.insert(0, equaltion)     

    def __init__(self, Calc) :
        Calc.title("Calcultor")
        Calc.geometry("520x500")
        Calc.resizable(width=False, height=False)
        # Row1-----------------
        self.giatri = StringVar()
        self.Ketqua = tkinter.Entry(Calc, textvariable=self.giatri, width=36, fg='Black', font=15, border=3)
        self.Ketqua.grid(column=1, row=1, columnspan=3, padx=10, pady=10)

        self.Clear = tkinter.Button(Calc, text="C", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("C"))
        self.Clear.grid(column=4, row=1, padx=5, pady=5)
        # Row2-----------------
        self.Nine = tkinter.Button(Calc, text="9", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("9"))
        self.Nine.grid(column=1, row=2, padx=10, pady=10)

        self.Eight = tkinter.Button(Calc, text="8", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("8"))
        self.Eight.grid(column=2, row=2, padx=10, pady=10)

        self.Seven = tkinter.Button(Calc, text="7", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("7"))
        self.Seven.grid(column=3, row=2, padx=10, pady=10)

        self.Cong = tkinter.Button(Calc, text="+", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.math_press("+"))
        self.Cong.grid(column=4, row=2, padx=10, pady=10)
        # Row2-----------------
        self.Six = tkinter.Button(Calc, text="6", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("6"))
        self.Six.grid(column=1, row=3, padx=10, pady=10)

        self.Five = tkinter.Button(Calc, text="5", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("5"))
        self.Five.grid(column=2, row=3, padx=10, pady=10)

        self.Four = tkinter.Button(Calc, text="4", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("4"))
        self.Four.grid(column=3, row=3, padx=10, pady=10)

        self.Tru = tkinter.Button(Calc, text="-", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.math_press("-"))
        self.Tru.grid(column=4, row=3, padx=10, pady=10)
        # Row3-----------------
        self.Three = tkinter.Button(Calc, text="3", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("3"))
        self.Three.grid(column=1, row=4, padx=10, pady=10)

        self.Two = tkinter.Button(Calc, text="2", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("2"))
        self.Two.grid(column=2, row=4, padx=10, pady=10)

        self.One = tkinter.Button(Calc, text="1", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("1"))
        self.One.grid(column=3, row=4, padx=10, pady=10)

        self.Nhan = tkinter.Button(Calc, text="*", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.math_press("*"))
        self.Nhan.grid(column=4, row=4, padx=10, pady=10)
        # Row4-----------------
        self.Zero = tkinter.Button(Calc, text="0", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("0"))
        self.Zero.grid(column=1, row=5, padx=10, pady=10)

        self.doubleZero = tkinter.Button(Calc, text="00", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("00"))
        self.doubleZero.grid(column=2, row=5, padx=10, pady=10)

        self.Dot = tkinter.Button(Calc, text=".", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.num_press("."))
        self.Dot.grid(column=3, row=5, padx=10, pady=10)

        self.Chia = tkinter.Button(Calc, text="/", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.math_press("/"))
        self.Chia.grid(column=4, row=5, padx=10, pady=10)
        # Row5
        self.Equal = tkinter.Button(Calc, text="=", fg='black', width=38, height=2, 
                                    font=15, border=3, command=lambda: self.equal_button())
        self.Equal.grid(column=1, row=6, columnspan=3, padx=10, pady=10)

        self.ChiaDu = tkinter.Button(Calc, text="%", fg='black', width=10, height=2, 
                                    font=15, border=3, command=lambda: self.math_press("%"))
        self.ChiaDu.grid(column=4, row=6, padx=10, pady=10)   

Maytinh = tkinter.Tk()
calculator = Calculator(Maytinh)
Maytinh.mainloop()
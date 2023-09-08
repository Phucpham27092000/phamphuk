import requests
import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk
import getAPIdata
from getAPIdata import *
import datetime

root = tk.Tk()
root.title("Weather Application")
root.geometry('800x520')
root.minsize(800,520)
root.maxsize(800,520)
 
def Hienthi():    
    city = str(value.get())
    getWeatherData(city)
    thanhpho.set("")    
    thanhpho.set(DATA[0]+', '+DATA[1])

    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    date = str(current_date)
    ngayThang.set("")
    ngayThang.set(date)    

    TrangthaiTT.set("")
    TrangthaiTT.set(DATA[2])

    NhietdoC.set("")
    NhietdoC.set(DATA[3])

    NhietdoF.set("")
    NhietdoF.set(DATA[4])

    DoAm.set("")
    DoAm.set(str(DATA[5])+"%")

    Sucgio.set("")
    Sucgio.set(DATA[6])

# ['Hanoi', 'VN', 'Clouds', '32.0°C', '89.6°F', 75, 4.32]

# 1st Area

row1 = tk.Frame(root,bg='dodgerblue4')
row1.pack(fill="both")

weather = tk.Label(row1,text="Weather Report", font=('Ariel',15,'bold'), fg='white', bg='dodgerblue4')
weather.pack(padx=20,pady=20)

thanhpho = tk.StringVar()
location = tk.Label(row1, textvariable=thanhpho, font=('Ariel',15,'bold'), justify='left', fg='white', bg='dodgerblue4')
location.place(x=20,y=20)
thanhpho.set("NA/-")

ngayThang = tk.StringVar()
day = tk.Label(row1, textvariable=ngayThang, font=('Ariel',15,'bold'), justify='right', fg='white', bg='dodgerblue4')
day.place(x=650,y=20)
ngayThang.set("YYYY-MM-DD")

# 2nd Area

img1_path = "weather.jpg"
newImg1_path = "newWeather.jpg"
img1 = Image.open(img1_path)
newImg1 = img1.resize((150,150))
newImg1.save(newImg1_path)
img1_tk = ImageTk.PhotoImage(newImg1)

Picture1 = tk.Label(root, image=img1_tk)
Picture1.place(x=50, y=80)

timKiem = tk.Label(root, text="City or Country Name", font=('Ariel',15,'bold'), fg='dodgerblue4')
timKiem.place(x=250, y=100)
value = tk.StringVar()
Search = tk.Entry(root, textvariable=value, font=('Ariel',18), width=18)
Search.place(x=250, y=150)

Nut = tk.Button(root, text="Search", font=('Ariel',12,'bold'), width=10, height=1, command=Hienthi)
Nut.place(x=500, y=150)

# 3rd Area

row3 = tk.Frame(root, bg='dodgerblue4')
row3.pack(fill='both', pady=180)

thirdRow = tk.Label(row3, text="Weather Report", font=('Ariel',15,'bold'), fg='white', bg='dodgerblue4')
thirdRow.pack(padx=10, pady=10)

# 4th Area

img2_path = "state.jpg"
newImg2_path = "newState.jpg"
img2 = Image.open(img2_path)
newImg2 = img2.resize((100,100))
newImg2.save(newImg1_path)
img2_tk = ImageTk.PhotoImage(newImg2)

img3_path = "temp.jpg"
newImg3_path = "newTemp.jpg"
img3 = Image.open(img3_path)
newImg3 = img3.resize((100,100))
newImg3.save(newImg3_path)
img3_tk = ImageTk.PhotoImage(newImg3)

img4_path = "humid.jpg"
newImg4_path = "newHumid.jpg"
img4 = Image.open(img4_path)
newImg4 = img4.resize((100,100))
newImg4.save(newImg4_path)
img4_tk = ImageTk.PhotoImage(newImg4)

img5_path = "wind.jpg"
newing5_path = "newWind.jpg"
img5 = Image.open(img5_path)
newing5 = img5.resize((100,100))
newing5.save(newing5_path)
img5_tk = ImageTk.PhotoImage(newing5)
 
Picture2 = tk.Label(root, image=img2_tk)
Picture2.place(x=80, y=320)
TrangthaiTT = tk.StringVar()
State = tk.Label(root, textvariable=TrangthaiTT, font=('Ariel',15,'bold'), width=10)
State.place(x=75, y=430)
TrangthaiTT.set("NA/-")

Picture3 = tk.Label(root, image=img3_tk)
Picture3.place(x=260, y=320)
NhietdoC = tk.StringVar()
Temp = tk.Label(root, textvariable=NhietdoC, font=('Ariel',15,'bold'), width=10)
Temp.place(x=255, y=430)
NhietdoF = tk.StringVar()
Temp = tk.Label(root, textvariable=NhietdoF, font=('Ariel',15,'bold'), width=10)
Temp.place(x=255, y=460)
NhietdoC.set("NA/-")

Picture4 = tk.Label(root, image=img4_tk)
Picture4.place(x=440, y=320)
DoAm = tk.StringVar()
Humid= tk.Label(root, textvariable=DoAm, font=('Ariel',15,'bold'), width=10)
Humid.place(x=435, y=430)
DoAm.set("NA/-")

Picture5 = tk.Label(root, image=img5_tk)
Picture5.place(x=620, y=320)
Sucgio = tk.StringVar()
Wind = tk.Label(root, textvariable=Sucgio, font=('Ariel',15,'bold'), width=10)
Wind.place(x=615, y=430)
Sucgio.set("NA/-")

root.mainloop()
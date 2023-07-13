import DinhNghia

ketnoi = DinhNghia.getConnection()
data = ketnoi.cursor()

def checkConnect():
    ketnoi.commit()
    if ketnoi.is_connected():
        return "Connection successed!"
    else: 
        return "Connection failed"
    
def getData():
    data.execute("SELECT * FROM quanlynhanvien.Company")
    ketqua = data.fetchall()
    danhSach = []
    for i in ketqua:        
        kq = list(i)        
        a = kq[-1]
        b = kq[-2]
        if b == 'NV':
            kq[-2] = 'Nhan vien'
            Salary = int(300000 * a * 1)       
        elif b == 'TP':
            kq[-2] = 'Truong phong'
            Salary = int(300000 * a * 1.6)          
        elif b == 'GD':
            kq[-2] = 'Giam doc'
            Salary = int(300000 * a * 2)           
        kq.append(Salary)                  
        danhSach.append(kq)
    return danhSach

def createData(name,age,sex,country,Chucvu,Songaylam):
    sql = "INSERT INTO quanlynhanvien.Company (`Name`,Age,Sex,Country,Chucvu,Songaylam) VALUES (%s, %s, %s, %s, %s, %s)"
    data.execute(sql,(name,age,sex,country,Chucvu,Songaylam,))
    ketnoi.commit()

def updateData(id,name,age,sex,country,Chucvu,Songaylam):
    sql = "UPDATE quanlynhanvien.Company SET `Name` = %s, Age = %s, Sex = %s, Country = %s, Chucvu = %s, Songaylam = %s WHERE ID = %s"
    data.execute(sql,(name,age,sex,country,Chucvu,Songaylam,id,))
    ketnoi.commit()

def deleteData(id):
    sql = "DELETE FROM quanlynhanvien.Company WHERE ID = %s"
    data.execute(sql,(id,))
    ketnoi.commit()

def name(danhSach):
    return danhSach[1]

def salary(danhSach):
    return danhSach[-1]

def sortByName():
    DS = getData()
    DS.sort(key=name, reverse=False)
    return DS
        
def sortBySalary():
    DS = getData()
    DS.sort(key=salary, reverse=True)
    return DS
        
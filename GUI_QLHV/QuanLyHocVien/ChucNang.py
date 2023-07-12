import DInhNghia
ketnoi = DInhNghia.getConnection()
data = ketnoi.cursor()

def checkConnect():
    ketnoi.commit()
    if ketnoi.is_connected():
        return "Connection successed!"
    else: 
        return "Connection failed"    

def getAllData():
    data.execute("SELECT * FROM quanlyhocvien.student")
    result = data.fetchall()
    Danhsach = []
    for i in result:
        j = list(i) 
        Danhsach.append(j)
    return Danhsach    

def createData(name,age,sex,country,info,eng):
    sql = "INSERT INTO Student (`Name`, Age, Sex, Country, English, Information) VALUES (%s,%s,%s,%s,%s,%s)"
    data.execute(sql,(name,age,sex,country,eng,info,))
    ketnoi.commit()
    # print("ADD SUCCESS!")

def updateDatabyID(id,name,age,sex,country,info,eng):
    sql = "UPDATE quanlyhocvien.student SET `Name` = %s, Age = %s, Sex = %s, Country = %s, English = %s, Information = %s WHERE Id = %s"
    data.execute(sql,(name,age,sex,country,eng,info,id,))
    ketnoi.commit()
    # print("UPDATE SUCCESS!")

def deleteDatabyID(id):
    sql = "DELETE FROM quanlyhocvien.student WHERE Id = %s"
    data.execute(sql,(id,))
    ketnoi.commit()
    # print("DELETE SUCCESS!")


        
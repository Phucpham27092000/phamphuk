import DInhNghia
ketnoi = DInhNghia.getConnection()
data = ketnoi.cursor()

def getAllData():
    data.execute("SELECT * FROM quanlyhocvien.student")
    result = data.fetchall()
    Danhsach = []
    for i in result:
        print(i)

def createData(name,age,country,info,eng):
    sql = "INSERT INTO Student (`Name`, Age, Country, English, Information) VALUES (%s, %s, %s, %s, %s)"
    data.execute(sql,(name,age,country,eng,info,))
    ketnoi.commit()
    print("ADD SUCCESS!")

def updateDatabyID(id,name,age,country,info,eng):
    sql = "UPDATE quanlyhocvien.student SET `Name` = %s, Age = %s, Country = %s, English = %s, Information = %s WHERE Id = %s"
    data.execute(sql,(name,age,country,eng,info,id,))
    ketnoi.commit()
    print("UPDATE SUCCESS!")

def deleteDatabyID(id):
    sql = "DELETE FROM quanlyhocvien.student WHERE Id = %s"
    data.execute(sql,(id,))
    ketnoi.commit()
    print("DELETE SUCCESS!")

        
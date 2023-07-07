from ChucNang import *
while True:
    print("__________________________")
    print()
    print("1. Them thong tin hoc vien")
    print("2. Hien thi danh sach hoc vien")
    print("3. Thay doi thong tin hoc vien theo ID")
    print("4. Xoa thong tin hoc vien theo ID")
    print("0. Thoat chuong trinh")
    print("__________________________")

    opt = int(input("Nhap lua chon: "))
    if opt == 1:
        addName = input("Nhap ten: ")
        addAge = int(input("Nhap tuoi: "))
        addCountry = input("Nhap que quan: ")
        addEng = float(input("Nhap diem Tieng Anh: "))
        addInfo = input("Nhap diem thong tin: ")
        print("__________________________")
        print()
        createData(addName,addAge,addCountry,addEng,addInfo)
        print("__________________________")
    elif opt == 2:
        print("__________________________")
        print()
        getAllData()
        print("__________________________")
    elif opt == 3:
        newId = int(input("Nhap ID: "))
        newName = input("Nhap ten: ")
        newAge = int(input("Nhap tuoi: "))
        newCountry = input("Nhap que quan: ")
        newEng = float(input("Nhap diem Tieng Anh: "))
        newInfo = input("Nhap ghi chu: ")
        print("__________________________")
        print()
        updateDatabyID(newId,newName,newAge,newCountry,newEng,newInfo)
        print("__________________________")
    elif opt == 4:
        xoaId = int(input("Nhap ID cua hoc vien can xoa: "))
        print("__________________________")
        print()
        deleteDatabyID(xoaId)
        print("__________________________")
    elif(opt == 0):
        ketnoi.close()
        print("__________________________")
        print()
        print("Da thoat chuong trinh")
        print("__________________________")
        break
    else:
        print("Lua chon khong hop le, hay nhap lai")

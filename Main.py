from chucNang import QuanLyNhanVien

qlnv = QuanLyNhanVien()
while True:
    print("|--------------------------------------------------------|")
    print("| 1. Them thong tin nhan vien                            |")
    print("| 2. Thay doi thong tin nhan vien                        |")
    print("| 3. Xoa thong tin nhan vien                             |")
    print("| 4. Hien thi danh sach nhan vien                        |")
    print("| 5. Sap xep nhan vien theo thu tu tang dan theo ten     |")
    print("| 6. Sap xep nhan vien theo thu tu giam dan theo ten     |")
    print("| 7. Tim nhan vien theo ID                               |")
    print("| 0. Thoat                                               |")
    print("|--------------------------------------------------------|")
     
    key = int(input("Nhap tuy chon: "))

    if (key == 1):
        qlnv.ThemNhanVien()
        print("\nThem sinh vien thanh cong!")

    elif (key == 2):
        oldTen = input("Nhap ten can sua: ")
        oldTuoi = int(input("Nhap tuoi can sua: ")) 
        oldQuequan = input("Nhap que quan can sua:")
        newTen = input("Nhap ten moi: ")
        newTuoi = int(input("Nhap tuoi moi: "))
        newQuequan = input("Nhap que quan moi: ")
        qlnv.SuaNhanVien(oldTen, oldTuoi, oldQuequan, newTen, newTuoi, newQuequan)
    
    elif (key == 3):        
        xoaNV = input("Nhap ten nhan vien can xoa: ")
        qlnv.XoaNhanVien(xoaNV)
        print("----------------------------------------------")
        print("\nDanh sach nhan vien sau khi xoa nhan vien co ten {}: ".format(xoaNV))
        qlnv.showNhanVien(qlnv.getListNhanVien())
        print("----------------------------------------------")

    elif (key == 4):
        print("----------------------------------------------")
        print("\nDanh sach nhan vien: ")
        qlnv.showNhanVien(qlnv.getListNhanVien())
        print("----------------------------------------------")

    elif (key == 5):        
        print("----------------------------------------------")
        print("\nDanh sach nhan vien sau khi sap xep tang dan: ")
        qlnv.sapXepNVTangTheoTen()
        qlnv.showNhanVien(qlnv.getListNhanVien())
        print("----------------------------------------------")
        
    elif (key == 6):
        print("----------------------------------------------")
        print("\nDanh sach nhan vien sau khi sap xep giam dan: ")
        qlnv.sapXepNVGiamTheoTen()
        qlnv.showNhanVien(qlnv.getListNhanVien())
        print("----------------------------------------------")

    elif (key == 7):
        FindID = input("Nhap ID nhan ven can tim: ")
        searchResult = qlnv.findByID(FindID)
        qlnv.showNhanVien(searchResult)    
        
    elif (key == 0):
        print("\nThoat chuong trinh!")
        break
    else:
       print("\nLua chon khong hop le, hay nhap lai")

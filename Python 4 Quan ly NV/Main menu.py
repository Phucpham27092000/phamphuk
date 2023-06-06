from Chuc_nang import QuanLyNhanVien

test = QuanLyNhanVien()

while True:
    print("|--------------------------------------------------------|")
    print("| 1. Them thong tin nhan vien                            |")
    print("| 2. Thay doi thong tin nhan vien                        |")
    print("| 3. Xoa thong tin nhan vien                             |")
    print("| 4. Hien thi danh sach nhan vien                        |")
    print("| 5. Sap xep nhan vien theo thu tu tang dan theo ten     |")
    print("| 6. Sap xep nhan vien theo thu tu giam dan theo ten     |")
    # print("| 7. Tim nhan vien theo ID                               |")
    print("| 0. Thoat                                               |")
    print("|--------------------------------------------------------|")
    option = int(input("Nhap lua chon: "))

    if option == 1:
        test.ThemNhanVien()
    
    elif option == 2:
        oldTen = input("Nhap ten can sua: ")
        oldTuoi = int(input("Nhap tuoi can sua: ")) 
        oldQuequan = input("Nhap que quan can sua:")
        newTen = input("Nhap ten moi: ")
        newTuoi = int(input("Nhap tuoi moi: "))
        newQuequan = input("Nhap que quan moi: ")
        test.SuaNhanVien(oldTen, oldTuoi, oldQuequan, newTen, newTuoi, newQuequan)

    elif option == 3:
        xoaNV = input("Nhap ten nhan vien can xoa: ")
        test.XoaNhanVien(xoaNV)
        print("----------------------------------------------")
        print("Danh sach nhan vien sau khi xoa nhan vien co ten {}: ".format(xoaNV))
        test.HienThiNhanVien()
        print("----------------------------------------------")
    
    elif option == 4:
        print()
        print("----------------------------------------------")
        print("Danh sach nhan vien: ")
        test.HienThiNhanVien()
        print("----------------------------------------------")
        print()

    elif option == 5:
        test.sapXepNVTangTheoTen()
        print("----------------------------------------------")
        print("Danh sach nhan vien sau khi sap xep tang dan: ")
        test.HienThiNhanVien()
        print("----------------------------------------------")
    
    elif option == 6:
        test.sapXepNVGiamTheoTen()
        print("----------------------------------------------")
        print("Danh sach nhan vien sau khi sap xep giam dan: ")
        test.HienThiNhanVien()
        print("----------------------------------------------")

    # elif option == 7:
    #     FindID = input("Nhap ID nhan ven can tim: ")
    #     FindResult = test.TimkiemTheoID(FindID)
    #     test.HienThiNhanVien(FindResult)

    elif option == 0:
        print("Da thoat chuong trinh")
        break

    else:
        print("Lua chon khong hop le, hay nhap lai")
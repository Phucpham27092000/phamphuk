from dinhNghia import CongTy
class QuanLyNhanVien:
    listNhanVien = []
    count = {}
    def ThemNhanVien(self):
        n = int(input("Nhap so luong nhan vien: "))

        for i in range (1, n+1):
            print("-------------------------------------")
            print("Nhap nhan vien thu {}".format(i))

            ten = input("Nhap ten: ")
            tuoi = int(input("Nhap tuoi: "))
            quequan = input("Nhap que quan: ")
            chucvu = input("Nhap chuc vu: ")
            chamcong = int(input("Nhap so ngay cham cong: "))

            NV = CongTy(ten, tuoi, quequan, chucvu, chamcong)

            # ID: Chucvu + maso
            if NV.chucvu not in QuanLyNhanVien.count:
                QuanLyNhanVien.count[NV.chucvu] = 1
            else:
                QuanLyNhanVien.count[NV.chucvu] += 1

            id_number = QuanLyNhanVien.count[NV.chucvu]
            NV.ID = NV.chucvu + str(id_number)

            # Tinh luong
            heso = 0            
            if chucvu == 'NV':
                heso = 1
                NV.chucvu = 'Nhan vien'
            elif chucvu == 'TP':
                heso = 1.5
                NV.chucvu = 'Truong phong'
            elif chucvu == 'GD':
                heso = 2
                NV.chucvu = 'Giam doc'
            NV.luong = int(300000 * chamcong * heso)

            self.listNhanVien.append(NV)
 
    def soLuongNhanVien(self):
        return self.listNhanVien.__len__()
 
    def SuaNhanVien(self,ten, tuoi, quequan, newTen, newTuoi, newQuequan):
        for NV in self.listNhanVien:
            if NV.ten == ten and NV.tuoi == tuoi and NV.quequan == quequan:
                NV.ten = newTen
                NV.tuoi = newTuoi
                NV.quequan = newQuequan
    
    def XoaNhanVien(self, ten):
        for NV in self.listNhanVien:
            if NV.ten == ten:
                self.listNhanVien.remove(NV)

    def sapXepNVTangTheoTen(self):
        self.listNhanVien.sort(key=lambda x: x.ten, reverse=False)

    def sapXepNVGiamTheoTen(self):
        self.listNhanVien.sort(key=lambda x: x.ten, reverse=True)
 
    def findByID(self, keyword):
        listNV = []
        if (self.soLuongNhanVien() > 0):
            for i in self.listNhanVien:
                if (keyword.upper() in i.ID.upper()):
                    listNV.append(i)
        return listNV
 
    def showNhanVien(self, listNV):
        print("{:<10}{:<20}{:<10}{:<15}{:<15}{:<10}{:<20}"
              .format("ID","Ten","Tuoi","Que quan","Chuc vu","Cham cong","Luong"))

        if (listNV.__len__() > 0):
            for i in listNV:
                print("{:<10}{:<20}{:<10}{:<15}{:<15}{:<10}{:<20}"
                      .format(i.ID, i.ten, i.tuoi, i.quequan, i.chucvu, i.chamcong, i.luong))

    def getListNhanVien(self):
        return self.listNhanVien
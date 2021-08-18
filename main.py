import datetime

class Laundry:

    def __init__(self, name, addr, phoneNumber, laundryWeight):
        self.nama = name
        self.alamat = addr
        self.telp = phoneNumber
        self.beratCucian = laundryWeight
        self.tanggalMasuk = datetime.datetime.now()
        self.estAmbil=0
        self.biaya = 0
    
    def cetakStruk(self):
        print('='*10 + ' Order Details ' + '='*10)
        print('Nama             : {}'.format(self.nama))
        print('Berat cucian     : {}'.format(self.beratCucian))
        print('Tanggal Diterima : {}'.format(self.tanggalMasuk.strftime('%c')))
        print('Tanggal Ambil    : {}'.format(self.estAmbil.strftime('%c')))
        print('Total Biaya      : Rp {}'.format(self.biaya))
        print('='*10 + ' Terima kasih ' + '='*10)

class LaundryKilat(Laundry):

    def __init__(self, name, addr, phoneNumber, laundryWeight):
        super().__init__(name, addr, phoneNumber, laundryWeight)
        self.biaya = self.beratCucian * 7500
        self.estAmbil = self.tanggalMasuk + datetime.timedelta(days=2)
    
    def cetakStruk(self):
        return super().cetakStruk()

class LaundryNormal(Laundry):
    def __init__(self, name, addr, phoneNumber, laundryWeight):
        super().__init__(name, addr, phoneNumber, laundryWeight)
        self.biaya = self.beratCucian * 3500
        self.estAmbil = self.tanggalMasuk + datetime.timedelta(days=4)
    
    def cetakStruk(self):
        return super().cetakStruk()
        

def main():


    while True:
        
        try:
            layanan = input('Pilih layanan \"normal / kilat\" :')
            if layanan != 'normal' and layanan != 'kilat':
                raise Exception
        except Exception:
            print('masukkan jenis layanan secara benar')
            continue

        namaCust = input('Masukkan nama cutomer : ')
        alamatCust = input('Masukkan alamat customer :')
        telpCust = input('Masukkan nomor telefon customer :')
        beratCucian = int (input('Masukkan berat cucian customer :'))

        if layanan == 'normal':
            cust = LaundryNormal(namaCust, alamatCust, telpCust, beratCucian)
        else:
            cust = LaundryKilat(namaCust, alamatCust, telpCust, beratCucian)

        cetak = input('Apakah anda ingin mencetak struk (y/n): ')
        if cetak == 'y' :
            cust.cetakStruk()
        else:
            continue
        
        
if __name__ == "__main__":
    main()

        
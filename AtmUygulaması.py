bakiye=10000

while True:
    islem = input('ATM UYGULAMASI\nYapmak İstediğiniz İşlemi Seçin\n1)Bakiye Sorgula\n2)Para Yatır\n3)Para Çek')
    
    if islem == 'q':
        print('Çıkışınız Yapıldı.')
        break
    if islem == '1':
        print('Bakiye:',bakiye)
    elif islem == '2':
        yatirilanpara=int(input('Yatırmak İstediğiniz Miktarı Girin:'))
        bakiye = yatirilanpara + bakiye
        print('Mevcut Bakiyeniz:',bakiye)
    elif islem == '3':
      cekilecekpara = int(input('Çekmek İstediğiniz Miktarı Girin:'))
      if(cekilecekpara>bakiye):
          print('Yetersiz Bakiye')
          continue
      bakiye -= cekilecekpara
      print('Mevcut Bakiyeniz:',bakiye)
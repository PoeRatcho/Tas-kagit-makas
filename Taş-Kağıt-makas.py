while True:

    print("""
TAS-KAGIT-MAKAS OYUNUNA HOŞGELDİNİZ.
YAPMANIZ GEREKEN TEK ŞEY SEÇİMİNİZİ YAPMAK.
""")
    import random
    
    try:

        ifadeler = ["taş" , "kağit" , "makas"]
        taş = ifadeler[0]
        kağit = ifadeler[1]
        makas = ifadeler[2]
        veri = input("Lütfen Seçiminizi Yapiniz...: Taş , Kağit , Makas: ")
        pc = random.choice(ifadeler)
        if veri == taş:
            if pc == taş:
                print("Bilgisayar Taş Seçti Berabere")
            elif pc == kağit:
                print("Bilgisayar Kağit Seçti Kaybettiniz.")
            elif pc == makas:
                print("Bilgisayar Makas Seçti Kazandiniz.")
        elif veri == kağit:
            if pc == taş:
                print("Bilgisayar Taş Seçti Kazandiniz.")
            elif pc == kağit:
                print("Bilgisayar Kağit Seçti Berabere.")
            elif pc == makas:
                print("Bilgisayar Makas Seçti Kaybettiniz.")
        elif veri == makas:
            if pc == taş:
                print("Bilgisayar Taş Seçti Kaybettiniz.")
            elif pc == kağit:
                print("Bilgisayar Kağit Seçti Kazandiniz.")
            elif pc == makas:
                print("Bilgisayar Makas Seçti Berabere.")
    except veri != ifadeler:
        print("Lütfen Sadece İfadenizi Seçiniz Farkli Bir Argüman Girmeyiniz...")
        break
    





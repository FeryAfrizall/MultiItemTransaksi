# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:32:28 2021

@author: hp
"""
jwb = "Y"
while jwb=="y" or jwb=="Y":  
    print("")
    print("========================================")
    print(" DAFTAR MENU ")
    print(" Kantin Fk Tek. Informasi ")
    print("========================================")
    print("")
    print("========================================")
    print(" Menu Makanan")
    print("========================================")
    print(" a = Nasi Goreng          Rp 15.000")
    print(" b = Lontong Goreng       Rp 14.900")
    print(" c = Bakso Goreng         Rp 12.900")
    print(" d = Rujak Goreng         Rp 13.000")
    print(" e = Rujak Bakso          Rp 15.000")
    print(" f = Rujak Bakso Pecel    Rp 17.000")
    print("========================================")
    print("")
    print("========================================")
    print(" Menu Minuman")
    print("========================================")
    print(" a1 = Teh Dingin/Hangat   Rp 2.500")
    print(" b2 = Kopi Dingin         Rp 5.000")
    print(" c3 = Kopi Teh Panas      Rp 6.500")
    print(" d4 = Coca Cola Dingin    Rp 3.500")
    print(" e5 = Coca Cola Panas     Rp 5.000")
    print("========================================")

    kode =['a','b','c','d','e','f']
    namaBarang = [' NasI Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
    harga = [15000,14900,12900,13000,15000,17000]
    
    pilihan = input("Masukkan Kode Barang    = ")
    qty     = input("Masukkan Jumlah Barang  = ")

    i = 0
    while i<len(namaBarang):
    
        if kode[i] == pilihan:
            nm_brg = namaBarang[i]
            hrgsat = harga[i]
            i+=1

    kode1 =['a1','b2','c3','d4','e5']
    namaBarang1 = ['Teh Dingin/Hangat','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    harga1 = [2500,5000,6500,3500,5000]
    
    pilihan1 = input("Masukkan Kode Barang    = ")
    qty1     = input("Masukkan Jumlah Barang  = ")

    i = 0
    while i<len(namaBarang1):
    
        if kode1[i] == pilihan:
            nm_brg1 = namaBarang1[i]
            hrgsat1 = harga1[i]
            i+=1
    
    tot_byr = (hrgsat + hrgsat1) * (int(qty) + int(qty1))

    print("Nama Barang      : " + nm_brg )
    print("Harga Barang     : " + str(hrgsat))
    print("Jumlah Barang    : " + qty)
    print(("-------------------------------"))
    print("Total Barang      : " + str(tot_byr)) 
    jwb = input("Mau mengulangi ? y/t = ")
    if jwb=="t" or jwb=="T":
            break
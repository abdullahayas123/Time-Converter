#NOMOR 1
'''
detik dibagi dengan 3600 ==> jam
sisanya dibagi 60 ==> menit
sisanya ==> detik
'''

try :
    seconds = int(input("Masukkan detik : "))                   #inisiasi input berupa integer
    def timeConverter(x):                                       #operasi perhitungan jam, menit, detik
        jam = x//3600           
        x = x%3600
        menit = x//60
        detik = x%60
        return "konversi :", jam, ":", menit, ":", detik        #return value jam, menit, detik

    tuple_1 = timeConverter(seconds)                            #inisiasi tuple dari return fungsi
    (str_1, hours, str_2, minutes, str_3, second) = tuple_1     #unpack tuple
    print(str_1, hours, str_2, minutes, str_3, second)          #print hasil
except :
    print("invalid input")                                      #errorr input jika tidak berupa integer
import random
from kamus import kamus


def kata_valid (kamus) :
    kata = random.choice(kamus)
    while  "-" in kata or ' ' in kata :
        kata = random.choice(kamus)

    return kata.upper ()


def tebak_kata () :
    kata_pilihan = kata_valid(kamus)
    huruf_kata  =  set (kata_pilihan)
    huruf_digunakan = set ()

    while len(huruf_kata) > 0 :

        print ("huruf yang sudah anda gunakan"," ".join(huruf_digunakan))
        list_huruf = [huruf if huruf in huruf_digunakan else '-' for huruf in kata_pilihan ]
        print ("kata tebakan anda : " ,''.join(list_huruf) )
        huruf_input = str (input("silahkan masukkan huruf tebakan anda : ").upper())
        huruf_digunakan.add (huruf_input)

        if huruf_input in huruf_kata :
            huruf_kata.remove(huruf_input)

        elif huruf_input in huruf_digunakan :
            print (f"anda telah menggunankan {huruf_input}, silahkan masukkan huruf lain")

        else :
            print ("invalid input.masukkan huruf yang lain ! ")






tebak_kata()
#import (module)
from cgitb import text
import pyperclip
import random
from difflib import SequenceMatcher
from threading import Timer

#var game ngetik
highscore=0
selesai=False

#Warna & efek teks
class Text:
   purple = '\033[95m'
   cyan = '\033[96m'
   dcyan = '\033[36m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underlinw = '\033[4m'
   end = '\033[0m'

class Kuis:
#constructor Kuis
    def __init__(kuisgame, pertanyaan, jawaban):
        kuisgame.pertanyaan = pertanyaan
        kuisgame.jawaban = jawaban

#list pertanyaan
kumpulan_pertanyaan = [
    "Tindakan/perilaku kita ketika menggunakan perangkat digital, berinteraksi dengan orang lain secara daring.\nMerupakan pengeertian dari?\
    \na) Kewajiban Digital \t\tc) Digital Citizenship \nb) Digital Responsibility \td) Internet Responsibility\n",
    "Contoh perbuatan yang tidak sepantasnya dilakukan di internet adalah?\
    \na) Membuka situs streming drama \t\tc) Bermain game online \nb) Memngkritik suatu postingan tidak bermoral \td) Menyebar berita drama palsu\n",
    "Aku sangat suka menonton kartun Jepang. Tetapi supaya praktis, aku menonton di situs ilegal.\nApakah tindakan 'aku' melanggar Digital Citizenship?\
    \na) Iya \t\t\t\t\tc) Tidak \nb) Tidak, jika situs tidak disebarkan \td) Iya, jika hanya sesekali\n",
    "Apa dampak baik dari internet yang berlandas Digital Citizenship?\
    \na) Orang menjadi lebih suka mengkritik tanpa alasan \tc) Penyebaran berita hoaks dapat terhenti \nb) Kuota yang dipakai menjadi lebih sedikit \t\td) Produk online shop menjadi lebih murah\n",
    "Pilih contoh kasus netizen Indonesia yang melakukan tindakan kurang baik di internet!\
    \na) Penyerbuan microsoft karena Indonesia dikatakan tidak sopan \tc) Penyebaran berita kesuksesan seseorang dalam NFT \nb) Membuat organisasi yang bertujuan membantu sesama \t\td) Mengkritik orang tidak sopan dalam internet\n",
]

lvl1 = ["aku", "kamu", "dia", "baik", "sopan", "ramah", "tolong", "kami", "mereka","bantu"]
lvl2 = ["Menolong", "Membantu", "Bersikap", "Menyapa", "Memahami","Bersama","Setengah","Bermain"]
lvl3 = ["Halilintar", "Legendaris", "Mempercayai", "Berbohong", "Kelelawar","Strategi","Instrumental","Berakhir"]
lvl4 = ["pERcaYa", "baiK", "sOMBong", "BAHAgia", "MeraiH","artistik","ARSItek","sauDARA","SEPUPU","membahayakan","MEMPERMUDAH"]
lvl5 = ["Mengetes?", "ApakahBisa?", "Benar!100", "Seribu1.000", "Tanda34C4","H4Ru5","HARUS","s3M4NGAT"]

#jawaban pertanyaan
acak = [
    Kuis(kumpulan_pertanyaan[0], "c"),
    Kuis(kumpulan_pertanyaan[1], "d"),
    Kuis(kumpulan_pertanyaan[2], "a"),
    Kuis(kumpulan_pertanyaan[3], "c"),
    Kuis(kumpulan_pertanyaan[4], "a"),
]

#mengacak urutan pertanyaan
pjg=len(acak)
pjgacak = random.sample(range(0, pjg), pjg)
pasangan = [
]
for i in pjgacak:
    pasangan.append(acak[i])

#mulai kuis
def mulaikuis(pasangan):
    nilai = 0
    for nomor in pasangan:
        jawab = input("\n"+Text.dcyan+nomor.pertanyaan+Text.purple+"Jawaban >"+Text.end).lower()
        if jawab == nomor.jawaban:
            nilai += 1
    print("Nilai: ", nilai, "/", len(pasangan))
    ulangatautidak()

def ulangatautidak():    
    ulang=input("Ulang Kuis? ("+Text.green+"ya"+Text.end+"/"+Text.red+"tidak"+Text.end+"): ").lower()
    if ulang == "ya":
        pjgacak = random.sample(range(0, pjg), pjg)
        pasangan = [
        ]
        for i in pjgacak:
            pasangan.append(acak[i])
        mulaikuis(pasangan)
    elif ulang == "tidak":
        halamanutama()
    else:
        print("pilihan hanya ya / tidak")
        ulangatautidak()

def gameselesai():
    global selesai
    selesai=True
    print(Text.red+"Waktu habis! Klik tombol enter untuk lanjut."+Text.end)

def HighScore():
    global highscore
    try:
        fileskor = open("highscore.txt", "r")
        highscore = int(fileskor.read())
        fileskor.close()
    except IOError:
        print("Belum ada record skor")
    except ValueError:
        print("Value mengamalmi masalah, skor tertinggi mengulang dari 0")
        highscore=0
 
def HighScoreBaru(nilai):
    try:
        fileskor = open("highscore.txt", "w")
        fileskor.write(str(nilai))
        fileskor.close()
    except IOError:
        print("Tidak dapat menyimpan record skor")

def mulaingetik():
    global selesai
    nilai = 0
    while(selesai==False):
        if nilai in range(0,5):
            batas = 15
            soal=random.choice(lvl1)
        elif nilai in range(6,15):
            batas = 10
            soal=random.choice(lvl2)
        elif nilai in range(16,20):
            batas = 10
            soal=random.choice(lvl3)
        elif nilai in range(21,25):
            batas = 5
            soal=random.choice(lvl4)
        elif nilai >25:
            batas = 5
            soal=random.choice(lvl5)
        
        waktu = Timer(batas,gameselesai)
        waktu.start()
        print(Text.blue+"Ketikan kata: "+Text.end+soal)
        jawab = Text.yellow+"Batas waktu {} detik untuk mengetik\n".format(batas)+Text.end
        jawaban = input(jawab)
        waktu.cancel()
        if(selesai==False):
            if (jawaban == soal):
                print(Text.green+"Jawaban Benar! ^_^\n"+Text.end)
                nilai += 1
            else:
                print(Text.red+"Jawaban Salah v_v\n"+Text.end)
                selesai=True
                HighScore()
                if nilai>highscore:
                    HighScoreBaru(nilai)
                    print("Selamat! anda mencetak skor tertinggi\nDengan Skor: {}".format(nilai))
                else:
                    print("Skor anda : {}\nSkor Tertinggi: {}".format(nilai,highscore))
    selesai=False
    nilai=0
    lagi=input("Ingin bermain lagi? ("+Text.green+"ya"+Text.end+"/"+Text.red+"tidak"+Text.end+"): ").lower()
    if lagi=="ya":
        mulaingetik()
    elif lagi=="tidak":
        halamanutama()
    else:
        print(Text.red+"Input tidak sesuai, anda akan diarahkan kembali ke halaman utama"+Text.end+"")
        halamanutama()   

#list data
inputlimit=["1", "s", "2", "sk","3","h","4","b","5","g","6","sm"]
target=["asu", "goblok", "tolol","bodo","bangsat","kampret","sialan",\
        "idiot","tai","bajingan","sinting","keparat","bego",\
        "fuck","shit","motherfucker","asshole","bitch","ass"]
tandabaca=[".",",","!","~","`","@","#","$","%","^","&","*","(",")","-","_",\
        "+","=","{","}","|",":",";","<",">","?","/","'",'"',"\\","0","1",\
        "2","3","4","5","6","7","8","9"]
tambahan=("""
a) Input tidak diproses dan muncul pesan kesalahan?
        >Ikuti arahan/petunjuk setiap langkah dalam prosesnya    
    \nb) Bagaimana cara kembali ke halaman utama?
        >Input tombol 3/h dalam pertanyaan "Pilih aksi yang ingin dilakukan: "
    \nc) Apa itu perbedaan Sensor normal, kustom, dan mirip?
        >Sensor normal hanya menyensor apa yang sudah saya targetkan (jadi kata kata
        yang disensor sesuai apa yang saya mau)
        >Sensor kustom akan menyensor sesuai apa yang anda input (jangan lupa pisahkan
        dengan spasi sesuai petunjuk saat menggunakan).
        >Sensor mirip, berbeda dengan kedua sensor lainnya, sensor ini tidak hanya menyensor
        kata yang sama persis, tetapi kata mirip juga akan ikut disensor. contohnya kata 
        target sensor adalah kucing, jika dalam teks ada kata khucing,maka akan disensor juga.
    \nc) Hubungan projek dengan Digital Citizenship?
        >Digital Citizenship adalah bagaimana cara kita berperilaku dan menghadapi sesuatu di 
        internet saaat kita sedang online, selain itu kita juga bisa harus bertanggung jawab
        atas apa yang kita lakukan di dunia digital. Nah, project SENSOR! ini membuat kata-kata
        kurang pantas disensor dan membuat percakapan onine menjadi lebih tersortir buruk baiknya
        penyensoran ini juga fleksibel mengikuti keinginan anda maka disediakan 3 tipe.
    """)

homescreen=("""
      ______________________________________________________________
     /                                                               \\
    |    ________________________________________________________     |
    |   |                                                        |    |
    |   |        ____   _____ _   _  ____   ___   ____  __       |    |
    |   |       / ___| | ____| \ | |/ ___| / _ \ |  _ \|  |      |    |
    |   |       \___ \ |  _| |  \| |\___ \| | | || |_) \  |      |    |
    |   |        ___) || |___| |\  |___) || |_| ||  _ < \_|      |    |
    |   |       |____/ |_____|_| \_|____/  \___/ |_| \_\(_)      |    |
    |   |                   _________________                    |    |
    |   |                  /  __________     \                   |    |
    |   |                  | |         /  /| |                   |    |
    |   |                  | |       /  /  | |                   |    |
    |   |                  | |     /  /    | |                   |    |
    |   |________          | |   /  /      | |                   |    |
    |   | by: VS |         | |_/  /________| |                   |    |
    |   |________|         \_________________/                   |    |
    |   |________________________________________________________|    |
    |                                                                 |    
     \_______________________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'               Fungsi Tombol               `-_
          _-'.~.~.~.~.~.~.~.~.~.~..~.~.~.~.~.~..~.~.~..~.~.~.~`-_
       _-'   1/S = Sensor normal       |      4/B = Bantuan      `-_
    _-'      2/SK = Sensor Kustom      |      5/G = Game Kuis       `-_
 _-'         3/H = Halaman Utama       |      6/SM = Sensor Mirip      `-_
:_________________________________________________________________________:
\___._._____________________________________________________________._.___/
""")

halbantuan=("""
    ________________________   ________________________
  /|   _                    \ /                        |\\
||||  |_) _ __ _|_    _ __   |  Sensor Normal: sensor  ||||
||||  |_)(_|| | |_|_|(_|| |  |  kalimat tetapi kata di-||||
||||                         |  sensor berdasarkan yang||||
||||(/'o')/================= |  telah diprogram.       ||||
||||         ABOUT           |                         ||||
|||| SENSOR! adalah project  |  Sensor Kustom: Seperti ||||
|||| sensor kata yang dibuat |  sensor normal tetapi   ||||
|||| untuk mengikuti perlom- |  kata yang disensor se- ||||
|||| baan Code Olympiad 2022 |  suai inputan anda.     ||||
|||| Dibuat dengan mengguna- |                         ||||
|||| kan bahasa Python       |  Halaman Utama: Halaman ||||
||||==================\(^ω^)/|  berisi fungsi tombol.  ||||
||||________________________ | ________________________||||
||/=========================\|/=========================\||
''-------------------------'___'-------------------------''
""")

#function
def sensor():
    teks=input("\nMasukan teks yang ingin"+Text.bold+" disensor normal"+Text.end+": ").lower()
    targett= tuple(target)
    tandabacat= tuple(tandabaca)
    teksakhir = teks.split()
    jumkata=len(teksakhir)
    jumsensor=0
    katadisensor=[]
    hasil = []
    
    for a in teksakhir:
        awal=a
        for t in tandabaca:
            a=a.replace(t,'')
        if a.startswith(targett) or a.endswith(targett) or a in targett:
            if awal.endswith(tandabacat):
                hasil.append("*"*(len(awal)-1)+awal[-1])
                jumsensor+=1
            else:    
                hasil.append("*"*len(awal))
                jumsensor+=1
        #Kata Disensor
            for t in tandabaca:
                    a = a.replace(t,'')
                    a.strip()
            if a not in katadisensor:       
                katadisensor.append(a)
        else:
            hasil.append(a)
    for a in range(55):
        print(Text.purple+'~',end=""+Text.end)  
    detail = Text.yellow+"\no) Jumlah Kata: {} \to) Jumlah Disensor: {} \n\
o) Kata Disensor: {}\n".format(jumkata,jumsensor,", ".join(katadisensor)+Text.end)
    # pyperclip.copy(" ".join(hasil)) gunakan jika pyperclip sudah diinstall
    print(detail)
    print("Hasil: "+Text.cyan+" ".join(hasil)+"\n"+Text.end)
    sensorulang('n')

def sensork():
    print("\nGunakan spasi untuk lebih dari 1 kata."+Text.bold+" Cth: kata1 kata2 kata3"+Text.end)
    sensorkustom = input("Kata yang ingin disensor: ").lower()
    target = sensorkustom.split(" ")
    teks=input("\nMasukan teks yang ingin"+Text.bold+" disensor kustom"+Text.end+": ").lower()
    targett= tuple(target)
    tandabacat= tuple(tandabaca)
    teksakhir = teks.split()
    jumkata=len(teksakhir)
    jumsensor=0
    hasil = []

    for a in teksakhir:
        awal=a
        for t in tandabaca:
            a=a.replace(t,'')
        if a.startswith(targett) or a.endswith(targett) or a in targett:
            if awal.endswith(tandabacat):
                hasil.append("*"*(len(awal)-1)+awal[-1])
                jumsensor+=1
            else:    
                hasil.append("*"*len(awal))
                jumsensor+=1
        else:
            hasil.append(a)
    for a in range(55):
        print(Text.purple+'~',end=""+Text.end)
    detail =Text.yellow+"\no) Jumlah Kata: {} \to) Jumlah Disensor: {} \n\
o) Kata Disensor: {}\n".format(jumkata,jumsensor,", ".join(target)+Text.end)
    # pyperclip.copy(" ".join(hasil)) gunakan jika pyperclip sudah diinstall
    print(detail)
    print("Hasil: "+Text.dcyan+" ".join(hasil)+"\n"+Text.end)
    sensorulang('k')

def sensorm():
    tipe=input("\nIngin sensor secara normal/kustom? (n/k) ").lower()
    if tipe=="n":
        targett= tuple(target)
    elif tipe=="k":
        sensorkustom = input("\nKata yang ingin disensor: ").lower()
        targetk = sensorkustom.split(" ")
        targett= tuple(targetk)
    else:
        print(Text.red+"Pilihan tidak tersedia, sensor normal akan dijalankan"+Text.end)
        targett= tuple(target)
    teks=input("\nMasukan teks yang ingin"+Text.bold+" disensor mirip"+Text.end+": ").lower()
    tandabacat= tuple(tandabaca)
    teksakhir = teks.split()
    jumkata=len(teksakhir)
    jumsensor=0
    katadisensor=[]
    hasil = []
    
    for a in teksakhir:
        awal=a
        for t in tandabaca:
            a=a.replace(t,'')
            for tgt in target:
                rasio=SequenceMatcher(None,a,tgt).ratio()
                if rasio>0.8:
                    break
        if rasio>0.8 or a.startswith(targett) or a.endswith(targett):    
            if awal.endswith(tandabacat):
                hasil.append("*"*(len(awal)-1)+awal[-1])
                jumsensor+=1
            else:    
                hasil.append("*"*len(awal))
                jumsensor+=1
            #Kata Disensor
                if a not in katadisensor:       
                    katadisensor.append(a)
        else:
            hasil.append(a)
    for a in range(55):
        print(Text.purple+'~',end=""+Text.end)
    detail = Text.yellow+"\no) Jumlah Kata: {} \to) Jumlah Disensor: {} \n\
o) Kata Disensor: {}\n".format(jumkata,jumsensor,", ".join(katadisensor)+Text.end)
    # pyperclip.copy(" ".join(hasil)) gunakan jika pyperclip sudah diinstall
    print(detail)
    print("Hasil: "+Text.blue+" ".join(hasil)+"\n"+Text.end)
    sensorulang('m')

def sensorulang(a):
    inputsensor=input("Ingin sensor lagi? ("+Text.green+"ya"+Text.end+"/"+Text.red+"tidak"+Text.end+") ").lower()
    if inputsensor=="ya":
        if a=='n':
            sensor()
        elif a=='k':
            sensork()
        elif a=='m':
            sensorm()
    elif inputsensor=="tidak":
        halamanutama()   
    else:
        print(Text.red+"Input anda tidak sesuai petunjuk, anda akan diarahkan kembali ke halaman utama"+Text.end)
        halamanutama()

def halamangame():
    arah =input("Pilih Game yang ingin dimainkan!\nKuis\tNgetik "+Text.red+"(h untuk keluar)"+Text.end+"\n").lower()
    if arah=="kuis":
        mulaikuis(pasangan)
    elif arah=="ngetik":
        mulaingetik()
    elif arah=="h":
        halamanutama()
    else:
        print(Text.red+"Input tidak tersedia, ketik h untuk kembali ke halaman utama atau input dengan benar"+Text.end)
        halamangame()

def halamanutama():
    inputaksi=input("\nPilih aksi yang ingin dilakukan: ").lower()
    if inputaksi in inputlimit:
        if inputaksi == '1' or inputaksi == 's':
            sensor()
        elif inputaksi == '2' or inputaksi == 'sk':
            print("Hasil: "+sensork()+"\n")
        elif inputaksi == '3' or inputaksi == 'h':
            print(homescreen)
            halamanutama()
        elif inputaksi == '4' or inputaksi == 'b':
            print(halbantuan)
            halamanbantuan()
        elif inputaksi == '5' or inputaksi == 'g':
            halamangame()
        elif inputaksi == '6' or inputaksi == 'sm':
            sensorm()
        halamanutama()
    else: 
        print(Text.red+"Input tidak atau belum tersedia"+Text.end)
        halamanutama()

def halamanbantuan():
    print(Text.bold+"Pengertian/Lainnya"+Text.end)
    print(tambahan)
     
# mulai 
print (homescreen)
halamanutama()
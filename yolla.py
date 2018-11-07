import smtplib
import imaplib
import email
import os
import subprocess
import datetime
from datetime import datetime
import time
from email import *
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart

#gmail kullanici adi ve sifresi
#mailleri gonderecek olan hesabin bilgileri buraya yazilacak.
user = 'MAİL ADRESİNİZ@gmail.com'
sifre = 'MAİL ŞİFRENİZ'
gonderilecek_mail = 'FOTOĞRAFIN GÖNDERİLECEĞİ MAİL ADRESİ@gmail.com'

def komut():
        #gmail inboxuna baglanir.
        mail = imaplib.IMAP4_SSL("imap.gmail.com")

        mail.login(user, sifre)
        mail.list()

        mail.select("Inbox")

        result, data  = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        #splitler falan havada ucusur. burda mailden verdigim komutu ayirtmak istedim. bunun icin da
        #verecegim komutun basina /./: sonuna da /./ koymayi tercih ettim.
        #siz istediginiz sekilde degistirebilirsiniz.
        #yalniz : kalsin, ilerde lazim olur.
        
        al = list(raw_email.split("/./"))
        #split ettigi parcalari array icine aldi
        iler=[]

    


        for i in al:
            # : isareti burda lazim. komutu tanimlamak icin basinda : olana bakar. bunu buradan degistirebilirsiniz gene.
            if i.find(":") == 0:
                i = i.replace(":","")
                iler.append(i)
                if len(iler)>0:
                    mulo = iler[0]
                if len(iler)<1:
                    print("Komut bekleniyor");
            #burda kolaya kacip daginik biraktim. 
            #gonderilen komutun daha once gonderilmedigini tespit etmek icin
            #baska bir sey split etmek yerine komple maili aldim.
            #elbet birkac degisken farklilik gosterecekti. oldu da.
            
        return str(mulo) + " " + str(data[0])
            #burda malum degeri dondurduk.
    
        
        
def fotoYolla():
    #Foto klasorundeki 1.jpg'yi mail adresine gonderip
    #Foto'daki 1.jpg'yi FotoYedek klasorune tasir
    
    msg = MIMEMultipart()
    msg['Subject'] = "tut" #mesaj konusu
    msg['From'] = "me"
    msg['To'] = "" #buraya mailleri alacak olan adresinizi seyedeceksiniz.
    msg.preamble = "Guncel Foto" #bu nedir bilmem, baktigim kodda boyleydi aldim buraya da yazdim.
    
    img_data = open("Foto/1.jpg", 'rb').read()
    img = MIMEImage(img_data, "1.jpg")
    msg.attach(img)
    
    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.ehlo()
    s.login(user, sifre)
    s.sendmail(user, gonderilecek_mail, msg.as_string()) #burada da maili alacak olan adresi yazmaniz gerek.
    s.quit()
    vakit = str(datetime.now().strftime('%d-%m-%Y_%H:%M:%S')) #FotoYedek klasorune dosyalari ust uste yazmamak icin anin saatini aldik.
    
    #tasinma islemi.
    os.system("mv Foto/1.jpg FotoYedek/" + vakit +".jpg")
    
    
    


def rutin():
    #scriptin rutin olarak yapacagi seyler. 
    while 1:
        time.sleep(5)  #dileyen isteyen bu beklemeyi iptal edebilir sanirim. problem olursa tekrar koyun.
        komut()
        kontrol = open("kontrol.txt")
        kontrol = kontrol.read()
        
        if str(komut()) != kontrol:
            if str(komut()).find("yolla") == 0:  #komutun ne oldugunu anlamak icin. yolla komutunda bunu yap dercesine.
                os.system("fswebcam -r 1080x720 Foto/1.jpg")  #fotograf cekmek icin fswebcam kullandim. bana tatli geldi.
                fotoYolla() #fonksiyonumuzu cagirdik.
                knt = open("kontrol.txt", "w") #kontrol dosyasini acip kullumakka yazdiriyoruz ki ayni komuta birden fazla islem yapmasin.
                knt.write(str(komut()))
                knt.close()
                print("Fotograf gonderildi")
                
rutin()


#ve iste bu kadar.
#ileride farkli komutlar ekleyerek guclendirmeyi dusunuyorum. 
#simdilik sadece yolla komutu ve fotograf cekip yollama olayi var.
#baslangic icin fena degildir sanirim :)

#Niyazi Coban
#26 Subat 2017 Cumartesi

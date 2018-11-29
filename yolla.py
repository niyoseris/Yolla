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

user = '[from address]@gmail.com'
sifre = '[from address password]'
gonderilecek_mail = '[to address]@gmail.com'

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
    
        al = list(raw_email.split("/./"))
        iler=[]

    


        for i in al:
           if i.find(":") == 0:
                i = i.replace(":","")
                iler.append(i)
                if len(iler)>0:
                    mulo = iler[0]
                if len(iler)<1:
                    print("Waiting for command...");
            
        return str(mulo) + " " + str(data[0])
    
        
        
def fotoYolla():
    
    msg = MIMEMultipart()
    msg['Subject'] = "tut"
    msg['From'] = "me"
    msg['To'] = ""
    msg.preamble = "Current Foto"
    
    img_data = open("Foto/1.jpg", 'rb').read()
    img = MIMEImage(img_data, "1.jpg")
    msg.attach(img)
    
    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.ehlo()
    s.login(user, sifre)
    s.sendmail(user, gonderilecek_mail, msg.as_string())
    s.quit()
    vakit = str(datetime.now().strftime('%d-%m-%Y_%H:%M:%S')) 
  
    os.system("mv Foto/1.jpg FotoYedek/" + vakit +".jpg")
    
    
    


def rutin():
    while 1:
        time.sleep(5) 
        komut()
        kontrol = open("kontrol.txt")
        kontrol = kontrol.read()
        
        if str(komut()) != kontrol:
            if str(komut()).find("yolla") == 0:
                os.system("fswebcam -r 1080x720 Foto/1.jpg")
                fotoYolla() #fonksiyonumuzu cagirdik.
                knt = open("kontrol.txt", "w") 
                knt.write(str(komut()))
                knt.close()
                print("Foto sent")
                
rutin()

#Niyazi Coban
#26 Feb 2017 Sat

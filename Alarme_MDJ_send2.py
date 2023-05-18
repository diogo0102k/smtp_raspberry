import cv2
from picamera import PiCamera


import time

from time import sleep
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  
import smtplib
import ssl


camera = PiCamera()
camera.resolution = (640, 480)

####################################################################
#enviaremail

#Connected to smtp.gmail.com.

#2server=smtplib.SMTP('smtp.gmail.com',25) #anterior 587
#server=smtplib.SMTP('smtp-mail.outlook.com',587)
#2server.starttls()

#server.login("Your Email ID", "Email ID Password")

#2server.login("@gmail.com","") 
####################################################################
#tirar foto  #######################################################


#novo


camera.start_preview()
time.sleep(2)
camera.capture("test_MDJ.jpg")
time.sleep(2)
camera.stop_preview()
img = cv2.imread('test_MDJ.jpg')
        # Output img with window name as 'image'
cv2.imshow('Image loaded with OpenCV', img)

#mandando gmail

def send_an_email():  
    toaddr = '@gmail.com'      # To id 
    me = '@gmail.com'          # your id
    subject = "Boa tarde"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = me  
    msg['To'] = toaddr  
    msg.preamble = "test "   
    
  
    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open("test_MDJ.jpg", "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename="Test_MDJ.jpg"')   # File name and format name
    msg.attach(part)  
  
    try:  
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()  
       s.starttls()  
       s.ehlo()  
       s.login(user = '@gmail.com', password = '')  # User id & password
       #s.send_message(msg)  
       s.sendmail(me, toaddr, msg.as_string())  
       s.quit()  
    #except:  
    #   print ("Error: unable to send email")    
    except SMTPException as error:  
          print ("Error")                # Exception
  
send_an_email()  

    
cv2.waitKey(0)
cv2.destroyAllWindows()

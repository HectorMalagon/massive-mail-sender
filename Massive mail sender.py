# -*- coding utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendMail():

    # mails.txt is where you get all the mails, separated one mail for line
    mails = open("mails.txt")
    sender = "yourMail@gmail.com"
    password = "yourPassword"
   
    
    msg = MIMEMultipart()
    msg['From'] = sender
        
    msg['Subject'] = 'Hello guys'
    # message in html
    message = """\
    <html>
      <head></head>
        <body>
           <img src="http://martiko.com/wp-content/uploads/2015/06/pato-partes-2.png">   
        </body>
    </html>
    """
    msg.attach(MIMEText(message, 'html'))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(sender, password)
    for mail in mails:
        mailserver.sendmail(sender,mail,msg.as_string())

    mailserver.quit()

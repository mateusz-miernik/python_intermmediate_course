# -*- coding: utf8 -*-
import smtplib

mailFrom = 'Automatic mail sending system'
mailTo = ['receiver_mail']
mailSubject = 'Spam'
mailBody = """Mail body !!!

lolerum polelu

"""

message = """From: {}
Subject: {}

{}
""".format(mailFrom, mailSubject, mailBody)

user = 'example_mail@python.com'
password = 'example_password'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('Mail has been sent!')
except:
    print('error while sending email')

# import gmail
import smtplib
import json
from email.mime.text import MIMEText
import os


def send_mail(mail_subject, mail_body, to_email):
	# credentials = json.load(open('CONFIG', 'r'))
	msg = MIMEText(mail_body)
	msg['Subject'] = mail_subject
    # print (msg)
	# sending mail
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(os.environ["EMAIL"],os.environ["PASSWORD"])
		server.sendmail(os.environ["EMAIL"], to_email, msg.as_string())
		server.quit()
		return True
	except :
		return False

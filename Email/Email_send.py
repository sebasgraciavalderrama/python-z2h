import smtplib, getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
#print(smtp_object.ehlo())
smtp_object.starttls()
my_email = getpass.getpass('Email please: ', None)
password = getpass.getpass('Password please: ', None)
print(smtp_object.login(my_email, password))
from_email = my_email
to_address = my_email
subject = input('Enter the subject: ')
message = input('Enter the message: ')
msg = 'Subject: '+ subject + '\n' + message
smtp_object.sendmail(from_email, to_address, msg)
smtp_object.quit()

import smtplib

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)   # if doesnt work try to use 465

smtp_obj.starttls()

email = input("Email: ")
password = input("Password: ")
smtp_obj.login(email, password)

from_adress = email
to_adress = email
subject = input("enter subject line: ")
message = input("enter body massage: ")
msg = "Subject: " + subject + "\n" + message

smtp_obj.sendmail(from_adress, to_adress, msg)
import smtplib
import time
import os

try:
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)   # if doesnt work try to use 465

    smtp_obj.starttls()

    email = input("Email: ")
    password = input("Password: ")        #this is not the actual email password but the google_app password
    smtp_obj.login(email, password)

    os.system("cls")

    from_adress = email
    to_adress = input("who do you want to send the email to?: ")
    os.system("cls")
    subject = input("enter subject line: ")
    os.system("cls")
    message = input("enter body massage: ")
    os.system("cls")
    msg = "Subject: " + subject + "\n" + message

    smtp_obj.sendmail(from_adress, to_adress, msg)
    smtp_obj.quit()

    print(f"Email sucessfully sent to: {to_adress} !")
    time.sleep(1.5)
    os.system("cls")
except:
    os.system("cls")
    print("Something went wrong! Check if your input was right, if it was please contact the developer!")
finally:
    print("The program is gonna close in 3s")
time.sleep(3)

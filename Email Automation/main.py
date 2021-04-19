import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *


def sendEmail():
    emailId = reciever_email.get()

    from_address = 'dpramanick9990@gmail.com'
    to_address = emailId
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Sample email"
    body = "Hello world"

    msg.attach(MIMEText(body, 'plain'))

    email = 'dpramanick9990@gmail.com'
    password = '9674003240'

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)
    text = msg.as_string()
    mail.sendmail(from_address, to_address, text)
    mail.quit()

    print(emailId, password)
    return None


root = Tk()
root.title("First Tkinter Window")
root.geometry('400x400')

reciever_email = Entry(root, width=40)
reciever_email.pack(padx = 10, pady = 10)


Button(root, text="Send", command=sendEmail).pack()


root.mainloop()

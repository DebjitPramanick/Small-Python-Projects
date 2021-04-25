import requests
import json
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Send Message...")
root.geometry('400x400')


def sendSMS(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {"authorization": "HRtqm2atqaFqwIkU1x35Fzxgqqxho1CKSU4BNOZFuuZbI5CDawKCrgWSoU8O", "sender_id": "TXTIND",
               "message": message, "route": "v3", "numbers": number}
    headers = {
        'cache-control': "no-cache"
    }
    res = requests.request("GET", url, headers=headers, params=querystring)
    dic = res.json()
    print(dic)

number = Entry(root, width=40)
number.pack(padx=10, pady=10)
msg = Entry(root, width=40)
msg.pack(padx=10, pady=10)

Button(root, text="Send", command=lambda: sendSMS(
    number.get(), msg.get())).pack()

root.mainloop()

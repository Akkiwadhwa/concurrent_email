import concurrent.futures
import os

import pandas as pd
import requests
from fake_useragent import UserAgent
from requests.structures import CaseInsensitiveDict


def mail(di):
    ua = UserAgent()
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/javascript, */*"
    headers["accept-encoding"] = "gzip, deflate, br"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["cache-control"] = "max-age=0"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["origin"] = "https://api.elasticemail.com"
    headers["referer"] = "https://api.elasticemail.com/"
    headers["upgrade-insecure-requests"] = "1"
    headers["user-agent"] = ua.random

    url = "https://api.smtprelay.co/contact/add?version=2"

    for key, value in di.items():
        data = f"email={value}&submit=Subscribe&publicaccountid={key}&returnUrl=https%253A%252F" \
               "%252Fgoogle.com&activationReturnUrl=&alreadyactiveurl=&activationTemplate=newstandard&source=WebForm" \
               "&verifyemail=false&captcha=false&sendActivation=true&notifyEmail= "
        prx = open('proxies.txt', 'r')
        prx1 = prx.readlines()
        http_prx = prx1[0].split('>')[-1].strip()
        https_prx = prx1[1].split('>')[-1].strip()
        proxies = {"http": http_prx, "https": https_prx}
        print("a")
        resp = requests.post(url, headers=headers, data=data)
        failed_mail.append(di)
        prx.close()

        if resp.status_code != 200:
            print("b")


li1 = []
failed_mail = []
o = input("Press a for sending emails,b for sending failed.csv emails: ").capitalize()
if o == "A":
    files = os.listdir('email')
    p_id = open("publicaccountids.txt", "r").readlines()
    count = 0
    count1 = 0
    f = []
    p_li = [i.strip() for i in p_id]
    for p1 in p_li:
        if count <= len(files):
            count += 1
            count1 = 0
            for e in files:
                if count1 < 1:
                    if e not in f:
                        f.append(e)
                        email = open(f"email/{e}", "r").readlines()
                        count1 += 1
                        for i in email:
                            a = {p1.strip(): i.strip()}
                            li1.append(a)
if o == "B":
    a = open("failed.csv").readlines()


print(a)
# print(f"total emails to sent -->  {len(li1)}")
# with concurrent.futures.ThreadPoolExecutor(16) as executor:
#     executor.map(mail, li1)
#
# df = pd.DataFrame(failed_mail)
# df.to_csv("failed.csv")

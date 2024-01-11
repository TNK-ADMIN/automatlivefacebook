import requests, json, re, base64, uuid, random, os
from urllib.parse import (parse_qsl, urlsplit)
from codecs import unicode_escape_decode
from bs4 import BeautifulSoup as bs

class FacebookMain:

    def __init__(self, proxy: str = None) -> None:
        self.__client           = requests.Session()
        if proxy != None and ':' in proxy:
            proxies = {
                'http': '',
                'https': ''
            }
            proxy = proxy.strip().split(':')
            if len(proxy) > 2: proxynew = f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
            else: proxynew = f"http://{proxy[0]}:{proxy[1]}"
            for x in proxies:
                proxies[x] = proxynew
            self.__client.proxies = proxies
        self.__client.headers       = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'referer': 'https://www.facebook.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }
        self.__client.headers ={
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.109", "Google Chrome";v="120.0.6099.109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'viewport-width': '2814',
        }
    def addCookie(self, cookie: str = ''):
        try:
            self.__client.headers['cookie'] = cookie
            self.cookie = cookie
            return self.infoAccount()
        except Exception as e: print(e)
        return False, "Cookie die"

    def check_url(self):
        send = self.__client.get('https://www.facebook.com/')
        print(send.status_code)
        open('a.html', 'w+', encoding='utf-8').write(send.text)
        url = send.url
        if '/login' in url: return False, "Cookie die"
        elif '/checkpoint' in url: 
            type_cp = None
            for pt in url.split('/'):
                try:
                    int(pt)
                    if pt[-3:] in ['282', '956']:
                        type_cp = pt[-3:]
                except: pass
            return False, "Tài khoản bị checkpoint" + ("|"+type_cp if type_cp != None else '')
        else: 
            return True, True
    
    def check_login_is_run(self):
        try:
            check_status = self.check_url()
            if check_status[0] == True: 
                return True, ''
            else: return check_status
        except: pass    
        return False, ''
    
    def infoAccount(self):
        try:
            send = self.__client.get('https://www.facebook.com/').text
            DTSG__INIT__ = re.findall('DTSGInitialData",\[\],{"token":"(.*?)"}', send)[0]
            if DTSG__INIT__:
                self.fb_dtsg = DTSG__INIT__
                self.jazoest = re.findall('&jazoest=(.*?)"', send)[0]
                self.idFacebook = str(re.findall('"USER_ID":"(.*?)"', send)[0])
                self.lsdFacebook = re.findall('\["LSD",\[\],{"token":"(.*?)"}', send)[0]
                self.nameFacebook = unicode_escape_decode(re.findall('"NAME":"(.*?)"', send)[0])[0]
                self.__client.headers['sec-fetch-site'] = 'same-origin'
                return True, {'idFacebook': self.idFacebook, 'nameFacebook': self.nameFacebook}
        except Exception as e:
            pass
        return False, "Cookie die"

    def view_live(self, live_id: str):
        try:
            data = {    
                'd': '{"pps":{"m":true,"pf":3368,"s":"playing","sa":2757389},"ps":{"m":true,"pf":13608,"s":"playing","sa":2757389},"si":"f15a9d1e26e924","so":"tahoe::topic_live","vi":"' + live_id + '","tk":"8Qv0Li7gMFJ5BBFyb1m6yBHLCpEUYQ1eOTCdZrxLR1Y1myQk+aSMWGOI+1BZoJCHIcDB2DEdv0JISR+KBV034w==","ls":true}',
                '__user': self.idFacebook,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'lsd': self.lsdFacebook,
            }
            response = self.__client.post('https://www.facebook.com/video/unified_cvc/', data).text
            if "LIVE" in response: return True, "View live thành công"
        except: pass
        return False, 'View live thất bại'
# import threading
# import time
# idlive = input("Nhập Id Live: ")
# def main(cookie, idlive):
#     fb = FacebookMain()
#     if fb.addCookie(cookie)[0] == True:
#         print(fb.view_live(idlive))
        

# while True:
#     with open("Cookie.txt", 'r', encoding='utf-8') as f:
#         cookie_lines = f.readlines()
#         for cook in cookie_lines:
#             cookie = cook.strip()
#             threading.Thread(target=main, args=(cookie, idlive),).start()
#     time.sleep(10)




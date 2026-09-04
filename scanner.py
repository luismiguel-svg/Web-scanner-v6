import requests, socket, threading
from datetime import datetime

R = "\033[91m"; G = "\033[92m"; Y = "\033[93m"; C = "\033[96m"; W = "\033[0m"

banner = r"""
 __ __ __ ____ ____ ____
/ \ / \ ___/ |__ / ___\ ___ ____ ____ ____ ____
\ \/\/ // __ \ __\ / /_/ \/ _// __ \ / \ / \/ _ \
 \ /\ ___/| | \___ ( <_> ) \_\| | \ | ( <_> )
  \__/\ / \___ >__| /_____ /\____/\___ >___| /___| /\____/
       \/ \/ \/ \/ \/ \/
          Web Scanner v7.0 - SENSITIVE FILES
          by luismiguel-svg - Iquique, Chile
"""
print(f"{C}{banner}{W}")

web_input = input("Web (ej: demo.testfire.net): ").strip()
if not web_input.startswith("http"):
    web_input = "http://" + web_input
host = web_input.replace("http://","").replace("https://","").split("/")[0]
target = f"http://{host}"

print(f"\n{Y}[*] Objetivo: {host}{W}")
print(f"{Y}[*] Solo para uso educativo en webs propias / testfire.net{W}\n")

try:
    r = requests.get(target, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
    print(f"{G}[+] ONLINE {r.status_code}{W} | Server: {r.headers.get('Server','?')}")
except Exception as e:
    print(f"{R}[!] Error: {e}{W}")
    exit()

# 1. Paneles
print(f"\n{C}[*] [1/3] Paneles...{W}")
paths = ["/admin","/admin/login.php","/login","/wp-admin","/phpmyadmin","/cpanel"]
for p in paths:
    try:
        rr = requests.get(target+p, timeout=4, headers={"User-Agent":"Mozilla/5.0"})
        if rr.status_code in [200,301,302,401,403]:
            print(f"{G}[FOUND] {p} -> {rr.status_code}{W}")
    except: pass

# 2. Subdominios
print(f"\n{C}[*] [2/3] Subdominios...{W}")
subs = ["www","mail","ftp","admin","test","dev","api","blog","demo","portal"]
def check_sub(s):
    try:
        full = f"{s}.{host}"
        ip = socket.gethostbyname(full)
        print(f"{G}[SUB] {full} -> {ip}{W}")
    except: pass
threads = []
for s in subs:
    t = threading.Thread(target=check_sub, args=(s,))
    t.start(); threads.append(t)
for t in threads: t.join()

# 3. NEW v7 - Archivos sensibles
print(f"\n{C}[*] [3/3] Archivos sensibles v7.0 NEW...{W}")
sensitive = ["/.env","/.git/config","/backup.zip","/backup.tar.gz","/.DS_Store","/config.php","/database.sql","/wp-config.php.bak","/robots.txt","/sitemap.xml"]

for fpath in sensitive:
    try:
        url = target + fpath
        rr = requests.get(url, timeout=5, headers={"User-Agent":"Mozilla/5.0"})
        if rr.status_code == 200 and len(rr.text) > 0:
            # Evita falsos positivos
            if "404" not in rr.text[:200].lower():
                print(f"{R}[CRITICAL] {fpath} -> EXPUESTO! {len(rr.text)} bytes{W}")
                if ".env" in fpath and "DB_PASSWORD" in rr.text:
                    print(f"{R} -> Contiene credenciales!{W}")
        elif rr.status_code in [403,401]:
            print(f"{Y}[PROTECTED] {fpath} -> {rr.status_code}{W}")
    except: pass

print(f"\n{Y}[+] Scan v7 terminado{W}")


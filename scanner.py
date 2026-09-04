import requests, socket, threading
from datetime import datetime

# Colores
R = "\033[91m"; G = "\033[92m"; Y = "\033[93m"; C = "\033[96m"; W = "\033[0m"

banner = r"""
 __ __ __ ____ ____ ____
/ \ / \ ___/ |__ / ___\ ___ ____ ____ ____ ____
\ \/\/ // __ \ __\ / /_/ \/ _// __ \ / \ / \/ _ \
 \ /\ ___/| | \___ ( <_> ) \_\| | \ | ( <_> )
  \__/\ / \___ >__| /_____ /\____/\___ >___| /___| /\____/
       \/ \/ \/ \/ \/ \/
          Web Scanner v6.2 - SUBDOMAIN EDITION
          by luismiguel-svg - Iquique, Chile
"""

print(f"{C}{banner}{W}")

web_input = input("Web (ej: demo.testfire.net): ").strip()
if not web_input.startswith("http"):
    web_input = "http://" + web_input

host = web_input.replace("http://","").replace("https://","").split("/")[0]
target = f"http://{host}"

print(f"\n{Y}[*] Objetivo: {host}{W}")
print(f"{Y}[*] Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}{W}\n")

# 1. Info basica
try:
    r = requests.get(target, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
    print(f"{G}[+] ONLINE {r.status_code}{W} | Server: {r.headers.get('Server','Desconocido')}")
    if "cloudflare" in str(r.headers).lower() or "cf-ray" in str(r.headers).lower():
        print(f"{R}[!] PROTEGIDO POR CLOUDFLARE/WAF{W}")
except Exception as e:
    print(f"{R}[!] Error conectando: {e}{W}")

# 2. Scanner de paneles
print(f"\n{C}[*] [1/2] Buscando paneles ocultos...{W}")
paths = ["/admin","/admin/login.php","/login","/wp-admin","/wp-login.php","/phpmyadmin","/cpanel","/.env","/backup.zip","/admin.php"]
hallazgos = []

def check_path(p):
    try:
        url = target + p
        rr = requests.get(url, timeout=4, headers={"User-Agent":"Mozilla/5.0"})
        if rr.status_code in [200,301,302,401,403]:
            print(f"{G}[FOUND] {p} -> {rr.status_code}{W}")
            hallazgos.append(f"[{rr.status_code}] {url}")
    except: pass

for p in paths:
    check_path(p)

# 3. Scanner de subdominios v6.2 NUEVO
print(f"\n{C}[*] [2/2] Buscando subdominios... (v6.2 NEW){W}")
subs = ["www","mail","ftp","admin","test","dev","staging","api","blog","shop","app","vpn","ns1","beta","demo","portal","secure"]
found_subs = []

def check_sub(s):
    try:
        full = f"{s}.{host}"
        ip = socket.gethostbyname(full)
        print(f"{G}[SUBDOMINIO] {full} -> {ip}{W}")
        found_subs.append(f"{full} -> {ip}")
    except: pass

threads = []
for s in subs:
    t = threading.Thread(target=check_sub, args=(s,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Reporte
with open("reporte.txt","w") as f:
    f.write(f"=== SCANNER v6.2 REPORT ===\nTarget: {host}\nFecha: {datetime.now()}\n\n[PANEL] Hallazgos ({len(hallazgos)}):\n" + "\n".join(hallazgos) + f"\n\n[SUBDOMAIN] Hallazgos ({len(found_subs)}):\n" + "\n".join(found_subs))

print(f"\n{Y}[+] Terminado: {len(hallazgos)} paneles + {len(found_subs)} subdominios{W}")
print(f"{G}[+] Reporte guardado: reporte.txt{W}")


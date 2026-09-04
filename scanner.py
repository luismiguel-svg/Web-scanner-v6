import requests, socket
from datetime import datetime

banner = r"""
 _ _ _ ____
| | | | ___| |__ / ___| ___ __ _ _ __ _ __ ___ _ __
| |/\| |/ _ \ '_ \\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| \/ | __/ |_) |___) | (_| (_| | | | | | | | __/ |
 \_/\_/ \___|_.__/____/ \___\__,_|_| |_|_| |_|\___|_| v6.1
 by luismiguel-svg - Iquique
"""

print(banner)
web = input("Web (ej: demo.testfire.net): ").strip()
if not web.startswith("http"):
    web = "http://" + web

print(f"\n[*] Escaneando {web}")
try:
    r = requests.get(web, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
    print(f"[+] ONLINE {r.status_code} | Server: {r.headers.get('Server','Desconocido')}")

    if "cloudflare" in str(r.headers).lower():
        print("[!] DETECTADO: Cloudflare/WAF")

    host = web.replace("http://","").replace("https://","").split("/")[0]

    print("\n[*] Buscando paneles...")
    paths = ["/admin","/admin/login.php","/login","/wp-admin"]
    hallazgos = []
    for p in paths:
        url = f"http://{host}{p}"
        try:
            rr = requests.get(url, timeout=5)
            if rr.status_code in [200,301,302]:
                print(f"[REDIRIGE] {p} -> {rr.status_code} - EXISTE")
                hallazgos.append(f"[{rr.status_code}] {url} - EXISTE")
        except: pass

    with open("reporte.txt","w") as f:
        f.write(f"=== SCANNER v6.1 REPORT ===\nTarget: {web}\nFecha: {datetime.now()}\nServer: {r.headers.get('Server')}\n\nHallazgos:\n" + "\n".join(hallazgos))

    print(f"\n[+] Terminado: {len(hallazgos)} hallazgos")
    print("[+] Reporte: reporte.txt")

except Exception as e:
    print(f"[!] Error: {e}")

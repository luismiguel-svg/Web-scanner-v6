import requests, datetime

# Colores
G="\033[92m"; Y="\033[93m"; R="\033[91m"; C="\033[96m"; W="\033[0m"

print(f"""{C}
  ____ ____ _ _ _ _ _ _____ ____
 / ___|/ ___| / \ | \ | | \ | | ____| _ \
 \___ | | / _ \ | \| | \| | _| | |_) |
  ___) | |___ / ___ \| |\ | |\ | |___| _ <
 |____/\____/_/ \_\_| \_|_| \_|_____|_| \_\
        Web Scanner v6.0 by TU NOMBRE{W}""")

headers={"User-Agent":"Mozilla/5.0"}
url=input(f"{Y}Web (ej: demo.testfire.net): {W}").strip()
if "://" not in url: url="http://"+url
url=url.rstrip("/")

print(f"\n{C}[*] Escaneando {url} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}{W}")

try:
    r=requests.get(url,timeout=8,headers=headers)
    print(f"{G}[+] ONLINE {r.status_code} | Server: {r.headers.get('Server','?')}{W}")

    # Deteccion tecnologia
    html=r.text.lower()
    tech="Custom"
    if "wp-content" in html: tech="WordPress"
    elif "joomla" in html: tech="Joomla"
    elif "drupal" in html: tech="Drupal"
    print(f"{C}[*] Tecnologia detectada: {tech}{W}\n")

    rutas=["/robots.txt","/sitemap.xml","/admin","/admin/login.php","/administrator","/login","/wp-login.php","/wp-admin","/.env","/.git","/config.php","/backup.zip","/phpinfo.php","/api","/dashboard","/panel"]

    encontrados=[]
    for ruta in rutas:
        try:
            res=requests.get(url+ruta,timeout=4,headers=headers,allow_redirects=False)
            if res.status_code==200:
                print(f"{G} [OK] {ruta} -> 200 - EXISTE{W}")
                encontrados.append(f"[200] {url}{ruta}")
            elif res.status_code in [301,302]:
                print(f"{Y} [REDIRIGE] {ruta} -> {res.status_code} - EXISTE (redirige){W}")
                encontrados.append(f"[{res.status_code}] {url}{ruta} - REDIRIGE")
            elif res.status_code==403:
                print(f"{Y} [PROTEGIDO] {ruta} -> 403 - EXISTE (protegido){W}")
                encontrados.append(f"[403] {url}{ruta} - PROTEGIDO")
        except: pass

    # Reporte
    with open("reporte.txt","w") as f:
        f.write(f"=== SCANNER v6.0 REPORT ===\nTarget: {url}\nFecha: {datetime.datetime.now()}\nServer: {r.headers.get('Server','?')}\nTech: {tech}\n\nHallazgos ({len(encontrados)}):\n")
        f.write("\n".join(encontrados) if encontrados else "Sin hallazgos criticos")

    print(f"\n{G}[+] Terminado: {len(encontrados)} hallazgos{W}")
    print(f"{C}[+] Reporte guardado en: reporte.txt{W}")
    print(f"{C}[+] Ver con: cat reporte.txt{W}")

except Exception as e:
    print(f"{R}[!] Error: {e}{W}")

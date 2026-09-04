import requests, socket
from datetime import datetime

R="\033[91m";G="\033[92m";Y="\033[93m";C="\033[96m";W="\033[0m"
print(C+" Web Scanner v8.0 - by luismiguel-svg - Iquique "+W)

t=input("Web (testfire.net): ").strip()
if not t.startswith("http"): t="http://"+t
host=t.replace("http://","").replace("https://","").split("/")[0]
target="http://"+host

print(Y+"[*] Objetivo: "+target+W)
try:
 r=requests.get(target,timeout=10,headers={"User-Agent":"Mozilla/5.0"})
 print(G+"[+] ONLINE "+str(r.status_code)+W)
except Exception as e:
 print(R+str(e)+W); exit()

for p in ["/admin","/login","/wp-admin"]:
 try:
  rr=requests.get(target+p,timeout=4)
  if rr.status_code in [200,301,302,401,403]:
   print(G+"[FOUND] "+p+" -> "+str(rr.status_code)+W)
 except: pass

for f in ["/.env","/.git/config","/backup.zip","/robots.txt"]:
 try:
  rr=requests.get(target+f,timeout=4)
  if rr.status_code==200:
   print(R+"[CRITICAL] "+f+" EXPUESTO!"+W)
 except: pass

for s in ["www","ftp","demo"]:
 try:
  ip=socket.gethostbyname(s+"."+host)
  print(G+"[SUB] "+s+"."+host+" -> "+ip+W)
 except: pass

open("reporte.html","w").write("<h1>Scan "+host+" v8.0 by luismiguel-svg "+str(datetime.now())+"</h1>")
print(G+"[+] reporte.html creado"+W)

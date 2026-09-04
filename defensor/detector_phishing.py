print("=== v9.1 DEFENSOR - Detector de Phishing ===")
url = input("Pega el link sospechoso: ").strip().lower()
sospechosas = ["bit.ly", "tinyurl", "free", "login-facebook", "instagram-verify", "faceb00k"]
peligro = 0
for s in sospechosas:
    if s in url:
        print(f"[!] Palabra sospechosa: {s}")
        peligro += 1
if "https" not in url:
    print("[!] No usa HTTPS - muy sospechoso")
    peligro += 2
if peligro >= 2:
    print("\nALTA PROBABILIDAD DE PHISHING - NO ENTRES")
else:
    print("\nParece limpio, pero verifica el dominio oficial")
print("\nv9.1 DEFENSOR Iquique - 100% Etico")


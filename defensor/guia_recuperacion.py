print("=== v9.0 DEFENSOR - Guia de Recuperacion ===")
print("1. Facebook")
print("2. Instagram")
print("3. Gmail")
print("4. WhatsApp")

opciones = input("Elige (ej: 1,3): ").replace(" ","").split(",")

for opcion in opciones:
    if opcion == "1":
        print("\n[FACEBOOK] Ve a facebook.com/hacked -> Mi cuenta fue hackeada -> Sigue pasos")
    if opcion == "2":
        print("\n[INSTAGRAM] Ve a instagram.com/hacked -> Mi cuenta fue hackeada")
    if opcion == "3":
        print("\n[GMAIL] Ve a myaccount.google.com -> Seguridad -> Actividad reciente -> Cierra sesiones")
    if opcion == "4":
        print("\n[WHATSAPP] Reinstala WhatsApp, verifica con SMS, Activa Verificacion en 2 pasos")

print("\nGuia generada por v9.1 DEFENSOR!"nano defensor/guia_recuperacion.pyrm defensor/detector_phishing.py
rm defensor/guia_recuperacion.py


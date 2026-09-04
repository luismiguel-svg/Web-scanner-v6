print("=== v9.1 DEFENSOR - Guia de Recuperacion ===")
print("1. Facebook")
print("2. Instagram")
print("3. Gmail")
print("4. WhatsApp")
opciones = input("Elige (ej: 1,3): ").replace(" ","").split(",")
for opcion in opciones:
    if opcion == "1":
        print("\n[FACEBOOK] Ve a facebook.com/hacked")
    if opcion == "2":
        print("\n[INSTAGRAM] Ve a instagram.com/hacked")
    if opcion == "3":
        print("\n[GMAIL] Ve a myaccount.google.com -> Seguridad")
    if opcion == "4":
        print("\n[WHATSAPP] Reinstala y activa verificacion en 2 pasos")
print("\nGuia v9.1 lista")

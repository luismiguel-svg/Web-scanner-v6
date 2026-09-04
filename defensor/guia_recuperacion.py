opcion = input("Elige: ")
opciones = input("Elige (puedes poner varias ej: 1,3): ").replace(" ","").split(",")
for opcion in opciones:
    if opcion == "1":
        print("\n[FACEBOOK] Ve a facebook.com/hacked -> Mi cuenta fue hackeada")
    if opcion == "2":
        print("\n[INSTAGRAM] Ve a instagram.com/hacked -> Mi cuenta fue hackeada")
    if opcion == "3":
        print("\n[GMAIL] Ve a myaccount.google.com -> Seguridad -> Actividad reciente")
    if opcion == "4":
        print("\n[WHATSAPP] Reinstala y verifica con SMS, activa 2 pasos")
# v9.0 DEFENSOR - Guía de Recuperación para Víctimas
print("=== v9.0 DEFENSOR - Guía de Recuperación ===\n")
print("¿Qué le hackearon?")
print("1 = Facebook")
print("2 = Instagram")
print("3 = Gmail / Google")
print("4 = WhatsApp")
op = input("Elige 1-4: ")

print("\n--- PLAN DE RESCATE ---")
print("PASO 1 (URGENTE): Cambia clave del CORREO primero.")
print("Si le robaron el correo, controlan todo.")

if op == "1":
    print("\n-> Facebook:")
    print("  - Ve a: facebook.com/hacked")
    print("  - Click en 'Mi cuenta fue hackeada'")
    print("  - Revisa: myaccount.google.com/activity no, facebook.com/settings -> sesiones")
    print("  - Cierra todas las sesiones y activa 2FA")

elif op == "2":
    print("\n-> Instagram:")
    print("  - Ve a: instagram.com/hacked")
    print("  - Pide código a tu correo / SMS")
    print("  - Si cambió el correo, usa '¿No puedes acceder?'")
    print("  - Activa: Configuración > Seguridad > Autenticación en dos pasos")

elif op == "3":
    print("\n-> Gmail:")
    print("  - Ve a: google.com/recovery")
    print("  - Después: myaccount.google.com/activity -> cierra dispositivos raros")
    print("  - Revisa: myaccount.google.com/permissions -> quita apps raras")

elif op == "4":
    print("\n-> WhatsApp:")
    print("  - Reinstala WhatsApp y verifica con SMS")
    print("  - Activa: Ajustes > Cuenta > Verificación en dos pasos > pon PIN")
    print("  - Avisa a contactos: 'Me hackearon, no manden plata'")

print("\nPASO FINAL PARA TODOS:")
print("- Corre antivirus en el celular/PC")
print("- Cambia claves que eran iguales a la robada")
print("- Revisa haveibeenpwned.com")
print("\n¡Guía generada por v9.0 DEFENSOR!")
nano defensor/guia_recuperacion.py
opcion = input("Elige: ")
opciones = input("Elige (puedes poner varias ej: 1,3): ").replace(" ","").split(",")
for opcion in opciones:
    if opcion == "1":
        print("\n[FACEBOOK] Ve a facebook.com/hacked -> Mi cuenta fue hackeada")
    if opcion == "2":
        print("\n[INSTAGRAM] Ve a instagram.com/hacked -> Mi cuenta fue hackeada")
    if opcion == "3":
        print("\n[GMAIL] Ve a myaccount.google.com -> Seguridad -> Actividad reciente")
    if opcion == "4":
        print("\n[WHATSAPP] Reinstala y verifica con SMS, activa 2 pasos")


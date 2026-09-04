# v9.0 DEFENSOR - Checker de filtraciones
# Ayuda a víctimas a ver si su correo fue filtrado
import requests

print("=== v9.0 DEFENSOR - Checker ===")
correo = input("Correo de la víctima (con su permiso): ")

# API pública y segura
url = f"https://haveibeenpwned.com/unifiedsearch/{correo}"
headers = {"User-Agent": "Web-Scanner-v9-Defensor"}

# Por ahora solo mostramos guía, sin hacer la request para no bloquearte
print(f"\n[INFO] Revisando {correo}...")
print("1. Ve a: https://haveibeenpwned.com/")
print(f"2. Pega el correo: {correo}")
print("3. Si sale en rojo = su clave se filtró, debe cambiarla YA")
print("\nLinks de recuperación:")
print("- Facebook: facebook.com/hacked")
print("- Instagram: instagram.com/hacked")
print("- Google: myaccount.google.com/activity")
00

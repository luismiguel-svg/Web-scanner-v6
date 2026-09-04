# SCANNER v6.0 - Web Recon Tool

Herramienta de reconocimiento web hecha en Python para Termux / Linux.

## Features
- Detección de servidor y tecnología (WordPress, Joomla, etc)
- Escaneo de 16 rutas sensibles (/admin, /.env, /backup.zip, etc)
- Detecta 200, 301, 302, 403
- Genera reporte automático en reporte.txt
- Banner y colores

## Uso
python scanner.py

## Ejemplo
Target: http://demo.testfire.net
[302] /admin - REDIRIGE
[302] /admin/login.php - REDIRIGE

## Autor
Hecho en Termux - Iquique, Chile
Para fines educativos / Bug Bounty

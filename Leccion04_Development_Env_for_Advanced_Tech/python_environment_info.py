# Requisitos:
# No requiere instalar librerías externas.
#
# Este script permite verificar si estás dentro de un Python Virtual Environment.
#
# Ejecutar con:
# python 02_virtual_environment_check.py

import sys

print("=== Virtual Environment Check ===")

if sys.prefix != sys.base_prefix:
    print("Estás ejecutando Python dentro de un virtual environment.")
    print(f"Virtual env path : {sys.prefix}")
else:
    print("NO estás dentro de un virtual environment.")
    print("Crea uno con:")
    print("python -m venv venv")
    print("Actívalo en Linux/macOS con:")
    print("source venv/bin/activate")
    print("Actívalo en Windows con:")
    print(r"venv\Scripts\activate.bat")
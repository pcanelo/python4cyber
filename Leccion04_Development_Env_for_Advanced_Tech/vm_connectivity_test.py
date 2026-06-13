# Requisitos:
# No requiere instalar librerías externas.
#
# Uso:
# python 04_vm_connectivity_test.py 192.168.56.101
#
# El argumento debe ser la IP de una VM local, por ejemplo una Ubuntu VM o Kali VM.

import subprocess
import sys
import platform

if len(sys.argv) != 2:
    print("Uso: python 04_vm_connectivity_test.py <IP_VM>")
    sys.exit(1)

target = sys.argv[1]

print(f"=== Connectivity Test to VM: {target} ===")

system = platform.system().lower()

if system == "windows":
    command = ["ping", "-n", "4", target]
else:
    command = ["ping", "-c", "4", target]

try:
    result = subprocess.run(command, capture_output=True, text=True)

    print(result.stdout)

    if result.returncode == 0:
        print("Resultado: VM alcanzable.")
    else:
        print("Resultado: VM no alcanzable.")

except Exception as error:
    print(f"Error ejecutando ping: {error}")
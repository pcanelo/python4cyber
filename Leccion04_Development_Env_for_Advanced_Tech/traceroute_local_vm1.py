# Requisitos:
# Linux/macOS:
#   traceroute debe estar instalado.
#   En Ubuntu/Debian:
#   sudo apt install traceroute
#
# Windows:
#   usa tracert, viene incluido por defecto.
#
# Uso:
# python 05_traceroute_local_vm.py 192.168.56.101

import subprocess
import sys
import platform

if len(sys.argv) != 2:
    print("Uso: python 05_traceroute_local_vm.py <IP_VM>")
    sys.exit(1)

target = sys.argv[1]

print(f"=== Traceroute to VM: {target} ===")

system = platform.system().lower()

if system == "windows":
    command = ["tracert", target]
else:
    command = ["traceroute", target]

try:
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

    if result.stderr:
        print("Errores:")
        print(result.stderr)

except Exception as error:
    print(f"Error ejecutando traceroute/tracert: {error}")
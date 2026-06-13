# Requisitos:
# Instalar psutil:
# pip install psutil
#
# Ejecutar con:
# python 03_network_interfaces.py

import psutil

print("=== Network Interfaces ===")

interfaces = psutil.net_if_addrs()

for interface_name, addresses in interfaces.items():
    print(f"\nInterface: {interface_name}")

    for addr in addresses:
        print(f"  Family  : {addr.family}")
        print(f"  Address : {addr.address}")
        print(f"  Netmask : {addr.netmask}")
        print(f"  Broadcast: {addr.broadcast}")
# nmap_discovery.py

"""
Descripción:
    Realiza un análisis de la red del sistema de destino.

 
"""

import nmap3
import json


class NmapDiscovery:
    def discover(self, host) -> None:
        """
        Discover using ARP.

        Args:
            host (string): host to scan
        """
        nmap = nmap3.NmapHostDiscovery()

        nmap.nma

        scan_results = nmap.nmap_arp_discovery(host)
        print(json.dumps(scan_results, indent=4))


if __name__ == "__main__":
    nmap_discovery = NmapDiscovery()
    nmap_discovery.discover('<<host>')

# censys_print_host_details.py

"""
Descripción:
    Utiliza Censys para obtener toda la información pública sobre un sistema de destino.
"""
 

import json
from censys.search import CensysHosts

censys_host = CensysHosts()


class CensysHostDetails:
    def print_host_details(self, ip_address) -> json:
        try:
            ipinfo = censys_host.view(ip_address)
        except:
            ipinfo = {}

        print(json.dumps(ipinfo, indent=4))


if __name__ == "__main__":
    censys_info = CensysHostDetails()
    censys_info.print_host_details('<<IP Address>>')

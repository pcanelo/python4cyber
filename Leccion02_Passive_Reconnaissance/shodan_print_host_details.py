# shodan_print_host_details.py

"""
Descripción:
    Utiliza Shodan para obtener toda la información pública sobre un sistema de destino.

 
 
"""

from shodan import Shodan
import json

api = Shodan('<<API Key>>')


class ShodanHostDetails:
    def print_host_details(self, ip_address):
        """""
        Print details about the IP address

        Args:
            ip_address (String): IP address to scan
        """
        ipinfo = api.host(ip_address)
        print(json.dumps(ipinfo, indent=4))


if __name__ == "__main__":
    shodan_info = ShodanHostDetails()
    shodan_info.print_host_details('<<IP Address>>')

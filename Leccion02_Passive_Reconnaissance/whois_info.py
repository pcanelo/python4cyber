# whois_info.py

"""
Descripción:
    Obtener los datos «whois» de un host.
 
"""

import whois as ws


class WhoisInfo:
    def print_whois_info(self, host):
        """
            host: Host that you want the whois details for.
        """

        whois_info = ws.whois(host)
        print(whois_info)


if __name__ == "__main__":
    whois_info = WhoisInfo()
    whois_info.print_whois_info("google.com")

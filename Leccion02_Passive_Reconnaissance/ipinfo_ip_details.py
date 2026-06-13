# ipinfo_ip_details.py

"""
Descripción:
    Utiliza IPInfo para obtener toda la información pública sobre una dirección IP.
"""

import json
import ipinfo

ipinfo_accesstoken = '<<Access Token>>'
handler = ipinfo.getHandler(ipinfo_accesstoken)


class IpinfoDetails:

    def get_host_details(self, ip_address):
        try:
            global handler
            ipinfo_details = handler.getDetails(ip_address)
        except:
            ipinfo_details = {}

        print (json.dumps(ipinfo_details.all, indent=4))


if __name__ == "__main__":
    ipinfo_details = IpinfoDetails()
    ipinfo_details.get_host_details('<<IP Address>>')

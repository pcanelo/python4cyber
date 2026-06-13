# censys_parse_host_details.py

"""
Descripción:
    Utiliza Censys para obtener toda la información pública sobre un sistema de destino y, a continuación, analiza algunas claves o atributos.
"""

import json
from censys.search import CensysHosts

censys_host = CensysHosts()


class CensysHostDetailsParser:
    def print_host_details(self, ip_address) -> json:
        try:
            ipinfo = censys_host.view(ip_address)
        except:
            ipinfo = {}

        # First convert the response to JSON using json.dumps and then load it in a JSON object
        json_data = json.loads(json.dumps(ipinfo))

        # Now print the attributes we need. The get() function can be used to get specific attributes
        print('[services][0][service_name]: ',
              json_data['services'][0]['service_name'])
        print('[services][0][port]: ', json_data['services'][0]['port'])
        print('[services][0][banner]: ', json_data['services'][0]['banner'])


if __name__ == "__main__":
    censys_host_details_parser = CensysHostDetailsParser()
    censys_host_details_parser.print_host_details('<<IP Address>>')

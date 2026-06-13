# apivoid_ssl_info.py

"""
Descripción:
    Obtener información SSL de un host mediante la API «sslinfo» de APIVoid.
"""
 

import requests
import json

apivoid_key = "<<API Key>>"


class ApivoidSslInfo:
    def apivoid_query(self, endpoint, host) -> json:
        """
        A generic method to query APIVoid using the endpoint supplied

        Args:
            endpoint (string): API endpoint
            host (string): host

        Returns:
            json: Query output
        """
        try:
            r = requests.get(url='https://endpoint.apivoid.com/'+endpoint +
                             '/v1/pay-as-you-go/?key='+apivoid_key+'&host='+host)
            return json.loads(r.content.decode())
        except:
            return {}


if __name__ == "__main__":
    apivoid_ssl_info = ApivoidSslInfo()
    json_data = apivoid_ssl_info.apivoid_query(
        'sslinfo', '<<Host>>')
    print(json.dumps(json_data, indent=4))

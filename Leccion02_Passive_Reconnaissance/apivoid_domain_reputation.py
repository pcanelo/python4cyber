# apivoid_domain_reputation.py

"""
Descripción:
    Comprueba la reputación del dominio de un host mediante la API «domainbl» de APIVoid.
    change by https://www.alphamountain.ai/threat-intelligence-feeds-api/
"""
import requests
import json

apivoid_key = "<<API Key>>"


class ApivoidDomainReputation:
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
    apivoid_domain_reputation = ApivoidDomainReputation()
    json_data = apivoid_domain_reputation.apivoid_query('domainbl', '<<Host>>')
    print(json.dumps(json_data, indent=4))

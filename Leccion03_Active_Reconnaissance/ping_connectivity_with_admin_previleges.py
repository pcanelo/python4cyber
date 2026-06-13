# ping_connectivity_with_admin_previleges.py

"""
Descripción:
    Comprueba la conectividad de un host mediante el comando Ping de ICMP.

    Este programa debe ejecutarse como «administrador» o con privilegios «sudo»; de lo contrario, dará un error similar a «PermissionError: [Errno 1] Operación no permitida». Un usuario sin privilegios
    elevados no puede enviar mensajes ICMP, de ahí el error.


 
"""

from pythonping import ping


class PingConnectivity:
    def check_ping_connectivity(self, host) -> None:
        ping(host, verbose=True)


if __name__ == "__main__":
    ping_check_connectivity = PingConnectivity()
    ping_check_connectivity.check_ping_connectivity('google.com')

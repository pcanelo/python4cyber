# netstat.py

"""
Descripción:
    Implementa la funcionalidad de «netstat» en Python para consultar información sobre puertos y servicios.
 
"""

# We are using net_connection from psutils to check for all the 'netstat' functionality. psutil has a hugh collection
# of very useful utiliy functions which are worth exploring.
from psutil import net_connections


class NetStats:
    def print_net_connections(self) -> None:
        print('TCP connections:')
        print(net_connections(kind='tcp'))
        print('\n')
        print('UDP connections:')
        print(net_connections(kind='udp'))


if __name__ == "__main__":
    netstats = NetStats()
    netstats.print_net_connections()

from  addressNetwork import AddressNetwork
import math

class SuperNetwork:
    def __init__(self, subnet, list_hosts_for_all_subnetworks):
        self.subnet = subnet
        self.hosts_subnet =SuperNetwork._order_hosts_subnet(list_hosts_for_all_subnetworks) 
        # self._prefix = 
    

    @staticmethod
    def _order_hosts_subnet(hosts_subnet):
            
            hosts_subnet.sort()
            hosts_subnet.reverse()
            return hosts_subnet
    
    @staticmethod
    def __print_format(subnet):
        string=str()
        for octet in subnet:
            string+=str(octet)+'.'
        else:
            string+=f'\b '
        return string
    @property
    def subnet(self):

        return self.__subnet
    
    
    @subnet.setter
    def subnet(self, value):
        subnet_and_prefix=SuperNetwork._check_subnet(value)
        self.__prefix=subnet_and_prefix[1]
        self.__subnet=subnet_and_prefix[0]
        
    @staticmethod
    def _check_subnet( value):
        subnet_and_prefix= value.split('\\')
        octets=subnet_and_prefix[0].split('.')
        prefix=subnet_and_prefix[1]

        for i,octet in enumerate(octets):
            octets[i]=int(octets[i])
            if int(octet) >255:
                raise ValueError("octet must be between 0 and 255")
        if not( 1<=int(prefix)<=32) :
            raise ValueError("prefix must be between 0 and 32")
        if len(octets)>4:
            raise ValueError("the number of octets must be 4 octets")
        return octets, prefix

        def __str__(self):
            return f"{self.__print_format(self.subnet)} /{self.prefix}"
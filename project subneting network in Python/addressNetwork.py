import math
class AddressNetwork:
    def __init__(self, subnet,hosts):
        """class for every subAssdress of the supersubnet"""
        self._subnet = subnet
        self.magic = 2**math.ceil(math.log2(hosts))
        self.prefix=32-math.ceil(math.log2(hosts))
        self.mask=self.claclate_mask(self.prefix)
        self.addressesWasted =self.magic -hosts
        self._broadcast=AddressNetwork.calclate_broadcast(self._subnet,self.magic)
        self.addressesForHosts=self.calclateRangeHost()


    @property
    def subnet(self):
        string=str()
        for octet in self._subnet:
            string+=str(octet)+'.'
        else:
            string+='\b '
        return string
   

    @property
    def broadcast(self):
        return self._broadcast
    @staticmethod
    def __print_formating(subnet):
        string=str()
        for octet in subnet:
            string+=str(octet)+'.'
        else:
            string+='\b '
        return string
    
    
    def calclateRangeHost(self):
        string=str()
        firstHost=self._subnet.copy()
        lastHost=self._broadcast.copy()
        firstHost[-1]+=1
        lastHost[-1]-=1
        mixOctet=firstHost+['.']+lastHost

        for octet in mixOctet:
            
            if octet=='.':
                string+='\b  to '
                continue
            string+=str(octet)+'.'
        else:
             string+='\b '

        return string
    
        
    def claclate_mask(self,prefix):
        binary_mask =prefix*'1'
        binary_mask +=(32-prefix)*'0'
        mask = []
        for i in range(4):
            mask.append(int(binary_mask[8*i:(i+1)*8],2))
            mask.append('.')
        string=str()
        for i in mask:
            string+=str(i)
        else:
             string+='\b '
             
        return string
    
    @staticmethod
    def calclate_broadcast(subnet, magic):
        broadcast = subnet.copy()
        

        broadcast[-1] += magic - 1

        if broadcast[-1] > 255:
            result_after_divider = broadcast[-1] // 256
            broadcast[-1] %= 256

            broadcast[-2] += result_after_divider

            if broadcast[-2] > 255:
                result_after_divider = broadcast[-2] // 256
                broadcast[-2] %= 256
                broadcast[-3] += result_after_divider

        return broadcast

    def __str__(self):
        string=f"{self.subnet:<18} {self.addressesForHosts:<40} {AddressNetwork.__print_formating(self._broadcast):<18}  {self.mask:<18}  {self.prefix:<10} {self.magic:<10} {self.addressesWasted:<10}"
        return string

subnet2=AddressNetwork([10,'10',253,20],50)
subnet=subnet2.broadcast.copy()
print(subnet)
print(type(subnet[1]))
# print(AddressNetwork.calclate_broadcast([200,30,254,0],512))



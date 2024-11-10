import Guid
from superAddress import SuperNetwork
from  addressNetwork import AddressNetwork
def read_inputs():
    address= input("Enter the network address to subnting as ->192.168.0.0 \\16 >> ")
    print("Enter the host for every  subnetwork ,Enter 0 or nagtive number to stop>> ")
   
    one_host=1
    total_host=[]
    while not (int(one_host)<=0 ):
        
        one_host=int(input("Enter hosts >> "))
        if one_host<=0:
            print("Done the input")
            break
        else:
            total_host.append(one_host)
        print(f"Total hosts for subnetwork is {total_host}")

    return address,total_host

def print_address(network_address,sub_addresses):
    print(" "*36,60*"*")
    print(" "*36,f"the super network address: {network_address}")
    print(" "*36,60*"*")
    print()
    print()

    print("_"*120)

    string=f"{'|subnet':<18}| {'Range fo host':<20} {'           |     broadcast':<18}  {'|       mask':<18}  {'|  prefix':<10} {'| magic':<10} {'|Wasted':<10}"
    print(string)
    print("_"*120)
    for address in sub_addresses:
        print(f"{address}")

def perform_subneting():
    address,total_host=read_inputs()
    obj_subnet=SuperNetwork(address,total_host)
    list_subnetworks=[AddressNetwork(obj_subnet.subnet,total_host[0])]
    for i in range(len(total_host)-1):
        broadcast_copy=list_subnetworks[-1].broadcast.copy()
        broadcast_copy[-1]+=1
        # list_subnetworks[-1].broadcast[-1]+=1
        # print(list_subnetworks[-1].broadcast)
        # print(list_subnetworks[-1].subnet)

        # list_subnetworks.append(AddressNetwork(list_subnetworks[-1].broadcast,total_host[i+1]))   
        list_subnetworks.append(AddressNetwork(broadcast_copy,total_host[i+1]))   
        # print(list_subnetworks[-1].broadcast)
        # print(list_subnetworks[-1].subnet)


        # list_subnetworks[-2].broadcast[-1]-=1
        # print(list_subnetworks[-1].broadcast)
        # print(list_subnetworks[-1].subnet)



    print_address(address,list_subnetworks)
perform_subneting()
n=Guid.new
print(n)
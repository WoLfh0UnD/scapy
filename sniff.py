#!/usr/bin/python
import sys
from scapy.all import *

print “Usage: scapy-arping eg: ./sniff.py 192.168.1.0/24″

#create and send ARP request packets

rec,unans=srp(Ether(dst=”ff:ff:ff:ff:ff:ff”)/ARP(pdst=sys.argv[1]),timeout=2)

for send,recv in rec:
	print recv.sprintf(r”MAC: “+”%Ether.src%”+” <–> IP: “+” %ARP.psrc%”)

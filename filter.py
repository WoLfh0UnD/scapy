from scapy.all import *

build_filter = "src host %s and src port 21"
sniff(iface=iface, prn=callback, filter=build_filter)

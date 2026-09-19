from scapy.all import sniff, IP, TCP
import time

def process_packets(packet):

    print(packet.summary())

    syn_connections = {}

    if not packet.haslayer(IP) or not packet.haslayer(TCP):
        return

    ip = packet[IP]

    tcp = packet[TCP]

    src = ip.src

    dst = ip.dst

    sport = tcp.sport

    dport = tcp.dport

    if packet.tcp == "S":

        key = (src,dst,sport,dport)

        syn_connections[key] = {
            "time": time.time()
        }

        print(f"[SYN] {src}:{sport} => {dst}:{dport}")

    elif packet.tcp == "SA":

        key = (src,dst,sport,dport)

        if key in syn_connections:

            syn_time = syn_connections[key]["time"]

            response_time = time.time() - syn_time

            print(
                f"[SYN-ACK] {src}:{sport} -> {dst}:{dport} "

                f"| Response: {response_time * 1000:.2f} ms"
            )

            syn_connections[key]["syn_ack_time"] = time.time()

    elif packet.tcp == "A":

        key = (src,dst,sport,dport)

        if key in syn_connections:

            start = syn_connections[key]["time"]

            total_time = time.time() - syn_time

            print(
                f"[ACK] {src}:{sport} -> {dst}:{dport} "

                f"| Handshake: {total_time * 1000:.2f} ms"
            )

            del syn_connections[key]

    print("[*] NIDS monitoring...")
    
    sniff(prn=process_packets, store=False)


    









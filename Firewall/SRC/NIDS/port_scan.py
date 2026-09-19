from scapy.all import scapy,TCP,IP,sniff

BLOCK_FILE = "blocked_ports.txt"

def block_packet(packet):
    print(f"BLOCKED PACKET: {packet.summary()}")


def port_summary(packet):

    if IP in packet and TCP in packet:
      ip = packet[IP]
      tcp = packet[TCP]
      print(f"PORT: {tcp.sport}:{tcp.dport} :: IP: {ip.dst}:{ip.src}")

def port_selection(port):

   with open(BLOCK_FILE, "a") as f:
      f.write(f"{port}\n")








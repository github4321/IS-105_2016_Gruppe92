import struct
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # F� input fra bruker for objekt (h�ne, korn, rev eller b�t) og 
    # handling (flytt inn, flytt ut, flytt over)
    raw_input(">")
    
    # Pakk data og send til server
    struct.pack()
    udp_socket.sendto(("localhost", 5000))

    # Motta resultat fra server og print resultat
    udp_socket.recv(512)
    success = struct.unpack()
    if success == 1:
        print("Resultat")
    else:
        print("Kunne ikke hente resultat")
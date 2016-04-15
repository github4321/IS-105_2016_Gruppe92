import struct
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("localhost", 5000))

while True:
    # Motta og pakk ut data
    data, address = udp_socket.recvfrom(512)
    try:
        struct.unpack(data)

    except struct.error:
        # Gi beskjed dersom pakken er skadet eller ikke kom frem riktig.
        print("Kunne ikke pakke ut data fra klient.")

    else:
        # Gj�r handlinger i elvekryssningsspillet basert p� input fra klient
        success = 0
        if input == "h�ne":
            success = 1
        elif input == "rev":
            success = 1
        elif input == "korn":
            success = 1
        elif input == "b�t":
            success = 1        

        # Pakk og send resultatet til klient
        struct.pack(success)
        udp_socket.sendto(address)
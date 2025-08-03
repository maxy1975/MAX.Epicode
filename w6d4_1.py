import math

def leggi_float(prompt):
    while True:
        valore = input(prompt).replace(',', '.')  # accetta anche 1,5 come 1.5
        try:
            return float(valore)
        except ValueError:
            print("⚠️ Inserisci un numero valido!")

def calcola_quadrato():
    lato = leggi_float("Inserisci la lunghezza del lato del quadrato: ")
    perimetro = lato * 4
    print(f"✅ Il perimetro del quadrato è: {perimetro:.2f}")

def calcola_cerchio():
    raggio = leggi_float("Inserisci il raggio del cerchio: ")
    circonferenza = 2 * math.pi * raggio
    print(f"✅ La circonferenza del cerchio è: {circonferenza:.2f}")

def calcola_rettangolo():
    base = leggi_float("Inserisci la base del rettangolo: ")
    altezza = leggi_float("Inserisci l'altezza del rettangolo: ")
    perimetro = 2 * base + 2 * altezza
    print(f"✅ Il perimetro del rettangolo è: {perimetro:.2f}")

def menu():
    print("\n📐 Scegli la figura geometrica:")
    print("1 - Quadrato")
    print("2 - Cerchio")
    print("3 - Rettangolo")

menu()
scelta = input("Inserisci la tua scelta (1/2/3): ")

if scelta == '1':
    calcola_quadrato()
elif scelta == '2':
    calcola_cerchio()
elif scelta == '3':
    calcola_rettangolo()
else:
    print("❌ Scelta non valida.")

import math

def quadrato(lato):
    perimetro = lato * 4
    area = lato ** 2
    print(f"\n🔷 Quadrato ➝ lato = {lato}, perimetro = {perimetro}, area = {area}")
    return area

def cerchio(raggio):
    circonferenza = 2 * math.pi * raggio
    area = math.pi * raggio ** 2
    print(f"\n⚪ Cerchio ➝ raggio = {raggio}, circonferenza = {circonferenza:.2f}, area = {area:.2f}")
    return area

def rettangolo(area_come_lato):
    base = area_come_lato
    altezza = area_come_lato / 2  # Scelta arbitraria per avere area coerente
    perimetro = 2 * (base + altezza)
    area = base * altezza
    print(f"\n▭ Rettangolo ➝ base = {base}, altezza = {altezza}, perimetro = {perimetro}, area = {area}")
    return area

def scegli_figura(opzioni):
    print("\n📐 Scegli una figura geometrica:")
    for i, figura in enumerate(opzioni, start=1):
        print(f"{i}) {figura}")
    while True:
        try:
            scelta = int(input("Scelta: "))
            if 1 <= scelta <= len(opzioni):
                return opzioni[scelta - 1]
            else:
                print("❌ Scelta non valida.")
        except ValueError:
            print("❌ Inserisci un numero.")

def main():
    valore = float(input("Inserisci un valore iniziale (es. lato, raggio): "))
    figure_disponibili = ["Quadrato", "Rettangolo", "Cerchio"]

    for _ in range(3):  # almeno 3 figure
        figura = scegli_figura(figure_disponibili)
        figure_disponibili.remove(figura)

        if figura == "Quadrato":
            valore = quadrato(valore)
        elif figura == "Rettangolo":
            valore = rettangolo(valore)
        elif figura == "Cerchio":
            valore = cerchio(valore)

main()

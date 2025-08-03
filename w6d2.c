#include <stdio.h>
#include <string.h>

//PULIZIA BUFFER
void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}
//INTRODUZIONE
void mostraIntroduzione() {
    printf("Benvenuto al quiz di BreakingBad !\n");
    printf("Rispondi correttamente per ricevere la tua confezione di metanfetamina blu.\n\n");
}
//CREAZIONE MENU INIZIALE 
void mostraMenu() {
    printf("MENU:\n");
    printf("A) Iniziare una nuova partita\n");
    printf("B) Uscire dal gioco\n");
    printf("Inserisci la tua scelta (A/B): ");
}
//IMPOSTAZIONE PUNTEGGIO E INIZIO GIOCO
int giocaPartita(char nome[]) {
    int punteggio = 0;
    char risposta;
//IL PROGRAMMA AGGIUNGERA' IL TUO NOME ALLA FRASE
    printf("\nVediamo quanto conosci del mondo di BreakingBad, %s!\n", nome);

    // DA QUI INIZIANO LE DOMANDE CON AL SUO INTERNO LA RISPOSTA CORRETTA 
    printf("\n1) Quando Craston l'attore che interpreta Walter White ha avuto un crollo durante un episodio della serie , quale??\n");
    printf("A) dopo aver assunto del pejote sul set\nB) dopo aver girato la scena della morte di jane la fidanzata di jesse \nC) mai avuto un crollo\nRisposta: ");
    risposta = getchar();
    clearInputBuffer();
    if (risposta == 'B' || risposta == 'b') punteggio++;

    
    printf("\n2) quante morti ci sono state nell'arco di 5 stagioni di BreakingBad?\n");
    printf("A) 1234\nB) 4\nC) 270\nRisposta: ");
    risposta = getchar();
    clearInputBuffer();
    if (risposta == 'C' || risposta == 'c') punteggio++;

    
    printf("\n3) l'iconica scena della pizza sul tetto quante volte e' stata girata prima di raggiungere il perfetto atterraggio?\n");
    printf("A) ben 47 volte \nB) al primo ciak!\nC) son dovuti ricorrere alla computer grafica\nRisposta: ");
    risposta = getchar();
    clearInputBuffer();
    if (risposta == 'B' || risposta == 'b') punteggio++;

    printf("\n4) Durante la scena in cui Walter uccide Mike cosa ha fatto l'intera troupe?\n");
    printf("A) Ha indossato il lutto al braccio \nB) sciopero per ben 2 mesi!\nC) hanno pianto tutto il tempo\nRisposta: ");
    risposta = getchar();
    clearInputBuffer();
    if (risposta == 'A' || risposta == 'a') punteggio++;

    printf("\n5) quale personaggio Jesse non incontrera' mai per tutta la serie ?\n");
    printf("A) Jesse ha incontrato tutti i personaggi della serie  \nB) Mike !\nC) Walter jr figlio di Walter White: ");
    risposta = getchar();
    clearInputBuffer();
    if (risposta == 'C' || risposta == 'c') punteggio++;

    printf("\n6) Quale degli attori non ha mai preso lezioni di recitazione?\n");
    printf("A) Bryan Craston alias Walter White \nB) Aaron Paul alias Jesse !\nC) Raymond Cruz alias Tuco\nRisposta: ");
    risposta = getchar();
    clearInputBuffer();
    if (risposta == 'B' || risposta == 'b') punteggio++;

    printf("\n7) Durante lo sciopero dei sceneggiatori nel 2007 2008 venne salvato un personaggio che sarebbe dovuto morire nella 9puntata della prima stagione, chi??\n");
    printf("A) Jesse \nB) Skyler la moglie di Walter !\nC) Hank cognato di Walter\nRisposta: ");
    risposta = getchar();
    clearInputBuffer();
    if (risposta == 'A' || risposta == 'a') punteggio++;

//FINE PARTITA CALCOLO PUNTEGGIO CON AGGIUNTA NOME 
    printf("\nPARTITA TERMINATA NON SARAI MAI IL NUOVO HEISENBERG!!, %s! Il tuo punteggio è: %d/7\n\n", nome, punteggio);

    return punteggio;
}
// DA QUI VIENE IMPOSTATO LA PARTE CHE GESTIRA' LA MEMORIA DEL PUNTEGGIO ACCUMULATO
int main() {
    char scelta;
    char nome[50];
    int punteggioTotale = 0;

    mostraIntroduzione();

    do {
        mostraMenu();
        scelta = getchar();
        clearInputBuffer();

        if (scelta == 'A' || scelta == 'a') {
            printf("\nInserisci il tuo nome: ");
            fgets(nome, sizeof(nome), stdin);
            nome[strcspn(nome, "\n")] = '\0';  

            
            punteggioTotale += giocaPartita(nome);

            printf("Punteggio totale accumulato: %d\n\n", punteggioTotale);
        } else if (scelta == 'B' || scelta == 'b') {
            printf("\nUscita dal gioco. Punteggio finale accumulato: %d\n", punteggioTotale);
            printf("Arrivederci!\n");
        } else {
            printf("\nScelta non valida. Riprova.\n");
        }

    } while (scelta != 'B' && scelta != 'b');

    return 0;
}

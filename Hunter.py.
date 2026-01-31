import requests
import time

# CONFIGURAZIONE PALOXIS HUB
TOKEN = "8380699103:AAHRPHc0t4hdiuhr-uaJGDlmO4kDa0LxusE"
# Sostituisci 'IL_TUO_CHAT_ID' con il tuo ID se vuoi ricevere notifiche, 
# oppure lo useremo per inviare ai gruppi.
CHAT_ID = "638656123" # Questo è un esempio, lo useremo per i test

def invia_messaggio(testo):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": testo, "parse_mode": "Markdown"}
    try:
        r = requests.post(url, data=data)
        print(f"Risposta invio: {r.status_code}")
    except Exception as e:
        print(f"Errore: {e}")

def hunt():
    print("--- PALOXIS HUB HUNTER ATTIVO ---")
    messaggio = (
        "💰 *BONUS ATTIVI SU PALOXIS HUB*\n\n"
        "Hai già prelevato i tuoi bonus? BBVA e Revolut sono attivi ora.\n"
        "Non perdere tempo, i posti sono limitati.\n\n"
        "🔗 *ACCEDI QUI:* https://paoloforex.github.io/PALOXIS-HUB-BUSINESS/"
    )
    invia_messaggio(messaggio)
    print("Caccia completata. Messaggio inviato.")

if __name__ == "__main__":
    hunt()

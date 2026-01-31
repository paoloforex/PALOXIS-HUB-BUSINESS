import requests
import time

TOKEN = "8380699103:AAHRPHc0t4hdiuhr-uaJGDlmO4kDa0LxusE"

# RETE BERSAGLI PALOXIS NEXUS (4 GRUPPI + CONTROLLO)
GRUPPI = [
    "638656123",           # Il tuo ID (Monitor)
    "-1001669188418",      # Guadagno soldi online
    "-1002228507073",      # GUADAGNARE ONLINE
    "-1002574569776",      # BUONI GRATIS
    "-1003381479423"       # Nuovo Gruppo
]

def hunt():
    # Messaggio studiato per massimizzare i click sui tuoi 3 profili
    messaggio = (
        "🚀 **PROTOCOLLO GUADAGNO PALOXIS** 🚀\n\n"
        "Non stare a guardare gli altri che incassano. Ecco i bonus di OGGI:\n\n"
        "🏦 **BBVA: 50€ DI BENVENUTO**\n"
        "10€ Subito + 40€ di Cashback (Rimborsi spesa).\n"
        "👉 Codice: `77620062590929`\n\n"
        
        "💳 **REVOLUT: BONUS CASH**\n"
        "Registrati e attiva la carta dal link ufficiale.\n"
        "👉 Link: https://revolut.com/referral/?referral-code=pgallo!FEB1-26-AR-MDL-CTRL\n\n"
        
        "🐶 **BUDDYBANK (UniCredit):**\n"
        "👉 Codice: `B2601MP72BOYH9`\n\n"
        
        "💎 **ISYBANK:**\n"
        "👉 Codice: `8ACGT2HQVT`\n\n"
        "⚠️ *Messaggio automatico. Promo valide finché i codici sono attivi.*"
    )
    
    for chat_id in GRUPPI:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": chat_id, "text": messaggio, "parse_mode": "Markdown"}
        try:
            r = requests.post(url, data=data)
            if r.status_code == 200:
                print(f"✅ Inviato con successo a: {chat_id}")
            else:
                print(f"❌ Errore su {chat_id}: {r.text}")
        except Exception as e:
            print(f"🚨 Errore connessione: {e}")
        
        # Piccolo delay di 2 secondi per evitare il ban di Telegram
        time.sleep(2)

if __name__ == "__main__":
    hunt()

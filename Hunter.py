import requests

# CONFIGURAZIONE PALOXIS HUB
TOKEN = "8380699103:AAHRPHc0t4hdiuhr-uaJGDlmO4kDa0LxusE"
CHAT_ID = "638656123" # Ricorda di mettere il tuo ID reale o quello del gruppo

def hunt():
    messaggio = (
        "🔥 **PALOXIS NEXUS - GUADAGNO IMMEDIATO** 🔥\n\n"
        "Non stare a guardare, preleva i tuoi bonus ora. Ecco la lista aggiornata:\n\n"
        "🏦 **BBVA:** 10€ subito + Cashback\n"
        "👉 Codice: `77620062590929`\n\n"
        "💳 **REVOLUT:** Bonus variabile (fino a 60-100€)\n"
        "👉 Link: https://revolut.com/referral/?referral-code=pgallo!FEB1-26-AR-MDL-CTRL\n\n"
        "🐶 **BUDDYBANK:** Bonus iscrizione\n"
        "👉 Codice: `B2601MP72BOYH9`\n\n"
        "💎 **ISYBANK:** Bonus benvenuto\n"
        "👉 Codice: `8ACGT2HQVT`\n\n"
        "📈 **TRADING 212:** Azione gratuita in arrivo\n"
        "👉 Chiedimi info per la riattivazione!\n\n"
        "⚠️ *Posti limitati per ogni codice. Se non funziona uno, usa l'altro!*"
    )
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": messaggio, "parse_mode": "Markdown"}
    requests.post(url, data=data)

if __name__ == "__main__":
    hunt()

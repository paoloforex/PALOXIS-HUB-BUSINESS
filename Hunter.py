import requests
import time

TOKEN = "8380699103:AAHRPHc0t4hdiuhr-uaJGDlmO4kDa0LxusE"

# 🎯 NETWORK PALOXIS NEXUS
GRUPPI = ["638656123", "-1001669188418", "-1002228507073", "-1002574569776", "-1003381479423"]

# 💬 GUIDA COMPLETA BONUS (Risposta Automatica)
RISPOSTA_AUTO = (
    "🤖 **PALOXIS HUB - GUIDA AI BONUS ATTIVI**\n\n"
    "Vuoi i soldi? Segui queste istruzioni precise e non sbaglierai un colpo. 💸\n\n"
    
    "🏦 **1. BBVA (BONUS 50€)**\n"
    "• Scarica l'app BBVA e registrati.\n"
    "• Inserisci il codice: `77620062590929` durante l'apertura.\n"
    "• Deposita anche solo 5€ e fai un acquisto (o ricarica Amazon).\n"
    "• **RISULTATO:** Ricevi 10€ di bonus subito + 40€ di cashback sugli acquisti!\n\n"
    
    "💳 **2. REVOLUT (BONUS VARIABILE)**\n"
    "• Clicca qui: https://revolut.com/referral/?referral-code=pgallo!FEB1-26-AR-MDL-CTRL\n"
    "• Registrati e ordina la carta fisica (arriva gratis).\n"
    "• Fai 3 acquisti da almeno 5€ (anche con carta virtuale su Google/Apple Pay).\n"
    "• **RISULTATO:** Ricevi il bonus previsto dalla promo attuale!\n\n"
    
    "🐶 **3. BUDDYBANK (BONUS 40€/30€)**\n"
    "• Scarica l'app di UniCredit e inserisci il codice: `B2601MP72BOYH9`.\n"
    "• Apri il conto e ricevi il bonus appena completi i requisiti.\n\n"
    
    "💎 **4. ISYBANK (BONUS BUONI AMAZON)**\n"
    "• Scarica l'app Isybank e usa il codice: `8ACGT2HQVT`.\n\n"
    
    "📸 **ORA TOCCA A TE:**\n"
    "Appena completi un passaggio, **mandami lo screenshot qui**. Se hai dubbi o non sai come fare un acquisto virtuale, chiedi pure. Sono qui per farti guadagnare."
)

def spara_nei_gruppi():
    messaggio_gruppi = (
        "⚡ **PALOXIS HUB: IL SISTEMA CHE PAGA** ⚡\n\n"
        "Basta perdere tempo in gruppi inutili. Qui hai i bonus reali di Gennaio 2026.\n\n"
        "✅ **BBVA:** 50€ (Codice: `77620062590929`)\n"
        "✅ **REVOLUT:** Cash Bonus (Link in privato)\n"
        "✅ **BUDDYBANK:** Bonus UniCredit\n\n"
        "👉 **SCRIVIMI ORA** per ricevere la guida passo-passo automatica!"
    )
    for chat_id in GRUPPI:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": messaggio_gruppi, "parse_mode": "Markdown"})
        time.sleep(2)

def gestisci_risposte():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        updates = requests.get(url).json()
        if "result" in updates:
            for update in updates["result"]:
                if "message" in update and "chat" in update["message"]:
                    user_id = update["message"]["chat"]["id"]
                    if update["message"]["chat"]["type"] == "private":
                        url_send = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                        requests.post(url_send, data={"chat_id": user_id, "text": RISPOSTA_AUTO, "parse_mode": "Markdown"})
    except:
        pass

if __name__ == "__main__":
    spara_nei_gruppi()
    timeout = time.time() + 45
    while time.time() < timeout:
        gestisci_risposte()
        time.sleep(5)

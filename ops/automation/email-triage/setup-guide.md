# Setup Guide: Email Triage med n8n

## Översikt

Detta system:
- Läser mejl från Microsoft 365 varje timme
- Klassificerar med AI (viktigt/info/skip)
- Vidarebefordrar viktiga mejl till Gmail
- Skickar kalendersammanfattning kl 07:00

---

## 1. n8n Installation

### Alternativ A: n8n Cloud (enklast)
1. Gå till https://n8n.io
2. Skapa konto (gratis tier finns)
3. Klar!

### Alternativ B: Self-hosted på Google Cloud
```bash
# Cloud Run deployment
gcloud run deploy n8n \
  --image n8nio/n8n \
  --platform managed \
  --region europe-north1 \
  --allow-unauthenticated \
  --set-env-vars N8N_BASIC_AUTH_ACTIVE=true \
  --set-env-vars N8N_BASIC_AUTH_USER=admin \
  --set-env-vars N8N_BASIC_AUTH_PASSWORD=DITT_LÖSENORD
```

---

## 2. Microsoft 365 OAuth Setup

### Steg 1: Registrera app i Azure
1. Gå till https://portal.azure.com
2. Sök "App registrations" → New registration
3. Namn: `n8n-email-triage`
4. Redirect URI: `https://DIN-N8N-URL/rest/oauth2-credential/callback`
5. Spara **Application (client) ID**

### Steg 2: Skapa client secret
1. I appen → Certificates & secrets
2. New client secret
3. Spara **Value** (visas bara en gång!)

### Steg 3: API-behörigheter
1. API permissions → Add permission
2. Microsoft Graph → Delegated permissions:
   - `Mail.Read`
   - `Calendars.Read`
3. Grant admin consent

### Steg 4: Konfigurera i n8n
1. Credentials → New → Microsoft Outlook OAuth2
2. Fyll i:
   - Client ID: från steg 1
   - Client Secret: från steg 2
   - Scope: `openid offline_access Mail.Read Calendars.Read`
3. Connect och godkänn

---

## 3. Gmail OAuth Setup

### Steg 1: Google Cloud Console
1. Gå till https://console.cloud.google.com
2. Skapa nytt projekt: `n8n-email-triage`
3. APIs & Services → Enable APIs → Gmail API

### Steg 2: OAuth consent screen
1. OAuth consent screen → External
2. App name: `n8n-email-triage`
3. Lägg till scope: `gmail.send`

### Steg 3: Skapa credentials
1. Credentials → Create → OAuth client ID
2. Application type: Web application
3. Redirect URI: `https://DIN-N8N-URL/rest/oauth2-credential/callback`
4. Spara **Client ID** och **Client Secret**

### Steg 4: Konfigurera i n8n
1. Credentials → New → Gmail OAuth2
2. Fyll i Client ID och Secret
3. Connect och godkänn

---

## 4. OpenAI API Setup

1. Gå till https://platform.openai.com
2. API Keys → Create new secret key
3. I n8n: Credentials → New → OpenAI API
4. Klistra in API-nyckel

---

## 5. Importera Workflow

1. I n8n: Workflows → Import from file
2. Välj `n8n-workflow.json`
3. Uppdatera:
   - `DIN_GMAIL@gmail.com` → din Gmail-adress
   - Koppla credentials till varje node

---

## 6. Testa

1. Kör "Hämta nya mejl" manuellt
2. Verifiera att AI-klassificering fungerar
3. Kolla att Gmail tar emot test-mejl
4. Aktivera workflow

---

## Felsökning

### "No emails found"
- Kontrollera att det finns olästa mejl i M365
- Verifiera OAuth-scope inkluderar `Mail.Read`

### "AI returns invalid JSON"
- Kolla att OpenAI API-nyckel är giltig
- Testa med längre `bodyPreview` i prompten

### "Gmail send failed"
- Verifiera `gmail.send` scope
- Kolla att Gmail-konto är samma som OAuth

---

## Kostnadsuppskattning

| Tjänst | Kostnad |
|--------|---------|
| n8n Cloud | $20/mån (starter) |
| OpenAI API | ~$1-5/mån (gpt-4o-mini) |
| Google Cloud | Gratis tier räcker |
| **Totalt** | **~$25/mån** |

---

## Nästa steg (framtida förbättringar)

- [ ] Lägg till fler kategorier
- [ ] Slack-notiser för kritiska mejl
- [ ] Automatisk svarsförslag
- [ ] Veckosammanfattning

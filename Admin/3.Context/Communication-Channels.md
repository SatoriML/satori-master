# Communication-Channels & Protocols

## Kanalöversikt

### Teams (Intern Kommunikation)
**Primärt för:** Daglig koordinering, projektsamarbete, snabba avstämningar

**Användning:**
- **Daily Check-ins**: Morgon status updates
- **Project Discussions**: Tekniska detaljer och implementering  
- **Document Collaboration**: Real-time editing och feedback
- **Quick Questions**: Snabba svar på operativa frågor

**Best Practices:**
- Använd trådar för projektspecifika diskussioner
- @mentions för urgent items
- Dela skärm för complex förklaringar
- Archive viktiga decisions till dokumentation

**Integration:**
- Transkribera viktiga Teams-calls
- Spara critical decisions i Kunder/ dokumentation
- Link till relevanta dokument i conversations

### Email (Extern Kommunikation)
**Primärt för:** Kundkommunikation, partners, formell correspondents

**Användning:**
- **Kundkommunikation**: Professionell, strukturerad
- **Säljuppföljning**: Follow-ups efter möten
- **Projektleveranser**: Dokumentation och konfirmationer  
- **Avtal & Juridiskt**: Formal agreements och ändringar

**Email Standards:**
- Tydliga subject lines med [Projekt] eller [Kund] prefix
- Professional signatur med kontaktinfo
- CC relevant teammedlemmar för transparens
- Archive viktiga emails i kundmappar

**Response Time Expectations:**
- **Kunder**: <4 timmar under arbetstid
- **Hot prospects**: <2 timmar  
- **Interna**: <24 timmar
- **Leverantörer**: <48 timmar

### Telefon (Säljfokus)
**Primärt för:** Kalla samtal, urgent problem-solving, personal touch

**Användning:**
- **Cold Calling**: Initial prospecting
- **Sales Follow-up**: Efter möten och proposals
- **Crisis Management**: Snabba lösningar på kritiska issues
- **Relationship Building**: Personal connections med nyckelkunder

**Call Management:**
- Förbered talking points innan säljsamtal
- Ta anteckningar under samtalet
- Följ upp med email summary inom 2 timmar
- Dokumentera outcomes i kundmappar

### SMS (Ad-hoc Koordinering)  
**Primärt för:** Urgent coordination, meeting confirmations

**Användning:**
- **Meeting Confirmations**: Sista minuten confirmations
- **Urgent Updates**: När email för långsamt
- **Location Changes**: Meeting logistics
- **Quick Status**: "Running 10 min late" typ meddelanden

**SMS Guidelines:**
- Behåll professional ton även i SMS
- Följ upp kritisk information via email
- Använd endast för time-sensitive items
- Respektera arbetstider (08-18)

## Kommunikationsflöden per Scenario

### Ny Kundkontakt
```
Initial Contact (Telefon/Email)
    ↓
Research & Qualification (Internal Teams discussion)
    ↓  
Meeting Scheduling (Email med SMS backup)
    ↓
Pre-meeting Brief (Teams koordinering)
    ↓
Post-meeting Follow-up (Email + internal Teams update)
```

### Befintlig Kund - Projektuppdatering
```
Status Preparation (Teams koordinering)
    ↓
Customer Communication (Email med attachments)
    ↓
Customer Response Handling (Email primary, telefon om urgent)
    ↓
Internal Update (Teams summary)
    ↓
Documentation (Arkivering i kundmapp)
```

### Crisis/Urgent Issue
```
Issue Discovery (Any channel)
    ↓
Immediate Response (Telefon för direct contact)
    ↓
Team Coordination (Teams för lösningsframtagning)
    ↓
Customer Update (Email + telefon om major)
    ↓
Post-resolution Documentation (Email follow-up + arkivering)
```

## Integration med Admin Agents

### Morning-Commands Integration
Morning input kan specificera preferred kommunikationskanal:
- "Ring [Kund] idag för uppföljning"
- "Skicka email till [Prospect] med proposal"
- "Teams-möte med Martin om [Projekt]"

### Document-Manager Integration
All kommunikation arkiveras automatiskt:
- **Email**: Forward kritiska emails till arkivering
- **Teams**: Spara viktiga conversations som dokument
- **Telefon**: Summary notes dokumenteras
- **SMS**: Screenshot/kopia för critical items

## Communication Metrics

### Response Time Tracking
- Email response average
- Phone call return time
- Crisis resolution time
- Customer satisfaction med response

### Channel Effectiveness
- Conversion rates per kanal (email vs telefon)
- Customer preference tracking
- Meeting booking success rate per kanal

## Eskalationsprotokoll

### Interna Eskaleringhar
1. **Teams message** (Normal priority)
2. **Teams mention** (Medium priority)  
3. **Telefon** (High priority)
4. **SMS + Telefon** (Critical)

### Kund Eskaleringar
1. **Email** (Standard issues)
2. **Telefon + Email follow-up** (Urgent issues)
3. **Immediate phone + SMS** (Critical/crisis)

## Tools & Integration

### Current Tools
- **Teams**: Microsoft Teams for interno
- **Email**: [Specify email platform]  
- **Phone**: [Phone system]
- **SMS**: [SMS platform]

### Desired Integration
- **CRM Integration**: Link kommunikation till kundrecords
- **Automated Archiving**: Email→dokumentation flow
- **Response Tracking**: SLA monitoring
- **Communication Analytics**: Channel effectiveness data

---
*Dokumenterad av: CEO Joachim Sahlin*  
*Uppdaterad: 2025-09-04*
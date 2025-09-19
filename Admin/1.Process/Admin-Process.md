# Admin-Process

## Vision
CEO ska kunna prata in "morning commands" som automatiskt triggar rätt agenter för dagens möten och uppgifter.

## Huvudprocess - Morning Commands Workflow

### 1. MORNING INPUT (5-10 min)
**CEO Action**: Prata in dagens agenda som transcript
- "Idag har jag möte med [kund] kl 10, [ny kund] kl 14, och teammeeting kl 16"
- Särskilda prioriteringar eller fokusområden
- Viktiga decisions som behöver dokumenteras

### 2. AGENT DISPATCH (Automatisk)
**System Action**: Morning-Commands-Agent analyserar input och aktiverar rätt agenter

**För varje möte:**
- **Ny kund** → Meeting-Prep-NewCustomer-Agent aktiveras
- **Befintlig kund** → Meeting-Prep-ExistingCustomer-Agent aktiveras
- **Team meeting** → Document-Manager-Agent förbereder senaste beslut

### 3. PREPARATION PHASE (30-60 min före mötet)
**Agent Actions**: Parallell förberedelse

#### Ny Kund Research:
- Webbsökning: Företagsinformation, antal anställda, tillväxt
- Nyheter och historia
- Branschkontext och utmaningar
- Potentiella AI-användningsområden för kunden

#### Befintlig Kund Briefing:
- Läs alla dokument i Kunder/[KundNamn]/
- Senaste transcript från Transcript/
- Öppna todos och action items
- Pågående projekt och utmaningar
- Förbered frågor om aktuella utvecklingar

### 4. DELIVERY (15 min före möte)
**Output**: Färdiga briefings levereras
- Research-sammanfattning för nya kunder
- Kontext-briefing för befintliga kunder
- Föreslagna frågor och diskussionspunkter
- Relevant bakgrundsinformation

## Möteshantering

### Under Mötet
- **Transkription**: Alla möten transkriberas
- **Real-time notes**: Viktiga decisions antecknas

### Efter Mötet
- **Protocol Creation**: Skapa protokoll enligt befintlig prompt
- **Todo Extraction**: Extrahera action items
- **Document Archive**: Spara i rätt Kunder/ undermapp
- **Version Control**: Uppdatera versionsnummer (0.1, 0.2... → 1.0 för live)

## Kommunikationsflöden

### Interna Möten (2x/vecka)
- **Teams**: Daglig koordinering
- **Transkribering**: Spara under Transcript/
- **Protocol**: Standard meeting protocol
- **Follow-up**: Action items distribueras

### Externa Kunder
- **Email**: Primär kommunikation
- **Telefon**: Säljsamtal (kalla samtal)
- **Teams/SMS**: Projektkoordinering

## Dokumenthantering

### Arkivering Process
1. **Kategorisera**: Identifiera dokumenttyp (avtal, beslut, kommunikation)
2. **Placera**: Spara i korrekt Kunder/ undermapp
3. **Versionshantera**: Använd 0.1, 0.2... → 1.0 system
4. **Datera**: Alltid dagens faktiska datum (2025-09-04)
5. **Index**: Uppdatera relevanta övergripande dokument

### Version Control Standards
- **0.1-0.9**: Draft versions under utveckling
- **1.0**: Första live/färdiga versionen
- **1.1, 1.2...**: Uppdateringar av live dokument
- **Alltid datum**: Exakt datum för skapande/uppdatering

## Success Metrics
- **Mötesförberedelse**: 100% av möten har relevant briefing
- **Time to Brief**: Max 15 min från morning command till färdig briefing
- **Documentation Rate**: 100% av möten dokumenterade inom 24h
- **Agent Utilization**: Hur ofta morning commands används vs manuell förberedelse

## Prioriteringsprinciper
1. **Kundmöten**: Alltid högsta prioritet för förberedelse
2. **Säljmöten**: Kräver mest research (nya kunder)
3. **Interna möten**: Kontinuitet och uppföljning fokus
4. **Dokumentation**: Måste göras samma dag som mötet

---
*Process-ägare: CEO Joachim Sahlin*  
*Implementerad: 2025-09-04*
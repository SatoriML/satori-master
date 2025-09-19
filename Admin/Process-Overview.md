# Admin - Process-Overview

## Syfte
Administrative styrning och support som möjliggör effektiv CEO-verksamhet genom automatiserade "morning commands" och intelligent mötesförberedelse.

## Kärnprocess - Morning Commands
**Vision**: Prata in dagens agenda på morgonen → Agenter förbereder allt

### Huvudflöde
1. **MORNING INPUT** - CEO pratar in dagens agenda och prioriteringar
2. **AGENT ACTIVATION** - Rätt agenter aktiveras baserat på dagens möten
3. **PREPARATION** - Agenter researchar, sammanställer och förbereder
4. **DELIVERY** - Färdiga briefings och dokument levereras innan möten

## Struktur

### 1.Process/
- **Admin-Process.md** - Komplett process för morning commands och möteshantering

### 2.Agents/
- **Meeting-Prep-NewCustomer-Agent.md** - Webbresearch för nya kunder
- **Meeting-Prep-ExistingCustomer-Agent.md** - Genomgång av kunddokumentation  
- **Document-Manager-Agent.md** - Arkivering och versionshantering
- **Morning-Commands-Agent.md** - Koordinerar andra agenter från daglig input

### 3.Context/
- **Meeting-Types.md** - Olika mötestyper och krav
- **Document-Flow.md** - Hur dokument hanteras i Kunder/
- **Communication-Channels.md** - Teams, email, telefon

### 4.Templates/
- **Meeting-Protocol-Template.md** - Standardformat för mötesprotokoll
- **Research-Brief-Template.md** - Format för kundresearch
- **Daily-Command-Template.md** - Mall för morning input

## Snabbkommandon
- `"Morning commands för idag"` - Aktivera hela morning workflow
- `"Förbered möte med [ny kund]"` - Research och analys för säljmöte
- `"Förbered möte med [befintlig kund]"` - Genomgång av kunddokumentation
- `"Arkivera dokument från [meeting]"` - Spara och versionshantera

## Integration Points

### Dataflöde IN (från andra processer):
- **Sälj**: Säljmötespotential kräver kundresearch från Meeting-Prep-NewCustomer-Agent
- **Kunder**: Befintlig kunddokumentation behöver sammanställas före kundmöten
- **Huvudstrategi**: Strategiska prioriteringar påverkar vilka möten som prioriteras
- **Tjänster**: Service delivery möten kräver projektspecifik förberedelse

### Dataflöde UT (till andra processer):
- **Meeting protocols** → Kunder/ (arkiveras per kund)
- **Action items** → relevanta processer baserat på meeting outcome
- **Customer insights** → Sälj (för förbättra future säljpitch)
- **Strategic feedback** → Huvudstrategi (från important möten)

### Agent-till-Agent kommunikation:
- **Morning-Commands-Agent** triggar Meeting-Prep-agents
- **Document-Manager-Agent** synkroniserar med Kunder/Customer-Health-Agent
- **Meeting-Prep results** feeds till Sälj/Sales-Meeting-Prep-Agent

---
*Process-ägare: CEO Joachim Sahlin*  
*Uppdaterad: 2025-09-04*
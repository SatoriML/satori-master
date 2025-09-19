# Daily Command Template - Morning Input

**Datum**: 2025-09-04  
**Tid för input**: [HH:MM]  
**Input method**: [Voice transcript/Written/Mixed]

---

## Morning Command Format

### Dagens Agenda - Prioritetsordning
```
"Idag har jag:
- [Tid] - [Mötestyp] med [Person/Företag] - [Kort beskrivning]
- [Tid] - [Mötestyp] med [Person/Företag] - [Kort beskrivning]  
- [Tid] - [Aktivitet] - [Beskrivning]

Prioriteringar idag:
1. [Högsta prioritet - vad som MÅSTE göras]
2. [Medium prioritet - viktigt men kan justeras]
3. [Låg prioritet - om tid finns]

Special focuses:
- [Särskild sak att fokusera på]
- [Beslut som behöver fattas]
- [Uppföljning som är urgent]
"
```

### Agent Dispatch Automatik
**Morning-Commands-Agent** kommer automatiskt att:

#### För Möten:
- **Nya kunder/prospects** → Meeting-Prep-NewCustomer-Agent aktiveras
- **Befintliga kunder** → Meeting-Prep-ExistingCustomer-Agent aktiveras  
- **Team/interna möten** → Document-Manager förbereder senaste interna dokument

#### För Uppföljning:
- **"Protokoll från [möte]"** → Document-Manager för arkivering
- **"Följ upp [ämne]"** → Relevant agent för statusuppdatering
- **"Rapport om [område]"** → Koordinering av relevanta agents för rapportering

## Exempel på Morning Commands

### Exempel 1 - Säljintensiv Dag
```
"Idag har jag:
- 10:00 - Säljmöte med TechCorp AB - första mötet, nytt företag inom fintech
- 14:00 - Kundmöte med Nordea - uppföljning på satori-chat implementering
- 16:00 - Teammöte med Martin - diskutera utvecklingspriorities

Prioriteringar idag:
1. TechCorp säljmöte MÅSTE gå bra - viktigt för Q4 target
2. Nordea renewal conversation - avtal går ut nästa månad
3. Utvecklingspriorities med Martin - kan skjutas om nödvändigt

Special focus:
- Research TechCorp ordentligt - de verkar ha mycket potential  
- Förbered expansion proposal för Nordea
- Beslut om resource allocation för Q1 development
"
```

**Agent Response:**
- Meeting-Prep-NewCustomer-Agent: Djupresearch på TechCorp AB
- Meeting-Prep-ExistingCustomer-Agent: Full kundgenomgång Nordea + expansion förslag
- Document-Manager-Agent: Förbered development roadmap för teammöte

### Exempel 2 - Administrativ Dag
```
"Idag fokuserar jag på:
- 09:00 - Genomgång av månadsrapporter
- 11:00 - Protokoll från gårdagens strategimöte behöver skrivas
- 14:00 - Planering av nästa veckas kundmöten
- 16:00 - Email catch-up och uppföljning

Prioriteringar:
1. Månadsrapporter MÅSTE bli klara för styrelsen  
2. Strategiprotokoll så decisions inte glöms bort
3. Nästa vecka planering för optimal prep

Special focus:
- Identifiera månadens top wins för styrelserapporten
- Säkerställ att alla strategic decisions dokumenteras ordentligt
- Optimera nästa veckas meeting prep för maximal effektivitet  
"
```

**Agent Response:**
- Document-Manager-Agent: Sammanställ månadsdata från alla områden
- Meeting-Protocol-Creation: Process gårdagens strategimöte transcript
- Morning-Commands-Agent: Förhandsanalys av nästa veckas meetings för optimerad prep

## Input Guidelines

### Vad som Hjälper Agents
✅ **Specifika tider**: "10:00 möte" istället för "möte på förmiddagen"  
✅ **Tydlig kategorisering**: "Säljmöte", "Kundmöte", "Teammöte"  
✅ **Kontextinfo**: "Första mötet med dem", "Renewal conversation"  
✅ **Prioritetsordning**: Nummer 1, 2, 3 för tydlighet  
✅ **Special circumstances**: "Mycket viktigt", "Kan skjutas", "Urgent"

### Vad som Förvirrar Agents  
❌ **Vaga tider**: "Någon gång på eftermiddagen"  
❌ **Oklara mötetyper**: "Träff med folk"  
❌ **Saknad kontext**: "Möte med Nordea" (nytt/befintligt?)  
❌ **Ingen prioritering**: Allt lika viktigt  
❌ **Abstrakt språk**: "Fixa grejer", "Kolla på saker"

## Output Förväntningar

### Vad Du Får Tillbaka (inom 30-60 min)
- **Meeting Briefs**: Färdiga briefings för alla möten
- **Research Reports**: Komplett företagsanalys för nya prospects  
- **Customer Status**: Aktuell status och förslag för befintliga kunder
- **Document Preparation**: Relevanta dokument och templates förberedda
- **Timeline Confirmation**: Bekräftelse på att allt blir klart i tid

### Leveransschema
- **09:00**: Morning Commands input
- **09:30**: Agent dispatch bekräftelse  
- **10:00-10:30**: Första deliverables klar (snabba briefs)
- **10:30-11:00**: Kompletta research reports klar
- **11:00+**: Alla materials redo för dagen

---

**Usage Tips:**
- Prata naturligt - agents förstår kontext
- Inkludera "why" inte bara "what" för bättre prioritering  
- Nämn special circumstances som påverkar approach
- Säg till om något är extra viktigt eller kan skjutas

**Integration:**
- Input sparas i Admin/Daily-Commands/[Date].md
- Agent responses arkiveras för lärdomar och förbättringar
- Success metrics spåras för kontinuerlig optimering

---
*Template för Morning-Commands-Agent workflow*  
*Skapad: 2025-09-04*
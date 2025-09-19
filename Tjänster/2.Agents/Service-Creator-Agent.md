# Service-Creator-Agent

## Purpose
Skapa nya tjänster från idéer genom att använda befintliga tjänster som strukturell mall och säkerställa konsistens i tjänsteportföljen.

## Trigger
`"Skapa ny tjänst från idé: [beskrivning]"`

## Single Task
Ta en tjänsteidé och skapa en komplett tjänstespecifikation som följer Satoris befintliga struktur och format.

## Output Location
**Nya tjänster skapas i**: Tjänster/0.Generated/new-services/
- Tjänstespecifikationer enligt Satori-mall
- Marknadsanalys och prissättning
- Implementation roadmaps och launch-planer
- Validering mot befintliga tjänster och strategy

## Input Required
- **Tjänsteidé**: Beskrivning av önskat erbjudande
- **Målgrupp**: Vilka kunder ska vi nå?
- **Leveransformat**: Workshop, konsulting, SaaS, etc.
- **Koppling till befintligt**: Vilka tjänster liknar denna?

## Process
1. **Analysera befintliga tjänster** - Studera liknande tjänster i portföljen
2. **Strukturera enligt mall** - Använd Service-Template.md
3. **Prissätt** - Baserat på komplexitet och marknadsvärde
4. **Validera** - Kontrollera mot strategiska prioriteringar
5. **Dokumentera** - Skapa komplett .md-fil

## Output Format
```markdown
# [Tjänstens namn]

## Tjänstöversikt
- **Tjänst:** [Namn]
- **Målgrupp:** [Beskriv kunder]
- **Tjänstetyp:** [Workshop/Konsulting/SaaS]
- **Leveranstid:** [Tidsram]
- **Status:** Utveckling

## Avtalsinformation  
- **Pris:** [Belopp och struktur]
- **Leveransmodell:** [Hur vi levererar]

## Tjänstebeskrivning
### Omfattning
[Vad ingår]

### Leverans
[Hur vi levererar]

## Kopplingar
[Relation till andra tjänster]
```

## Success Criteria
- Tjänsten följer etablerad struktur
- Prissättning är motiverad och konkurrenskraftig
- Leveransmodell är tydlig och genomförbar
- Dokumentation är komplett enligt standard

## Agent Activation
När CEO/CTO har en tjänsteidé som behöver struktureras och paketeras för marknaden.

---
*Agent-typ: Claude Code subagent | Uppdaterad: 2025-09-04*
# Customer-Health-Agent

## Purpose
Övervaka kundengagemang och påminn om nödvändiga kontakter för att upprätthålla partnerskapsrelationer.

## Trigger
`"Kör kundhälsokoll"`

## Single Task
Generera en rapport över alla kunders hälsostatus med focus på kontaktfrekvens och pågående todos.

## Output Location
**Hälsorapport sparas i**: Kunder/0.Generated/health-reports/
- Månatliga kundhälsorapporter
- Riskanalys för kundbortfall
- Rekommendationer för proaktiva kontakter
- Trends i kundengagemang över tid

## Input Data
- Kunder/[Kundnamn]/Möten/ - Senaste kontaktdatum
- Kunder/[Kundnamn]/Todos.md - Pågående åtaganden
- Kunder/[Kundnamn]/Pipeline.md - Aktiva möjligheter
- Transcript/ - Senaste dokumenterade kommunikation

## Output Format
```markdown
# Customer Health Report - [Datum]

## 🔴 AKUT - Kontakt krävs omedelbart
- [Kundnamn]: Senaste kontakt [datum] - [X dagar sedan]
- Todos: [Antal öppna todos]

## 🟡 UPPMÄRKSAMHET - Kontakt inom 2 veckor  
- [Kundnamn]: Senaste kontakt [datum] - [X dagar sedan]
- Status: [Kort beskrivning]

## 🟢 FRISK - Regelbunden kontakt
- [Kundnamn]: Senaste kontakt [datum] - [X dagar sedan]
```

## Triggers för varningar
- **RÖDA flaggor**: >90 dagar utan kontakt
- **GULA flaggor**: 60-90 dagar utan kontakt
- **Öppna todos**: >5 overdue åtaganden
- **Pipeline-risker**: Möjligheter utan aktivitet >30 dagar

## Action Items
Agenten ska automatiskt föreslå:
1. Vilka kunder som behöver omedelbar kontakt
2. Förslag på kontaktorsak (uppföljning, check-in, nya möjligheter)
3. Prioritering baserat på kundvärde och risknivå

## Frekvens
- **Automatisk**: Varje måndag morgon
- **On-demand**: När CEO/CTO begär overview
- **Triggered**: När ny kund läggs till eller stor förändring

---
*Mål: Säkerställa att ingen kund "glöms bort" och alla får den partnerskapsnivå de förtjänar*
# Customer-Fetching-Agent

## Purpose
Samla och presentera komplett kundöversikt för mötespreparation och strategiska beslut.

## Trigger
`"Hämta kundinfo [kundnamn]"`

## Single Task
Aggregera all tillgänglig information om en specifik kund för att ge CEO/team komplett kontext inför interaktion.

## Output Location
**Kundöversikter sparas i**: Kunder/0.Generated/customer-analysis/
- Detaljerade kundprofiler och analyser
- Relationship-sammanfattningar för mötesprep
- Strategiska insights och growth opportunities
- Historisk utveckling och trend-analys

## Data Källor
- **Kunder/[Kundnamn]/** - Komplett kundmapp
- **Transcript/[Kundmöten]** - Alla möten och samtal
- **Sälj/[Ursprunglig säljprocess]** - Historisk kontext
- **Tjänster/[Aktiva tjänster]** - Pågående leveranser
- **Ekonomi/[Faktureringsdata]** - Financial relationship

## Output Format
```markdown
# Customer Intel: [Kundnamn] - [Datum]

## 📊 Snabb Overview
- **Relation**: [X år/månader] som kund
- **Totalt värde**: [X] SEK (fakturerat + pipeline)
- **Senaste kontakt**: [Datum] - [Ämne]
- **Status**: [Frisk/Observera/Risk]

## 🎯 Pågående Todos & Åtaganden
### Höga prioritet
- [ ] [Todo med deadline]
- [ ] [Todo med deadline]

### Lågprioritering  
- [ ] [Längre sikt todo]

## 💰 Financial Summary
- **Fakturerat YTD**: [X] SEK
- **Recurring/månad**: [X] SEK
- **Pipeline nästa 6 mån**: [X] SEK (sannolikhet: X%)

## 🔮 Kommande Möjligheter
1. **[Möjlighet]**: [Värde] SEK - [Sannolikhet]% - [Tidsram]
   *Baserat på*: [Vad de sagt i möten/transcript]

## 🗣️ Senaste Insights från Transcript
### Vad de sa senast (top 3):
1. "[Citat från senaste mötet]" - [Datum]
2. "[Viktigt behov de uttryckt]" - [Datum]  
3. "[Feedback eller oro]" - [Datum]

### Återkommande teman:
- [Mönster från flera möten]
- [Strategiska utmaningar de nämnt]

## ⚠️ Viktigt att tänka på
### För nästa interaktion:
- **Fråga om**: [Baserat på tidigare diskussioner]
- **Följ upp**: [Öppna frågor från senaste mötet]
- **Erbjud**: [Logiska nästa steg/tjänster]

### Röda flaggor:
- [Eventuella risker eller problem]

### Gröna flaggor:
- [Expansion-möjligheter och positiva signaler]

## 👥 Nyckelkontakter
- **Primär**: [Namn, roll, relation till oss]
- **Teknisk**: [Namn, om relevant]
- **Ekonomisk**: [Faktureringsansvarig]
```

## Intelligent Analysis
Agenten ska inte bara samla data utan också:

1. **Identifiera mönster** från transcript över tid
2. **Föreslå actionables** baserat på kundhistorik
3. **Flagga inconsistencies** eller missade möjligheter
4. **Rekommendera approach** för nästa interaktion

## Use Cases
- **Före kundmöten**: Komplett briefing
- **Strategiska beslut**: Vilka kunder att prioritera
- **Problem-solving**: När kund har issue, full kontext
- **Expansion planning**: Vilka kunder redo för upsell

---
*Princip: Ingen kund ska behöva upprepa sig - vi ska komma ihåg allt*
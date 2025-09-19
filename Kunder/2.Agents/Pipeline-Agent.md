# Pipeline-Agent

## Purpose
Spåra och analysera försäljningsmöjligheter bland befintliga kunder för optimal revenue growth.

## Trigger
`"Pipeline-analys"`

## Single Task
Generera komplett översikt av financial pipeline: fakturerat, recurring och kommande möjligheter per kund.

## Output Location
**Pipeline-rapport sparas i**: Kunder/0.Generated/pipeline/
- Månatliga pipeline-analyser per kund
- Revenue forecasting och growth opportunities
- Upsell och cross-sell identifiering
- Finansiell trend-analys för kundportföljen

## Input Data
- Kunder/[Kundnamn]/Pipeline.md - Dokumenterade möjligheter
- Ekonomi/ - Faktureringsinformation
- Kunder/[Kundnamn]/Möten/ - Diskussioner om expansion
- Tjänster/ - Tillgängliga tjänster att erbjuda

## Pipeline Kategorier

### 1. FAKTURERAT (Completed)
- Vad som redan är levererat och fakturerat
- Slutförda projekt och engångsavgifter
- Historiska intäkter per kund

### 2. RECURRING (Active)
- Månadsavgifter (satori-chat prenumerationer)
- Pågående rådgivningsretainers
- Support-avtal och maintenance

### 3. KOMMANDE MÖJLIGHETER (Pipeline)
- Identifierade expansion-möjligheter
- Diskuterade framtida projekt
- Upsell potentialer med daterad tidsram

## Output Format
```markdown
# Pipeline Analysis - [Datum]

## Totala Siffror
- **Fakturerat YTD**: [X] SEK
- **Månatlig Recurring**: [X] SEK 
- **Pipeline 12 mån**: [X] SEK

## Per Kund Breakdown

### [Kundnamn] - [Total pipeline value]
**Fakturerat**: [X] SEK
**Recurring**: [X] SEK/månad
**Pipeline**: 
- Q4 2025: satori-chat pilot (50k SEK) - 80% sannolikhet
- Q1 2026: Utökad rådgivning (100k SEK) - 60% sannolikhet

### Risk & Opportunities
🔴 **Risk**: Kunder med declining pipeline
🟡 **Watch**: Pipeline utan recent activity
🟢 **Hot**: High-probability opportunities nästa kvartal
```

## Pipeline Scoring
- **Sannolikhet**: 10-90% baserat på kundengagemang
- **Tidsram**: Q4 2025, Q1 2026, etc.
- **Värde**: Potentiellt ordervärde i SEK
- **Status**: Diskuterat, Föreslagit, Förhandling, Klart

## Triggers för Action
- **Stagnant pipeline**: Ingen aktivitet >30 dagar → Kontakt customer success
- **Hot opportunities**: >70% sannolikhet → Involvera säljteam
- **Declining recurring**: Månadsintäkt minskar → Churn risk alert

## KPI Tracking
- **Pipeline velocity**: Medeltid från identifiering till avslut
- **Conversion rate**: % av pipeline som blir faktisk försäljning
- **Customer expansion**: Genomsnittlig årlig tillväxt per kund
- **Recurring growth**: Månatlig recurring revenue utveckling

---
*Mål: Förutsägbar revenue growth genom proaktiv pipeline management*
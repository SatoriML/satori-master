# Sälj - Process-Overview

## Syfte
Satoris säljprocess för att konvertera cold leads till kunder genom Satori CRM och strukturerad uppföljning.

## Kärnprocess (3 steg)
1. **PROSPEKTERA** - Cold calling via Satori CRM från alla bolag
2. **KVALIFICERA** - Ingen befintlig AI-partner + nyfikenhet på generativ AI
3. **KONVERTERA** - Strukturerad säljprocess (veckor till månader)

## Målprofiler
- **satori-chat**: IT-chefer, 100+ anställda
- **satori-uppstart**: Mindre organisationer, ~50 anställda

## Säljfilosofi
- **Volym är allt**: Stor pipeline som fylls på konstant
- **Alla leads tas**: Ingen prioritering, ta alla möjligheter
- **Datum på allt**: Varje lead måste vara datumssatt
- **Automatisk rensning**: Gamla inaktiva leads rensas bort

## Agenter
- `"Kör lead-kvalificering"` - Kontrollera hälsosignaler och nyheter
- `"Berika kunddata"` - Hitta beslutsfattare och organisationsinfo
- `"Förbered säljmöte"` - Komplett mötesprep inkl. transcripts
- `"Uppdatera pipeline"` - Håll ordning och rensa gamla leads
- `"Analysera pipeline"` - Grafer och insikter över utveckling

## Integration Points

### Dataflöde IN (från andra processer):
- **Marketing**: Qualified leads från LinkedIn och SEO för prospektering
- **Admin**: Meeting prep data och customer research för säljmöten
- **Huvudstrategi**: Strategic priorities och focus areas för target selection
- **Tjänster**: Current service offerings och pricing för sales presentations

### Dataflöde UT (till andra processer):
- **Won deals** → Kunder (nya kunder skapas från successful closes)
- **Customer feedback** → Marketing (what resonates i säljprocessen)
- **Sales insights** → Huvudstrategi (market demand och competitor intelligence)
- **Meeting protocols** → Admin (dokumentation av säljsamtal)

### Agent-till-Agent kommunikation:
- **Lead-Qualification-Agent** → receives Market intelligence från Marketing/Market-Research-Agent
- **Sales-Meeting-Prep-Agent** → coordinates med Admin/Meeting-Prep-ExistingCustomer-Agent
- **Pipeline-Analytics-Agent** → feeds data till Huvudstrategi/KPI-Tracker-Agent
- **Data-Enrichment-Agent** → levererar prospect research till Admin/Morning-Commands-Agent

## Snabbkommandon
- `"Förbered möte med [kund]"` - Aktiverar Sales-Meeting-Prep-Agent
- `"Pipeline-review"` - Veckovis genomgång av alla aktiva leads
- `"Rensa pipeline"` - Automatisk rensning av gamla inaktiva leads

---
*Uppdaterad: 2025-09-04*
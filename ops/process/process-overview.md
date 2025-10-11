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
- **Growth**: Qualified leads från LinkedIn, events och inbound i `growth/campaigns/`
- **Ops**: Meeting prep data och customer research i `ops/process/` & `ops/transcripts/`
- **Strategy**: Fokusområden dokumenterade i `ops/index/catalog.md`
- **Services**: Aktuella erbjudanden och pricing i `ops/reference/services/`

### Dataflöde UT (till andra processer):
- **Won deals** → `clients/<kund>/` (nya kunder skapas från successful closes)
- **Customer feedback** → `growth/context/` (vad som resonerar i säljprocessen)
- **Sales insights** → `ops/index/catalog.md` (market demand & competitor intelligence)
- **Meeting protocols** → `ops/transcripts/` (dokumentation av säljsamtal)

### Agent-till-Agent kommunikation:
- **Lead-Qualification-Agent** → tar marknadsinsikter från `growth/context/`
- **Sales-Meeting-Prep-Agent** → koordinerar med `.claude/agents/meeting-prep-agent.md`
- **Pipeline-Analytics-Agent** → skickar status till strategiägare (registrerade i `ops/index/catalog.md` och `ops/index/manifest.json`)
- **Data-Enrichment-Agent** → levererar prospect research till dagliga ops-kommandon

## Snabbkommandon
- `"Förbered möte med [kund]"` - Aktiverar Sales-Meeting-Prep-Agent
- `"Pipeline-review"` - Veckovis genomgång av alla aktiva leads
- `"Rensa pipeline"` - Automatisk rensning av gamla inaktiva leads

---
*Uppdaterad: 2025-09-04*

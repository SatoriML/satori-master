# Kunder - Process-Overview

## Syfte
Partnerskapsfokuserat kundarbete med kvartalsvis uppföljning för långsiktig affärstillväxt.

## Kundprofil
- **Storlek**: 30-300 anställda
- **Branscher**: Ideell sektor, förbund, studieförbund, idrottsorganisationer
- **Nuvarande**: 15 kunder
- **Tillväxtmål**: +10 kunder/år

## Kärnprocess (4 steg)
1. **ONBOARDING** - Komplett kunddata från säljprocessen
2. **LEVERANS** - satori-uppstart (8 veckor)
3. **PARTNERSKAP** - Kvartalsvis kontakt minimum
4. **EXPANSION** - Pipeline för upsell-möjligheter

## Aktiva Agenter
- **Customer-Health-Agent**: Övervakar todos och kontakthistorik
- **Onboarding-Agent**: Checklista för komplett kunddata
- **Pipeline-Agent**: Fakturerat + recurring + möjligheter
- **Customer-Fetching-Agent**: Hämtar all kundinfo för mötesprep

## Snabbkommandon
- `"Kör kundhälsokoll"` - Health check alla kunder
- `"Onboarding för [kund]"` - Ny kundprocess
- `"Pipeline-analys"` - Försäljningsmöjligheter
- `"Hämta kundinfo [kund]"` - Komplett kundöversikt

## Integration Points

### Dataflöde IN (från andra processer):
- **Sälj**: Nya kunder från won deals, handover från säljprocess
- **Admin**: Meeting protocols och customer touchpoints
- **Tjänster**: Project deliveries och service completion updates
- **Huvudstrategi**: Customer success metrics för strategic review

### Dataflöde UT (till andra processer):
- **Customer success stories** → Marketing (anonymiserat för content)
- **Customer health data** → Huvudstrategi (retention och growth insights)
- **Upsell opportunities** → Sälj (expansion possibilities)
- **Service feedback** → Tjänster (improvement opportunities)

### Agent-till-Agent kommunikation:
- **Customer-Health-Agent** → alerts Sälj/Pipeline-Agent för at-risk accounts
- **Onboarding-Agent** → coordinates med Tjänster/Service-Delivery-Agent
- **Pipeline-Agent** → feeds opportunities till Sälj/Sales-Pipeline-Agent
- **Customer-Fetching-Agent** → provides research för Admin/Meeting-Prep-agents

---
*Uppdaterad: 2025-09-04*
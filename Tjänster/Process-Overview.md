# Tjänster - Process-Overview

## Syfte
Satoris tjänsteportfölj och leveransprocess för att skapa, leverera och kontinuerligt förbättra AI-tjänster baserat på kundefterfrågan.

## Kärnprocess (3 steg)
1. **UTVECKLA** - Från kundförfrågan/idé till färdig tjänstepaket
2. **LEVERERA** - Strukturerad leverans med kvalitetssäkring
3. **FÖRBÄTTRA** - Feedback-driven utveckling och optimering

## Prioriterade Tjänster (Q3 2025)
1. **satori-chat** - Mest lönsam kortsiktigt
2. **satori-uppstart** - Fokus för återkommande intäkt (10k/mån x 6 månader)
3. **satori-consulting** - Löpande konsulting 
4. **satori-ai-advisor** - Strategisk rådgivning

## Agenter i Mappen
- **Service-Creator-Agent** - Skapar nya tjänster från idéer
- **Service-Improver-Agent** - Förbättrar tjänster baserat på feedback
- **Service-Delivery-Agent** - Koordinerar leverans från sälj

## Struktur
```
1.Process/       # Huvudprocess för tjänsteutveckling
2.Agents/        # Automatisering för tjänstehantering
3.Context/       # Tjänsteportfölj och prioriteringar
4.Templates/     # Mallar för nya tjänster och feedback
```

## Snabbkommandon
- `"Skapa ny tjänst från idé"` → Service-Creator-Agent
- `"Förbättra tjänst med feedback"` → Service-Improver-Agent  
- `"Koordinera tjänsteleverans"` → Service-Delivery-Agent

## Integration Points

### Dataflöde IN (från andra processer):
- **Huvudstrategi**: Strategic priorities och service development fokus areas
- **Sälj**: Won deals som kräver service delivery coordination
- **Kunder**: Customer feedback och feature requests för service improvement
- **Marketing**: Market research och customer demands för new service ideas

### Dataflöde UT (till andra processer):
- **Service updates** → Marketing (för content och communication)
- **New service offerings** → Sälj (för pipeline och pricing updates)
- **Delivery completion** → Kunder (för customer success tracking)
- **Service performance metrics** → Huvudstrategi (för strategic review)

### Agent-till-Agent kommunikation:
- **Service-Creator-Agent** → coordinates med Marketing/Market-Research-Agent för demand validation
- **Service-Delivery-Agent** → syncs med Kunder/Onboarding-Agent för seamless handover
- **Service-Improver-Agent** → receives feedback från Kunder/Customer-Health-Agent
- **All service agents** → feed performance data till Huvudstrategi/Process-Health-Agent

---
*Uppdaterad: 2025-09-04 | Kunddrivet + proaktiv innovation*
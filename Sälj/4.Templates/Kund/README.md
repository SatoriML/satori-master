# Kund Folder Template

Detta är standard mappstrukturen för alla nya kunder/prospects i Satori systemet.

## Struktur
```
[Företagsnamn]/
├── 1.Möten/           # Mötesprotokoll och agenda
├── 2.Timmar-fakturering/  # Tidrapporter och fakturering  
├── 3.Tjänster/        # Tjänstebeskrivningar och leveranser
├── 4.Strategi/        # Strategisk kunddata och planering
├── 5.Notes-Todos/     # Löpande anteckningar och uppgifter
└── [Företagsnamn].md  # Huvudsaklig kundkort/pipeline-fil
```

## Användning

### För Data-Enrichment-Agent
Denna struktur används automatiskt när nya prospects läggs till via:
- `"Add prospect [företag]"`
- `"New lead [företag] [website]"`
- `"Quick prospect [företag]"`

### För Won Deals
När ett deal går från Pipeline → Won, flyttas hela mappstrukturen från:
- `Sälj/5.Pipeline/[Fas]/[Företag]/` → `Kunder/[Företag]/`

### Konsistens
Samma struktur används i:
- **Pipeline prospects** (Sälj/5.Pipeline/)
- **Won customers** (Kunder/)
- **Partnership deals** (med samma struktur)

## Syfte
- **Organiserad dokumentation** från dag 1
- **Professionell approach** även för prospects  
- **Smidig transition** från prospect till kund
- **Systematisk struktur** för all kunddata

---
*Template för Satori Customer Management System*  
*Senast uppdaterad: 2025-09-04*
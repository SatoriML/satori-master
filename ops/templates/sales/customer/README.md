# Client Folder Template

Standardlayout för nya prospects och kunder i den förenklade strukturen.

## Struktur
```
[kund-slug]/
├── overview.md               # Översikt & status (utgå från overview-template.md)
├── journal.md                # Löpande datumanteckningar (starta från journal-template.md)
├── contracts/                # Avtal, offerter, legalt material
└── deliverables/             # Leveranser, strategier, presentationer m.m.
```

`.gitkeep`-filerna säkrar att mapparna följer med vid kopiering – behåll dem eller ersätt med första riktiga dokumentet. Lägg till fler undermappar (t.ex. `assets/media/`) när behov uppstår.

## Användning
- Kopiera hela `ops/templates/sales/customer/` till `clients/<kund-slug>/`.
- Byt namn på `overview-template.md` till `overview.md` och fyll i front matter + snapshot.
- Byt namn på `journal-template.md` till `journal.md` och fortsätt fylla på med datumrader.
- Lägg avtal i `contracts/` och övrigt material i `deliverables/`; skapa undermappar vid behov.
- Arkivera avslutade kunder genom att flytta hela mappen till `archive/<Kvartal>/`.

## Skapande
- Prospects utan mapp: kopiera denna struktur från `ops/templates/sales/customer/`.
- Won deals: flytta mappen till `clients/<Namnet>/` och konvertera till aktiv kund.
- Arkivera avslutade kunder genom att flytta mappen till `archive/<Kvartal>/`.

## Syfte
- **Snabb överblick** via `overview.md`.
- **Delad sanningskälla** för alla interaktioner.
- **Minimal friktion** när prospects blir kunder.
- **Konsistent naming** för automations och manuella flöden.

---
*Template för Satori Client Management System*  
*Senast uppdaterad: 2025-10-12*

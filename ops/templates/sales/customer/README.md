# Client Folder Template

Standardlayout för nya prospects och kunder i den förenklade strukturen.

## Struktur
```
[Företagsnamn]/
├── notes.md                  # Översikt & status (utgå från notes-template.md)
├── log/                      # Daterade anteckningar och mötesprep
│   └── YYYY-MM-DD_topic.md
└── assets/                   # Material kunden fått eller delat
    ├── contracts/
    ├── time/
    ├── strategy/
    └── service/
```

`.gitkeep`-filerna säkrar att mapparna följer med vid kopiering – behåll dem eller ersätt med första riktiga dokumentet. Lägg till fler undermappar (t.ex. `assets/media/`) när behov uppstår.

## Användning
- Kopiera hela `ops/templates/sales/customer/` till `clients/<Företagsnamn>/`.
- Byt namn på `notes-template.md` till `notes.md` och fyll i front matter + snapshot.
- Lägg mötesbrev, call-prep och uppföljning i `log/` med datumprefix (`YYYY-MM-DD_subject.md`).
- Parkera offerter, avtal, tidrapporter och övriga referenser i `assets/` och dess underkategorier.
- Arkivera avslutade kunder genom att flytta hela mappen till `archive/<Kvartal>/`.

## Skapande
- Prospects utan mapp: kopiera denna struktur från `ops/templates/sales/customer/`.
- Won deals: flytta mappen till `clients/<Namnet>/` och konvertera till aktiv kund.
- Arkivera avslutade kunder genom att flytta mappen till `archive/<Kvartal>/`.

## Syfte
- **Snabb överblick** via `notes.md`.
- **Delad sanningskälla** för alla interaktioner.
- **Minimal friktion** när prospects blir kunder.
- **Konsistent naming** för automations och manuella flöden.

---
*Template för Satori Client Management System*  
*Senast uppdaterad: 2025-09-21*

# Kontextschema – LinkedIn Content Agent

| Lager | Syfte | Fil(er) | Användning |
| --- | --- | --- | --- |
| **Agentstyrning** | Process och arbetsflöde för agenten | `linkedin-agent-export.md` | Startpunkt för varje skrivsession, beskriver roller, content mix och outputformat. |
| **Hookbibliotek** | Snabb access till öppningar i olika format | `hooks.md` | Välj rätt hook-typ utifrån budskap och målgrupp. |
| **Exempelsamling** | Referensposter för tonalitet, CTA och längd | `exempel.md` | Hitta mönster för struktur, CTA och pillar-balans. |
| **Företagsprofil** | Grundläggande varumärkes- och erbjudandekontext | `context/company/*.md` | Översikter från hemsidan: om satori., tjänstesida, uppstartspaket, metoder och case. |
| **Tjänsteöversikt** | Ingångskarta till alla erbjudanden | `context/services/tjansteoversikt.md` | Snabb filtrering: kategori, målgrupp och prisnivå. |
| **Tjänstespecifika blad** | Djupinfo per tjänst (värde, innehåll, detaljer) | `context/services/satori-*.md` | Lyft fram unika vinklar, resultat och call-to-actions. |
| **Resurser & Metoder** | Stödmaterial för utbildning, policy, KLARAT-metodik | `context/resources/*.md` | Berika thought leadership och case med konkreta tillgångar. |

## Struktur & uppdatering
- All kontext ligger i `growth/campaigns/generated/export/` och är redo att laddas upp till Claude Projects.
- Underkataloger speglar användningsområde:
  - `context/company/` – varumärke, erbjudanden, metoder, kundnytta.
  - `context/services/` – samtliga tjänstedokument från `ops/reference/services/`.
  - `context/resources/` – guider och verktyg från `growth/campaigns/website/pages/`.
- Lägg nya kunskapsfiler i relevant underkatalog och uppdatera tabellen ovan med en kort rad (lager, syfte, fil, användning).
- När strukturen ändras, spegla det även i `ops/index/CLAUDE.md` enligt repo-rutinen.

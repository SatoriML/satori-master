# Email Triage Automation

M365 → AI-klassificering → Gmail

## Filer

| Fil | Syfte |
|-----|-------|
| `n8n-workflow.json` | Importera i n8n |
| `system-prompt.md` | AI-prompts (referens) |
| `setup-guide.md` | Fullständig OAuth-guide |
| `.env.example` | Credentials att fylla i |

## Flöde

- **Varje timme**: Läser M365, klassificerar, skickar viktiga till Gmail
- **Kl 07:00**: Skickar dagens kalenderöversikt till Gmail

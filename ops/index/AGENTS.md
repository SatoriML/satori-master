# Repository Guidelines

## Project Structure & Module Organization
- `ops/` – shared backbone: `index/` (nav docs, manifest, catalog), `process/`, `templates/`, `transcripts/`, `reference/`.
- `.claude/agents/` – production agent briefs; link from `ops/index/CLAUDE.md`.
- `clients/` – varje kund har `overview.md`, `journal.md`, `contracts/`, `deliverables/`; centrala timfiler ligger i `_time-report/` (`time-invoicing.md`, `time-accounts.md`); `_playbooks/` lagrar guider.
- `growth/` – marketing + sales execution: `campaigns/website/pages/`, `campaigns/website/blog/`, `campaigns/generated/` (channel drops), `content-assets/`, `context/`, `enablement/`, `pipeline/`, `inbox/`.
- `archive/` – quarterly buckets for retired material to keep the active tree lean.

## Build, Test, and Development Commands
- `rg "<term>"` — fastest way to locate briefs, decisions, or historical assets across the flattened tree.
- `git status -sb` — run before, during, and after edits to ensure only intentional moves are staged.
- `npx markdownlint-cli2 "**/*.md"` — optional lint pass; install once with `npm install -g markdownlint-cli2` if you touch docs frequently.

## Coding Style & Naming Conventions
- Anchor on `ops/index/MINIMAL-GUIDE.md`: bias toward bullets, action verbs, and one-screen outputs for agent-facing docs.
- Default naming: `YYYY-MM-DD_slug.md` for chronological logs; keep lowercase ASCII unless established Swedish terms require diacritics.
- Describe client-facing work in Swedish business tone with SEK as the default currency reference.
- When adding directories, favour semantic labels (`log/`, `assets/`, `campaigns/`) over numeric prefixes to keep navigation flat.

## Testing Guidelines
- No automated suite exists; rely on meticulous self-review and peer spot checks before merging.
- Validate links and filenames; `rg` + `ls` catches path drift after moves.
- Cross-check dates, metrics, and claims mot källor i `ops/transcripts/` innan publicering.
- Dokumentera större omstruktureringar i PR-beskrivningen.

## Commit & Pull Request Guidelines
- Håll commit-subjekt sentence-case och action-driven (t.ex. `Move marketing campaigns into growth structure`).
- Begränsa varje commit till ett workstream eller en kund.
- Beskriv PR-intent, berörda mappar, verifieringssteg och om `MINIMAL-GUIDE` följdes; bifoga bevis för binärer.

## Agent-Specific Instructions
- Skriv nya automationbriefs i `.claude/agents/` enligt trigger/rules/process/output-mallen.
- Lagra producerade resultat under `growth/campaigns/` eller `clients/<kund>/journal.md` och uppdatera `ops/index/CLAUDE.md` när agentflöden ändras.
- Synka nya resurser med `ops/index/manifest.json` vid behov av programmatisk åtkomst.

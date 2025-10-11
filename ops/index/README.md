# Ops Index

## Quick Navigation
- `AGENTS.md` – contributor guidelines & repo map
- `CLAUDE.md` – agent operating rules and tone
- `MINIMAL-GUIDE.md` – formatting commandments (bullets, brevity)
- `catalog.md` – ownership table for core directories
- `manifest.json` – machine-readable map of clients, website content, and channels

## Structure Overview
- `ops/process/` – canonical playbooks for growth, clients, delivery, and ops
- `ops/templates/` – reusable collateral (client, services, sales)
- `.claude/agents/` – production agent briefs (follow trigger/rules/process/output)
- `clients/<Name>/` – notes + log + assets per account
- `growth/campaigns/website/pages/` – primary web copy; `blog/articles/` for long-form posts
- `growth/campaigns/generated/` – channel drops (`linkedin/`, `email/`, `research/`, `calendar/`, `seo/`)
- `growth/pipeline/` – pipeline forecasts, stage notes, and opp trackers
- `archive/<Quarter>/` – retired content and legacy material

## Usage
- Start with `manifest.json` when you need a quick programmatic lookup (clients, web pages, generated assets).
- Keep `catalog.md` in sync when adding, moving, or retiring directories.
- Update this index whenever the navigation, structure, or ownership model changes.
- Run `git status -sb` and `git diff --stat` before committing large structural edits.

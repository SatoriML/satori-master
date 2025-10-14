# Repository Guidelines

## Project Structure & Module Organization
- `ops/` houses canonical process docs, reusable templates, transcripts, and the `index/` navigation hub (`README.md`, `catalog.md`, `manifest.json`).
- `clients/` stores one folder per account (`<kund-slug>` med `overview.md`, `journal.md`, `contracts/`, `deliverables/`) samt centrala tidsfiler i `_time-report/` (`time-accounts.md`, `time-invoicing.md`); `_playbooks/` rymmer mallar.
- `growth/` collects marketing and sales enablement: website pages, generated social drops, pipeline stages, and shared creative assets.
- `.claude/agents/` contains automation briefs that link back to `ops/index/CLAUDE.md`; update these together.
- `archive/<Quarter>/` keeps retired material so the active tree stays focused.

## Build, Test, and Development Commands
- `rg "<term>"` — fastest cross-repo search; scope by directory when working a single client or campaign.
- `git status -sb` — sanity-check live edits before staging or committing.
- `npx markdownlint-cli2 "**/*.md"` — optional lint pass; install globally once with `npm install -g markdownlint-cli2`.

## Coding Style & Naming Conventions
- Follow `ops/index/MINIMAL-GUIDE.md`: lead with bullets, action verbs, and one-screen outputs.
- Default to lowercase ASCII filenames; keep Swedish diacritics only when mirroring client names or titles.
- Date-prefix logs and campaign drops as `YYYY-MM-DD_slug.md`; place decision logs under the relevant client or pipeline stage.
- Keep prose direct, professional, and in Swedish when facing external stakeholders.

## Testing Guidelines
- No automated suite—proofread manually, confirm numbers and claims against `ops/transcripts/` and source decks.
- After moves or renames, run `rg` plus `ls` to ensure links and manifest entries still resolve.
- For agent briefs, validate trigger, rules, and output paths by dry-running with a small sample input.

## Commit & Pull Request Guidelines
- Write sentence-case, action-led subjects (e.g., `Clarify growth website hero messaging`); one workstream per commit.
- In PRs, outline intent, touched directories, manual checks (lint, link validation), and attach screenshots when updating assets.
- When automation scopes change, cross-link the relevant `.claude/agents/*.md` entry and note updates in `ops/index/CLAUDE.md`.

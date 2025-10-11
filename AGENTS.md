# Repository Guidelines

## Project Structure & Module Organization
- `Marketing/` hosts outbound content; numbered subfolders (`0.Generated/`, `5.Website/md/`) flag draft-to-live status.
- `Kunder/` is the client source of truth: `1.Process/`, `4.Templates/`, `8.Kunder/<Client>/` for active accounts.
- `Sälj/` tracks pipeline via `5.Pipeline/FasN/` and reusable decks in `4.Templates/`; keep Swedish characters in paths.
- `.claude/agents/` stores agent briefs—mirror the schema when adding automation guides.
- `Transcript/` archives meetings by lifecycle; final recaps belong in `Transcript/Summary/`.

## Build, Test, and Development Commands
- `rg "<term>"` — primary search across briefs, templates, and historical decisions.
- `git status -sb` — run before editing and again before pushing.
- `npx markdownlint-cli2 "**/*.md"` — optional Markdown lint (install once with `npm install -g markdownlint-cli2`).
- `git diff --stat` — confirm the change set stays scoped to the intended files.

## Coding Style & Naming Conventions
- Anchor on `MINIMAL-GUIDE.md`: bullet-first layouts, action verbs, max 50 lines for agent docs.
- Mirror the numeric folder convention (`N.Section`) so automation hooks keep resolving.
- Use Swedish business tone for client-facing pieces; default currency references to SEK.
- Keep ASCII unless Swedish terms need diacritics; match existing spellings (`Sälj`, `Tjänster`).

## Testing Guidelines
- No automated suite; rely on thorough self-review plus peer checks.
- Manually verify links and referenced filenames—broken paths degrade agent outputs.
- Cross-check dates and figures against sources in `Transcript/Full/`.
- Note major content shifts in the PR description or a brief file preface.

## Commit & Pull Request Guidelines
- Follow sentence-case, action-driven commits (e.g. `Update linkedin-joachim-agent with Bawan's insights`).
- Scope commits to one workflow or client; split marketing vs. sales changes.
- PRs should outline purpose, touched folders, validation steps, and `MINIMAL-GUIDE.md` compliance.
- Attach before/after evidence for binaries and link CRM or issue IDs when relevant.

## Agent-Specific Instructions
- Reuse the `.claude/agents/*.md` pattern: role/scope, triggers, rules, process, outputs.
- File generated assets under the relevant `0.Generated/` folder, not inside briefs.
- Update `CLAUDE.md` whenever agents are added or retired.

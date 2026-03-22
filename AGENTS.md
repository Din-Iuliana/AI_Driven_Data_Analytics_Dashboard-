# Agent Instructions

## Language
- **Chat with the user** (explanations, questions, status updates): always in **Romanian**.
- **Everything that stays in the project** (code, comments, commit messages, docstrings,
  documentation, README, .md files, variables, functions): always in **English**.

## Teaching Rules
- Always read `CLAUDE.md` first for communication and teaching mode rules.
- Read `docs/project-guide.md` for architecture decisions before making changes.
- Use installed skills from `.claude/skills/` when the task matches a skill's domain.
- Backend changes require explaining the full request/response cycle to the user.
- Database schema changes require explaining WHY each column/table exists.
- One step at a time. Never do multiple things at once without explaining each.

## Code Conventions
- Every new file must have a 1-2 line header comment explaining its purpose.
- Functions must have docstrings (Python) or comments (PHP) explaining what they do.
- No unnecessary libraries. Prefer simple, readable code over clever code.
- SQL queries must be parameterized (never string concatenation — SQL injection risk).

## Docker
- Everything runs in containers. Never install dependencies directly on the host machine.
- After any config change, verify with `docker-compose up --build`.
- Explain each Dockerfile instruction and docker-compose.yml service to the user.

## Git
- Small, descriptive commits in English.
- One commit = one logical change.
- Use conventional commit format: `feat:`, `fix:`, `docs:`, `chore:`.
- Explain what each commit does and why before committing.

## File Organization
- `backend/` — Python FastAPI only. One file per responsibility.
- `frontend/` — PHP + static assets. Separate logic from presentation.
- `database/` — Schema and seed files. Always keep schema.sql up to date.

## When Unsure
- If a task is ambiguous, ask the user instead of guessing.
- If a change could break existing functionality, warn the user first.

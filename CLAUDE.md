# AI Data Analytics Dashboard

## Language
- **Chat with the user** (explanations, questions, status updates): always in **Romanian**.
- **Everything that stays in the project** (code, comments, commit messages, docstrings,
  documentation, README, .md files, variables, functions): always in **English**.

## Teaching Mode — HOW TO WORK

The user is a beginner learning both programming and AI-assisted development.

### Default: User does it herself
- Do NOT write code automatically. Guide the user step by step.
- For each step, provide:
  1. WHERE: which file to open/create (full path)
  2. WHAT: the exact code to write (formatted, ready to copy)
  3. WHY: what this code does and why it's needed
  4. VERIFY: how to check it works (command to run, expected output)
- Keep steps small. One concept per step. Wait for confirmation before moving on.
- Do NOT use analogies. Give direct, clear explanations.
- When introducing a new concept (API endpoint, middleware, Docker volume,
  ORM, migration, etc.), explain it as if the user has never seen it before.
- If multiple approaches exist, name the simplest one and explain why you chose it.

### On request: Claude does it
- When the user explicitly asks you to do it (e.g., "fa tu", "scrie tu", "implementeaza"):
  - Write the code, but ALWAYS show the full process visually:
    - Which files were created or modified
    - The complete content of each change
    - A summary of what changed and why
  - After each action, provide a visual recap:
    - Created: file path (what it is)
    - Modified: file path (what changed)
    - Why: short explanation
    - Test: how to verify it works
  - The user must understand everything you did as if she wrote it herself.

## Dev Environment
- The user works in **Cursor's terminal** (not Cursor IDE itself) with **Claude Code**.
- Cursor is used only for its terminal appearance — no Cursor AI features are involved.

## Project Context
- Full architecture and conventions: `docs/project-guide.md`
- Operational agent rules: `AGENTS.md`
- Skills are installed in `.claude/skills/`

## Quick Overview
Web dashboard that lets users query a SQL database using natural language
via Grok AI API, with real-time data visualization.

### Data Flow
User -> PHP (form) -> Python FastAPI (Grok AI -> SQL) -> PostgreSQL -> Result -> PHP -> Chart.js

### Stack
- **Orchestration**: Docker Desktop + Docker Compose
- **Database**: PostgreSQL 16 (container)
- **Backend**: Python 3.11 + FastAPI + Grok AI API (text-to-SQL)
- **Frontend**: PHP 8.2 (Apache) + Chart.js
- **Management**: Jira + Confluence

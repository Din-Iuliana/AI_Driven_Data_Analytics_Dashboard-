# Project Guide — AI Data Analytics Dashboard

## Architecture

```text
+---------------+     HTTP POST      +--------------------+
|  Frontend     | -----------------> |  Backend           |
|  PHP 8.2      |                    |  Python FastAPI    |
|  + Chart.js   | <----------------- |  + Grok AI API     |
|  Port 8080    |     JSON response  |  Port 8000         |
+---------------+                    +--------+-----------+
                                             | SQL queries
                                    +--------v-----------+
                                    |  PostgreSQL 16     |
                                    |  Port 5432         |
                                    +--------------------+
```

## Project Structure

```text
backend/
  app/
    main.py              # FastAPI entry point
    routes/
      query.py           # /api/query endpoint
    services/
      grok_service.py    # Grok AI API integration
      db_service.py      # PostgreSQL connection and execution
    models/
      schemas.py         # Pydantic request/response models
  requirements.txt
  Dockerfile

frontend/
  public/
    index.php            # Main dashboard page
    css/
      style.css
    js/
      charts.js          # Chart.js initialization and rendering
  src/
    api_client.php       # HTTP calls to Python backend
    helpers.php          # Utility functions
  Dockerfile
  apache.conf

database/
  schema.sql             # Table definitions
  seed.sql               # Test data
  indexes.sql            # Performance indexes
```

## Design Decisions
- PHP serves as a thin UI layer — it does NOT talk to the database directly.
- Python/FastAPI is the only service that connects to PostgreSQL.
- Grok AI receives the DB schema as context and returns SQL queries.
- All inter-service communication is HTTP/JSON over Docker's internal network.

## Database Schema (planned)
Tables: customers, products, sales
(to be defined in database/schema.sql)

## Environment Variables
- `GROK_API_KEY` — Grok AI API key (never commit this)
- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` — DB credentials
- `DATABASE_URL` — Connection string for Python backend

## Docker Services
| Service | Image | Port | Purpose |
|---------|-------|------|---------|
| `db` | postgres:16 | 5432 | PostgreSQL database |
| `backend` | python:3.11 | 8000 | FastAPI + Grok AI |
| `frontend` | php:8.2-apache | 8080 | Dashboard UI |

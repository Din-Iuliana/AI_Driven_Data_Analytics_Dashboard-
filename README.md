  # AI-Driven Data Analytics Dashboard

  A web dashboard that lets users query a SQL database using **natural language**.
  Questions are translated into SQL by the **Grok AI API**, executed against
  **PostgreSQL**, and returned to the browser as interactive tables and
  auto-generated **Chart.js** visualizations.

  ---

  ## Table of Contents

  - [Overview](#overview)
  - [Tech Stack](#tech-stack)
  - [Architecture](#architecture)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Database Schema](#database-schema)
  - [Environment Variables](#environment-variables)
  - [Development Notes](#development-notes)
  - [License](#license)

  ---

  ## Overview

  This project is an end-to-end analytics platform designed for users who want
  to explore data **without writing SQL**. A user types a question such as
  *"Who are the top 5 customers by total sales?"* and the platform:

  1. Sends the question to the **Grok AI API** along with the database schema.
  2. Receives a valid PostgreSQL `SELECT` query.
  3. Executes the query against the database.
  4. Returns the rows as an HTML table and renders an auto-selected chart type
     (bar, line, or pie) based on the result set.
  5. Optionally asks the AI to suggest **performance improvements and indexes**
     for the generated query.

  The project is fully containerized with Docker Compose, so it runs the same
  way on any machine.

  ---

  ## Tech Stack

  | Layer         | Technology                                      |
  |---------------|-------------------------------------------------|
  | Orchestration | Docker Desktop + Docker Compose                 |
  | Database      | PostgreSQL 16                                   |
  | Backend       | Python 3.11 + FastAPI + Uvicorn                 |
  | AI Engine     | Grok AI API (`grok-4-1-fast-non-reasoning`)     |
  | DB Driver     | psycopg2                                        |
  | HTTP Client   | httpx                                           |
  | Frontend      | PHP 8.2 + Apache                                |
  | Charts        | Chart.js (CDN)                                  |
  | DB Admin UI   | CloudBeaver 24.3.0                              |
  | Management    | Jira (Kanban) + Confluence (Documentation)      |

  ---

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

  **Design decisions:**

  - PHP serves only as a thin UI layer and **never talks to the database directly**.
  - Python/FastAPI is the **only service** that connects to PostgreSQL.
  - Grok AI receives the DB schema as system prompt context and returns SQL only.
  - All inter-service communication happens via HTTP/JSON on Docker's internal
    network.
  - The AI is locked to `SELECT` queries only (no `INSERT`, `UPDATE`, `DELETE`,
    `DROP`, or `ALTER`) for safety.

  ---

  ## Features

  - **Natural Language to SQL** — ask questions in plain English, get SQL results.
  - **Smart chart detection** — the frontend automatically picks the best chart
    type based on the result shape:
    - `line` chart for time-based data (dates)
    - `pie` chart for small categorical result sets (≤ 5 rows)
    - `bar` chart as the default
  - **HTML result tables** — every query result is also rendered as a readable table.
  - **AI Performance Analyzer** — a one-click `Analyze Performance` button sends
    the generated SQL back to the AI for index suggestions and optimization tips.
  - **Pre-seeded demo database** — 500 customers, 101 products, and 1,000 sales
    records ready to query.
  - **CloudBeaver web UI** — visual database management at `localhost:5050`.

  ---

  ## Project Structure

  ```text
  AI_Driven_Final_Project/
  ├── backend/
  │   ├── main.py              # FastAPI entry point, endpoints, CORS
  │   ├── grok_service.py      # Grok AI integration (text-to-SQL + optimizer)
  │   ├── db_service.py        # PostgreSQL connection and query execution
  │   ├── requirements.txt     # Python dependencies
  │   └── Dockerfile           # Python 3.11-slim image
  │
  ├── frontend/
  │   ├── index.php            # Main dashboard page + Chart.js logic
  │   ├── css/
  │   │   └── style.css        # Dashboard styling
  │   └── Dockerfile           # PHP 8.2 + Apache image
  │
  ├── database/
  │   ├── generate_data.py     # Script that generates init.sql seed data
  │   └── init.sql             # Schema + 500 customers, 101 products, 1000 sales
  │
  ├── docs/
  │   └── project-guide.md     # Architecture reference for contributors
  │
  ├── docker-compose.yml       # Orchestrates all four services
  ├── .env.example             # Template for required environment variables
  ├── .gitignore
  ├── CLAUDE.md                # AI collaboration rules (teaching mode)
  ├── AGENTS.md                # Agent instructions and code conventions
  └── README.md                # This file
  ```

  ---

  ## Getting Started

  ### Prerequisites

  - **Docker Desktop** (includes Docker Compose)
  - A **Grok AI API key** from [x.ai](https://x.ai/)
  - Git

  ### 1. Clone the repository

  ```bash
  git clone https://github.com/<your-username>/AI_Driven_Final_Project.git
  cd AI_Driven_Final_Project
  ```

  ### 2. Configure environment variables

  Copy the template and fill in your own values:

  ```bash
  cp .env.example .env
  ```

  Then edit `.env`:

  ```env
  POSTGRES_USER=your_username
  POSTGRES_PASSWORD=your_password
  POSTGRES_DB=your_database_name
  DATABASE_URL=postgresql://your_username:your_password@postgresql:5432/your_database_name
  GROK_API_KEY=your_grok_api_key
  ```

  > ⚠️ **Never commit the `.env` file.** It is already listed in `.gitignore`.

  ### 3. Build and start the containers

  ```bash
  docker-compose up --build
  ```

  The first build takes a few minutes. Subsequent starts are fast.

  ### 4. Open the dashboard

  | Service      | URL                       |
  |--------------|---------------------------|
  | Dashboard    | http://localhost:8080     |
  | Backend API  | http://localhost:8000     |
  | CloudBeaver  | http://localhost:5050     |

  ---

  ## Usage

  1. Open http://localhost:8080 in a browser.
  2. Type a question in the input field, for example:
     - *"Who are the top 5 customers by total sales?"*
     - *"What is the total revenue per product category?"*
     - *"Show me monthly sales for 2024."*
     - *"How many products are in each category?"*
  3. Click **Send**.
  4. The dashboard shows:
     - the generated SQL query
     - the results as an HTML table
     - an auto-chosen chart visualization
  5. Click **Analyze Performance** to get AI-generated index suggestions for the
     query that was just executed.

  ---

  ## API Endpoints

  The FastAPI backend exposes two endpoints.

  ### `GET /`

  Health check.

  ```json
  { "status": "Backend is running" }
  ```

  ### `POST /api/query`

  Translates a natural language question into SQL and executes it.

  **Request:**

  ```json
  { "question": "Who are the top 5 customers by total sales?" }
  ```

  **Successful response:**

  ```json
  {
    "question": "Who are the top 5 customers by total sales?",
    "sql": "SELECT c.first_name, c.last_name, SUM(s.total_amount) AS total ...",
    "results": [
      { "first_name": "Maria", "last_name": "Popescu", "total": 12450.00 }
    ]
  }
  ```

  **Error response:**

  ```json
  { "error": "Grok AI took too long to respond" }
  ```

  ### `POST /api/optimize`

  Asks the AI to suggest indexes and optimizations for a given SQL query.

  **Request:**

  ```json
  { "sql": "SELECT ... FROM sales WHERE sale_date > '2024-01-01'" }
  ```

  **Response:**

  ```json
  { "suggestion": "CREATE INDEX idx_sales_sale_date ON sales(sale_date); ..." }
  ```

  ---

  ## Database Schema

  Three related tables form the analytics domain.

  ### `customers`

  | Column       | Type          | Notes                        |
  |--------------|---------------|------------------------------|
  | `id`         | SERIAL        | Primary key                  |
  | `first_name` | VARCHAR(50)   | Not null                     |
  | `last_name`  | VARCHAR(50)   | Not null                     |
  | `email`      | VARCHAR(100)  | Not null, unique             |
  | `created_at` | TIMESTAMP     | Default `CURRENT_TIMESTAMP`  |

  ### `products`

  | Column     | Type          | Notes                                           |
  |------------|---------------|-------------------------------------------------|
  | `id`       | SERIAL        | Primary key                                     |
  | `name`     | VARCHAR(100)  | Not null                                        |
  | `price`    | DECIMAL(10,2) | Not null                                        |
  | `currency` | VARCHAR(3)    | Default `'RON'`                                 |
  | `category` | VARCHAR(50)   | `Electronics`, `Accessories`, `Furniture`, `Gadgets`, `Supplies` |

  ### `sales`

  | Column         | Type          | Notes                                   |
  |----------------|---------------|-----------------------------------------|
  | `id`           | SERIAL        | Primary key                             |
  | `customer_id`  | INTEGER       | FK → `customers(id)`, on delete cascade |
  | `product_id`   | INTEGER       | FK → `products(id)`, on delete cascade  |
  | `quantity`     | INTEGER       | Not null                                |
  | `sale_date`    | DATE          | Not null, always ≥ customer `created_at`|
  | `total_amount` | DECIMAL(10,2) | Not null                                |

  ### Indexes

  The seed script creates these performance indexes automatically:

  ```sql
  CREATE INDEX idx_sales_customer_id ON sales(customer_id);
  CREATE INDEX idx_sales_product_id  ON sales(product_id);
  CREATE INDEX idx_sales_sale_date   ON sales(sale_date);
  CREATE INDEX idx_products_category ON products(category);
  ```

  ### Regenerating seed data

  To regenerate `database/init.sql` with a fresh randomized dataset:

  ```bash
  python database/generate_data.py
  ```

  The random seed is fixed (`random.seed(42)`) so the output is deterministic.

  ---

  ## Environment Variables

  | Variable            | Purpose                                                 |
  |---------------------|---------------------------------------------------------|
  | `POSTGRES_USER`     | PostgreSQL username                                     |
  | `POSTGRES_PASSWORD` | PostgreSQL password                                     |
  | `POSTGRES_DB`       | Database name                                           |
  | `DATABASE_URL`      | Full connection string used by the Python backend       |
  | `GROK_API_KEY`      | API key for the Grok AI service (keep secret)           |

  ---

  ## Development Notes

  - **Hot reload:** the backend runs with `uvicorn --reload`, so Python changes
    are picked up automatically. For PHP, simply refresh the browser.
  - **Rebuilding after dependency changes:** run `docker-compose up --build`
    when you add a new Python package or change a `Dockerfile`.
  - **Logs:** `docker-compose logs -f python` (or `php`, `postgresql`) to tail
    logs for a specific service.
  - **Stopping:** `docker-compose down` stops containers; add `-v` to also drop
    the database volume and reset seed data.
  - **Security:** all SQL is generated by the AI and constrained to `SELECT`
    queries via the system prompt. Never expose the Grok API key in the frontend
    or commit it to Git.

  ---

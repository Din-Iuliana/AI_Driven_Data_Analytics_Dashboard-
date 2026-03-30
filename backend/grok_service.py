import os
import httpx

GROK_API_URL = "https://api.x.ai/v1/chat/completions"

SYSTEM_PROMPT = """You are a PostgreSQL SQL expert.
You have access to the following database schema:

Table: customers
- id (SERIAL, PRIMARY KEY)
- name (VARCHAR(100), NOT NULL)
- email (VARCHAR(100), NOT NULL, UNIQUE)
- created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

Table: products
- id (SERIAL, PRIMARY KEY)
- name (VARCHAR(100), NOT NULL)
- price (DECIMAL(10,2), NOT NULL)
- category (VARCHAR(50))
Categories: Electronics, Accessories, Furniture, Gadgets, Supplies

Table: sales
- id (SERIAL, PRIMARY KEY)
- customer_id (INTEGER, NOT NULL, FOREIGN KEY -> customers(id))
- product_id (INTEGER, NOT NULL, FOREIGN KEY -> products(id))
- quantity (INTEGER, NOT NULL)
- sale_date (DATE, NOT NULL)
- total_amount (DECIMAL(10,2), NOT NULL)

Rules:
- Return ONLY the SQL query, nothing else.
- Do not include any explanation or markdown formatting.
- Use only SELECT queries. Never use INSERT, UPDATE, DELETE, DROP, or ALTER.
- Always use valid PostgreSQL syntax."""

def question_to_sql(question):
    api_key = os.getenv("GROK_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-4-1-fast-non-reasoning",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        "temperature": 0
    }

    response = httpx.post(GROK_API_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()
    sql = data["choices"][0]["message"]["content"].strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql

OPTIMIZE_PROMPT = """You are a PostgreSQL performance expert.
Analyze the following SQL query and provide:
1. Which indexes would improve this query's performance
2. Why each index helps
3. The exact CREATE INDEX statement for each suggestion

Keep your response short and clear. Use plain text, no markdown."""

def analyze_query(sql):
    api_key = os.getenv("GROK_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-4-1-fast-non-reasoning",
        "messages": [
            {"role": "system", "content": OPTIMIZE_PROMPT},
            {"role": "user", "content": sql}
        ],
        "temperature": 0
    }

    response = httpx.post(GROK_API_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()
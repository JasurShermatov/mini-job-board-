# Mini Job Platform Backend

FastAPI backend for a mini job platform. The API supports two operations:

- `GET /jobs` - list all jobs
- `POST /jobs` - create a new job

Tech stack:

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- uv

## Project Structure

```text
mini_job_platform_backend/
├── core/
│   ├── config.py
│   └── database.py
├── models/
│   └── job.py
├── routers/
│   └── jobs.py
├── schemas/
│   └── job.py
├── services/
│   └── job.py
├── .env.example
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Data Model

`Job` fields:

- `id` (integer, primary key)
- `title` (string, required)
- `company` (string, required)
- `salary` (string, optional)
- `description` (text, optional)

## API Endpoints

### `GET /jobs`

Returns all job listings ordered by newest first.

Response example:

```json
[
	{
		"id": 1,
		"title": "Backend Developer",
		"company": "Codefy",
		"salary": "$1200",
		"description": "FastAPI va PostgreSQL bilan ishlash"
	}
]
```

### `POST /jobs`

Creates a new job listing.

Request body:

```json
{
	"title": "Backend Developer",
	"company": "Codefy",
	"salary": "$1200",
	"description": "FastAPI va PostgreSQL bilan ishlash"
}
```

Response: `201 Created`

## Setup with uv

### 1. Initialize project (already done for this repository)

```bash
uv init
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment

Create `.env` from `.env.example` and set your PostgreSQL connection.

```env
PROJECT_NAME=Mini Job Platform API
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/job_platform_db
```

### 4. Run server

```bash
uv run fastapi dev main.py
```

Production style run:

```bash
uv run fastapi run main.py
```

## Notes

- Database tables are created automatically at application startup.
- Validation is handled with Pydantic schemas.
- Database access is handled via SQLAlchemy async session dependency.
# mini-job-board-

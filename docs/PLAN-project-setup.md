# Plan: Layer 1.1 - Project Skeleton Setup

## Goal

Initialize a minimal FastAPI project structure for Pathfinder AI, focusing on a clean, scalable foundation without premature complexity.

## Proposed Structure

```text
backend/
├── main.py              # Application entry point
├── database.py          # Database connection (SQLite)
├── models.py            # database models (SQLAlchemy)
├── schemas.py           # Pydantic schemas (Request/Response)
└── routes/              # API Route definitions
    └── __init__.py
```

## Tasks

- [ ] Create `backend` directory
- [ ] Create `main.py` (FastAPI app instance)
- [ ] Create `database.py` (SQLAlchemy setup)
- [ ] Create `models.py` (Empty for now, just structure)
- [ ] Create `schemas.py` (Empty for now)
- [ ] Verify environment works (`uvicorn backend.main:app --reload`)

## Verification

- [ ] `uvicorn backend.main:app` starts without errors.
- [ ] `curl localhost:8000/docs` returns 200 OK.

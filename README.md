# Order Analytics System

A backend system for managing orders, products, and customers, built with FastAPI and PostgreSQL. Designed to demonstrate backend development and data engineering fundamentals relevant to supply chain and order processing systems.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

## Features
- Full CRUD API for Products
- Database models for Orders, Customers, and Order Items
- Auto-generated API documentation (Swagger UI)

## Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it and install dependencies: `pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic`
3. Set up PostgreSQL and update the connection string in `database.py`
4. Run the server: `uvicorn main:app --reload`
5. Visit `http://127.0.0.1:8000/docs` for API documentation
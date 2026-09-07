# Order Analytics System

A backend system for managing orders, products, and customers, with an integrated data pipeline for sales analytics and demand forecasting. Built with FastAPI and PostgreSQL, and designed to demonstrate backend development and data engineering fundamentals relevant to supply chain and order processing systems.

## Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **Data Engineering:** Pandas (ETL pipeline)
- **Machine Learning:** Scikit-learn (demand forecasting)

## Features
- Full CRUD API for Products, Customers, and Orders (with nested order items)
- Relational database schema with proper foreign key relationships
- ETL pipeline that ingests raw CSV sales data, cleans it, and aggregates it into daily sales totals
- Analytics API endpoint exposing aggregated sales data
- Simple linear regression model to forecast sales for the next 7 days

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /products/ | Create a product |
| GET | /products/ | List all products |
| GET | /products/{id} | Get a single product |
| PUT | /products/{id} | Update a product |
| DELETE | /products/{id} | Delete a product |
| POST | /customers/ | Create a customer |
| GET | /customers/ | List all customers |
| POST | /orders/ | Create an order with items |
| GET | /orders/ | List all orders |
| GET | /orders/{id} | Get a single order |
| GET | /analytics/daily-sales | Get aggregated daily sales |

## Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it and install dependencies: `pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic pandas scikit-learn`
3. Set up PostgreSQL and update the connection string in `database.py`
4. Run the server: `uvicorn main:app --reload`
5. Visit `http://127.0.0.1:8000/docs` for interactive API documentation
6. Run `python etl.py` to load and aggregate sample sales data
7. Run `python forecast.py` to generate a 7-day sales forecast

## Project Structure
- `main.py` - FastAPI application and API routes
- `models.py` - SQLAlchemy database models
- `schemas.py` - Pydantic request/response schemas
- `database.py` - Database connection setup
- `etl.py` - ETL pipeline for sales data
- `forecast.py` - Demand forecasting model
# FastAPI CRUD API with JWT Authentication

A simple backend API built with FastAPI that supports user registration, login with JWT authentication, and basic CRUD operations. The project connects to PostgreSQL and includes automated tests.

## Features

* User registration and login
* JWT-based authentication
* CRUD operations for users
* PostgreSQL database integration
* Automated tests with pytest
* Deployed on Render

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT (python-jose)
* Passlib (bcrypt)
* Pytest

## Project Structure

```
fastapi-crud-auth
│
├── src/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── routers/
│        └── users.py
│
├── tests/
│   └── test_users.py
│
├── pyproject.toml
└── README.md
```

## Setup (Local Development)

Clone the repository

```
git clone <repo-url>
cd fastapi-crud-auth
```

Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run the server

```
uvicorn src.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Interactive docs:

```
http://127.0.0.1:8000/docs
```

## Environment Variables

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@host:port/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running Tests

```
pytest
```

## Live Deployment

The API is deployed on Render.

Example endpoint:

```
https://fastapi-crud-auth.onrender.com/docs
```

## License

MIT

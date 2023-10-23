## FastAPI and Elasticsearch Proof of Concept

This repository contains a proof of concept for integrating FastAPI and Elasticsearch with a simple CRUD functionality.

:warning: This is a work in progress!

### Features

- FastAPI-based RESTful API with CRUD operations
- Elasticsearch integration
- Docker setup for easy deployment

### Prerequisites

- Python 3.x
- Docker
- pip

### Getting started

Create a Python virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```

Run the app:
```
docker compose up --build
```

Documentation should be available at: http://localhost:8000/docs

Elasticsearch dashboard should be available at: http://localhost:5601

### TODO list:

- [ ] add linter to pre-commit hook
- [ ] investigate how custom index settings work and implement some
- [ ] add custom exception handling
- [ ] write tests
- [ ] extend the search functionality
- [ ] add more indexes

# ProjectPicker
ProjectPicker is a simple web application for managing internal project assignments.
Employees can create a profile, select projects they are interested in, and update their information.
## Features
- Employee profile form
- Select one or more projects from a multi-select dropdown
- Project list loaded dynamically from the database
- Form validation (client-side and server-side)
- Create new profile or update an existing one based on email
- Store employee data and project selections in a database
- Backend REST API

## Tech Stack
### Backend:
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Frontend:
- Vanilla JavaScript
- HTML

## Prerequisites
- Python 3.11+
- PostgreSQL
- Docker (optional, recommended for running PostgreSQL)


## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/palllaura/ProjectPicker.git
   cd projectpicker

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv 
   source .venv/bin/activate

3. Install dependencies
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary
   
4. Start PostgreSQL (Docker example)
      ```bash
   docker run --name projectpicker-db \ 
    -e POSTGRES_USER=postgres \ 
    -e POSTGRES_PASSWORD=postgres \ 
    -e POSTGRES_DB=projectpicker \ 
    -p 5432:5432 \ 
    -d postgres

5. Run the backend server
      ```bash
   uvicorn main:app --reload
   
The API will start at:
http://localhost:8000

API documentation (Swagger UI):
http://localhost:8000/docs

## Database
The application uses PostgreSQL with the following main tables:

- users – employee profile information
- projects – available internal projects
- user_projects – mapping table for user project selections

Project data is imported from the provided HTML project list.

## Frontend

The frontend is implemented using simple HTML and Vanilla JavaScript.

The project assignment form allows users to:

- enter profile information
- select one or more projects
- submit and update their profile

Project options in the dropdown are loaded dynamically from the backend API.

## API Overview

Example endpoints:
- GET /projects
- POST /profile
- PUT /profile
- GET /profile
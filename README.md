# Students Database CRUD Application (+ Optional AI Extension)

A Python backend application for managing student records using **FastAPI**, **SQLAlchemy**, and **SQLite**. It supports Create, Read, Update, and Delete (CRUD) operations, along with a local **Ollama AI** feature for asking questions about student data.

## Features

- Create, retrieve, update, and delete student records through REST API endpoints.
- Generate a unique student ID automatically.
- Store student records persistently in SQLite.
- Validate request data, including email addresses, with Pydantic.
- Return appropriate errors for invalid requests and missing students.
- Explore and test endpoints using FastAPI's Swagger UI.
- Ask natural-language questions about stored student data using Ollama.

## Technology Stack

- **Python** — Backend programming language
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server
- **SQLAlchemy** — Database ORM
- **SQLite** — Local database
- **Pydantic and pydantic-settings** — Data validation and application configuration
- **LangChain Ollama and Ollama** — Local AI integration (`llama3.2:1b`)

## Project Structure

```text
FastAPI/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ai_query.py
│   │   ├── base.py
│   │   ├── create_student.py
│   │   ├── delete_student.py
│   │   ├── get_students.py
│   │   └── update_student.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

Local files such as `venv/`, `.env`, and `students.db` are excluded from version control.

## Prerequisites

- Python 3.13 or another version compatible with the project's dependencies
- `pip`
- Ollama (required only for the AI feature)

## Installation and Setup

### 1. Get the project

Download the repository as a ZIP file or clone it using the HTTPS URL provided on GitHub. Open a terminal in the project's root folder (the folder containing `main.py`).

### 2. Create and activate a virtual environment

In Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Database configuration

The application uses SQLite by default:

```text
sqlite:///./students.db
```

An `.env` file is optional because a default database URL is configured. When the application starts, it creates the missing database tables automatically. The local database file is not included in the repository.

### 5. Run the API

```powershell
python -m uvicorn main:app --reload
```

Open **http://127.0.0.1:8000/docs** to view and test the API in Swagger UI.

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/students/` | Create a student record |
| `GET` | `/students/` | Retrieve all student records |
| `GET` | `/students/{student_id}` | Retrieve a student by ID |
| `PUT` | `/students/{student_id}` | Update student details |
| `DELETE` | `/students/{student_id}` | Delete a student record |
| `POST` | `/ai/query-students` | Ask a question about student data |
| `GET` | `/` | Display the welcome response |

## Student Record Fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | Integer | Unique ID generated automatically |
| `student_name` | String | Required student name |
| `student_class` | String | Required class |
| `student_section` | String | Required section |
| `student_dob` | Date (`YYYY-MM-DD`) | Required date of birth |
| `student_email` | Email string | Required, validated email address |

### Example: Create a Student

In Swagger UI, expand `POST /students/`, select **Try it out**, and submit:

```json
{
  "student_name": "Rahul Sharma",
  "student_class": "10",
  "student_section": "A",
  "student_dob": "2005-05-15",
  "student_email": "rahul@example.com"
}
```

The API generates the student's ID automatically.

## AI Query with Ollama

The AI endpoint is an additional feature that runs with a local Ollama model. The CRUD endpoints can be used without Ollama.

1. Install Ollama from **https://ollama.com/**.
2. Download the model:

   ```powershell
   ollama pull llama3.2:1b
   ```

3. Make sure Ollama is running, then start the FastAPI server.
4. In Swagger UI, expand `POST /ai/query-students` and select **Try it out**.
5. Submit a question:

   ```json
   {
     "question": "How many students are there?"
   }
   ```

Other examples include “List all students” and “What are the students' names?” Answers depend on the records currently available in the local database.

## API Testing

1. Create a test student using `POST /students/`.
2. List students using `GET /students/`.
3. Retrieve the new student using `GET /students/{student_id}`.
4. Update a field using `PUT /students/{student_id}` and verify the change.
5. Delete a test record using `DELETE /students/{student_id}`.
6. Restart the application and verify that remaining records persist in SQLite.
7. Test an invalid email address and an unknown student ID to check error handling.
8. With Ollama running, test `POST /ai/query-students` against your test records.

## Security and Privacy

- Use dummy student records for testing and screenshots.
- Do not commit real student information, passwords, or other secrets.
- Exclude `.env`, local SQLite databases, and virtual environments from Git.
- Keep database queries under application control; do not allow the AI model to execute unrestricted SQL.

# 🎯 Task Manager API

A Django RESTful API for managing personal tasks. Each user can register, log in using JWT, and manage their own tasks — including creating, updating, deleting, filtering by date or priority, and marking tasks as complete.

<p>&nbsp;</p>

## Features:

- User registration and login with JWT authentication
- Full CRUD operations on tasks (Create, Read, Update, Delete)
- Each user only accesses their own tasks
- Filter tasks by completion status, priority, and due date range
- Mark tasks as completed with a dedicated endpoint
- Timestamps for created and updated tasks
- API documentation with Swagger UI

<p>&nbsp;</p>

## Endpoints:

### Auth Endpoints:

| Method | Endpoint            | Description               |
|--------|---------------------|---------------------------|
| POST   | `/api/register/`    | Register a new user       |
| POST   | `/api/login/`       | Log in and get JWT token  |

### Task Endpoints (Protected):

| Method | Endpoint                         | Description                     |
|--------|----------------------------------|---------------------------------|
| GET    | `/api/tasks/`                    | List all your tasks             |
| POST   | `/api/tasks/`                    | Create a new task               |
| GET    | `/api/tasks/<id>/`               | View a specific task            |
| PUT    | `/api/tasks/<id>/`               | Update a task                   |
| DELETE | `/api/tasks/<id>/`               | Delete a task                   |
| PATCH  | `/api/tasks/<id>/complete/`      | Mark a task as completed        |
| GET    | `/api/tasks/?completed=true`     | Filter by completed tasks       |
| GET    | `/api/tasks/?priority=high`      | Filter by priority              |
| GET    | `/api/tasks/?due_after=2025-06-01&due_before=2025-06-30` | Filter by due date range |

### Documentation:

| Method | Endpoint     | Description                          | Access |
|--------|--------------|--------------------------------------|--------|
| GET    | `/swagger/`  | Swagger UI (interactive API docs)    | Public |


<p>&nbsp;</p>

## Getting Started:

- Clone this repository:
   ```bash
   git clone https://github.com/Muna-Yusuf/Task-Manager-API.git
   cd Task-Manager-API
   ```
- Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
- Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
- Run migrations:
  ```bash
  python manage.py migrate
  ```
- Run the development server:
  ```bash
  python manage.py runserver
  ```
- Open API Documentation:
    - Swagger UI: http://localhost:8000/swagger/

<p>&nbsp;</p>

## How to Use the API:

1. **Register a User:**
   ```http
   POST http://localhost:8000/api/register/
   ```
   - Body:
   - ```json
     {
        "username": "ali",
        "email": "ali@example.com",
        "password": "yourpassword123*"
     }
      ```

2. **Log In and Get Token:**
   ```http
   POST http://localhost:8000/api/login/
   ```
   - Body:
   - ```json
     {
        "email": "ali@example.com",
        "password": "yourpassword123*"
     }
      ```
    - Response:
    - ```json
      {
        "access": "your_jwt_token_here",
        "refresh": "refresh_token_here"
      }
      ```
3. **Use Token for Authorization:**
   ```makefile
   Authorization: Bearer your_jwt_token_here
   ```
4. **Create a Task:**
   ```http
   POST http://localhost:8000/api/tasks/
   ```
   - Body:
   - ```json
     {
        "title": "Finish report",
        "description": "Submit the final report.",
        "due_date": "2025-07-01",
        "priority": "high"
     }
      ```
5. **List All Your Tasks:**
   ```http
   GET http://localhost:8000/api/tasks/
   ```
6. **Filter Tasks:**
   ```http
   GET /api/tasks/?completed=true&priority=high&due_after=2025-06-01&due_before=2025-06-30
   ```
7. **Update a Task:**
   ```http
   PUT http://localhost:8000/api/tasks/3/
   ```
   - Body:
   - ```json
     {
        "title": "Updated title",
        "description": "Updated description",
        "due_date": "2025-07-10",
        "completed": false,
        "priority": "medium"
     }
      ```
8. **Delete a Task:**
   ```http
   DELETE http://localhost:8000/api/tasks/3/
   ```
9. **Mark a Task as Completed:**
   ```http
   PATCH http://localhost:8000/api/tasks/3/complete/
   ```

<p>&nbsp;</p>

## Testing with Postman or Bruno:

- Register and log in to get your token.
- Set Authorization: Bearer <your_token> in the header.
- Test creating, listing, updating, deleting, and filtering tasks.

<p>&nbsp;</p>

## Tech Stack: 
- Python 3.13 +
- Django 5 +
- Django REST Framework
- SimpleJWT for authentication
- PostgreSQL for storage
- drf-yasg for Swagger UI


<p>&nbsp;</p>

---
Built with Django, Django REST Framework, JWT (via SimpleJWT), and PostgreSQL.

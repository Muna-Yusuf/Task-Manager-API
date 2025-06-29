# 🎯 Task Manager API

A Django RESTful API for managing personal tasks. Each user can register, log in using JWT, and manage their own tasks — including creating, updating, deleting, filtering by date or priority, and marking tasks as complete.

<p>&nbsp;</p>

## Features:

- User registration and JWT-based login (`/api/register/` + `/api/token/`)
- CRUD operations on tasks (Create, Read, Update, Delete)
- Authenticated users only access their own tasks
- Filter tasks by:
  - Completion status (`completed=true`)
  - Priority (`priority=high`)
  - Due date range (`due_date_after`, `due_date_before`)
- Mark tasks as completed (PATCH endpoint)
- Timestamps: `created_at`, `updated_at`
- Swagger UI for API documentation
- Pagination and ordering support (`?page=2&ordering=due_date`)

<p>&nbsp;</p>

## Endpoints:

### Auth Endpoints:

| Method | Endpoint            | Description               |
|--------|---------------------|---------------------------|
| POST   | `/api/register/`    | Register a new user       |
| POST   | `/api/token/`       | Get JWT access + refresh  |

### Task Endpoints (Protected):

| Method | Endpoint                            | Description                     |
|--------|-------------------------------------|---------------------------------|
| GET    | `/api/tasks/`                       | List all your tasks             |
| POST   | `/api/tasks/`                       | Create a new task               |
| GET    | `/api/tasks/{id}/`                  | View a specific task            |
| PUT    | `/api/tasks/{id}/`                  | Update a task (all fields)      |
| PATCH  | `/api/tasks/{id}/`                  | Partial update (some fields)    |
| DELETE | `/api/tasks/{id}/`                  | Delete a task                   |
| PATCH  | `/api/tasks/{id}/mark_complete/`    | Mark a task as completed        |


### Filtering Examples

| Query                                             | Description                      |
|--------------------------------------------------|----------------------------------|
| `/api/tasks/?completed=true`                     | Filter completed tasks           |
| `/api/tasks/?priority=high`                      | Filter by high priority          |
| `/api/tasks/?due_date_after=2025-06-01`          | Tasks due after June 1, 2025     |
| `/api/tasks/?due_date_before=2025-07-01`         | Tasks due before July 1, 2025    |
| `/api/tasks/?ordering=due_date&page=2`           | Sorted by due date, page 2       |

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
   POST /api/token/
   ```
   - Body:
   - ```json
     {
        "email": "ali",
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

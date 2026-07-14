# Task Allocation System

A web-based Task Allocation System built using Flask, MySQL, HTML, and CSS that helps managers assign tasks to employees and track task information efficiently.

## Overview

The Task Allocation System is designed to simplify employee task management within an organization. The application allows managers to add employees, assign tasks, view task details, and manage employee-task relationships through a user-friendly web interface.

This project demonstrates backend development concepts including Flask routing, CRUD operations, database connectivity, SQL queries, form handling, and dynamic webpage rendering.

---

## Features

### Employee Management
- Add new employees
- View all employees
- Store employee information in MySQL database
- Maintain employee records

### Task Management
- Create new tasks
- Assign tasks to employees
- View assigned tasks
- Track task descriptions
- Manage task records

### Database Integration
- MySQL database connectivity
- Persistent data storage
- Relational database design
- Foreign key relationships

### Web Interface
- Responsive HTML pages
- Flask template rendering
- Form-based data submission
- Dynamic content display

---

## Technologies Used

### Backend
- Python
- Flask
- MySQL Connector

### Database
- MySQL

### Frontend
- HTML5
- CSS3

### Tools
- VS Code
- Git
- GitHub

---

## Project Structure

```text
task-allocation-system/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── employees.html
│   ├── tasks.html
│
├── static/
│   ├── style.css
│
├── database/
│   └── schema.sql
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

## Database Design

### Employees Table

| Column | Data Type |
|----------|----------|
| id | INT (Primary Key) |
| name | VARCHAR(100) |
| email | VARCHAR(100) |
| department | VARCHAR(100) |

### Tasks Table

| Column | Data Type |
|----------|----------|
| id | INT (Primary Key) |
| task_name | VARCHAR(100) |
| description | TEXT |
| employee_id | INT (Foreign Key) |

---

## Entity Relationship

```text
Employees
---------
id (PK)
name
email
department

        |
        |
        | 1
        |
        | M
        |

Tasks
-----
id (PK)
task_name
description
employee_id (FK)
```

One employee can have multiple tasks assigned.

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/task-allocation-system.git

cd task-allocation-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
pip install mysql-connector-python
```

or

```bash
pip install -r requirements.txt
```

### 4. Create Database

Open MySQL and execute:

```sql
CREATE DATABASE task_allocation;
```

Create Employees table:

```sql
CREATE TABLE employees(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100)
);
```

Create Tasks table:

```sql
CREATE TABLE tasks(
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(100),
    description TEXT,
    employee_id INT,
    FOREIGN KEY(employee_id)
    REFERENCES employees(id)
);
```

### 5. Configure Database Connection

Update database credentials inside `app.py`

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="task_allocation"
)
```

### 6. Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Flask Concepts Implemented

### Routing

```python
@app.route("/")
def home():
    return render_template("index.html")
```

### Form Handling

```python
if request.method == "POST":
```

### Database Queries

```python
cursor.execute(query)
db.commit()
```

### Fetching Records

```python
cursor.fetchall()
```

### Template Rendering

```python
render_template()
```

---

## CRUD Operations

| Operation | Status |
|------------|---------|
| Create Employee | ✔ |
| Read Employee | ✔ |
| Create Task | ✔ |
| Read Task | ✔ |
| Update Records | Planned |
| Delete Records | Planned |

---

## Learning Outcomes

Through this project I learned:

- Flask application development
- MySQL database integration
- Database schema design
- SQL query execution using Python
- CRUD operations
- Form handling in Flask
- HTML template rendering
- Backend and database communication
- Error debugging and troubleshooting
- Git and GitHub project management

---

## Future Improvements

- User authentication and login system
- Admin dashboard
- Task status tracking
- Task priority levels
- Employee performance analytics
- Search and filter functionality
- Email notifications
- REST API integration
- Responsive Bootstrap UI
- Role-based access control

---

## Screenshots

### Home Page

(Add screenshot here)

### Employee Management

(Add screenshot here)

### Task Assignment

(Add screenshot here)

---

## Author

**Gauri Gupta**

BCA Student | Python Developer

GitHub: https://github.com/gauriri-exe

LinkedIn: https://www.linkedin.com/in/gauri-gupta-849670202/

---

## License

This project is developed for educational and portfolio purposes.

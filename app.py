import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Garv140605",
    database="task_allocation"
)

cursor = db.cursor()


# ---------------- LOGIN ---------------- #

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            return redirect("/home")

    return render_template("login.html")


# ---------------- HOME ---------------- #

@app.route("/home")
def home():
    return render_template("index.html")


# ---------------- EMPLOYEES ---------------- #

@app.route("/employees", methods=["GET", "POST"])
def employees():

    if request.method == "POST":

        name = request.form["name"]
        skill = request.form["skill"]

        query = """
        INSERT INTO employees(name, skill)
        VALUES (%s, %s)
        """

        cursor.execute(query, (name, skill))
        db.commit()

    cursor.execute("SELECT * FROM employees")
    employees_list = cursor.fetchall()

    return render_template(
        "employees.html",
        employees=employees_list
    )


# ---------------- TASKS ---------------- #

@app.route("/tasks", methods=["GET", "POST"])
def tasks():

    if request.method == "POST":

        task_name = request.form["task_name"]
        required_skill = request.form["required_skill"]

        query = """
        INSERT INTO tasks(task_name, required_skill)
        VALUES (%s, %s)
        """

        cursor.execute(query, (task_name, required_skill))
        db.commit()

    cursor.execute("SELECT * FROM tasks")
    task_list = cursor.fetchall()

    return render_template(
        "tasks.html",
        tasks=task_list
    )


# ---------------- ASSIGN TASK ---------------- #

@app.route("/assign", methods=["GET", "POST"])
def assign():

    if request.method == "POST":

        employee_id = request.form["employee_id"]
        task_id = request.form["task_id"]

        cursor.execute(
            "SELECT skill, available FROM employees WHERE id = %s",
            (employee_id,)
        )
        employee = cursor.fetchone()

        cursor.execute(
            "SELECT required_skill FROM tasks WHERE id = %s",
            (task_id,)
        )
        task = cursor.fetchone()

        if employee and task:

            employee_skill = employee[0]
            available = employee[1]
            required_skill = task[0]

            if available and employee_skill.strip().lower() == required_skill.strip().lower():

                cursor.execute(
                    """
                    INSERT INTO assignments(employee_id, task_id)
                    VALUES(%s, %s)
                    """,
                    (employee_id, task_id)
                )

                cursor.execute(
                    """
                    UPDATE employees
                    SET available = FALSE
                    WHERE id = %s
                    """,
                    (employee_id,)
                )

                cursor.execute(
                    """
                    UPDATE tasks
                    SET status = 'Assigned'
                    WHERE id = %s
                    """,
                    (task_id,)
                )

                db.commit()

    cursor.execute("""
        SELECT id, name, skill
        FROM employees
        WHERE available = TRUE
    """)
    employees = cursor.fetchall()

    cursor.execute("""
        SELECT id, task_name, required_skill
        FROM tasks
        WHERE status = 'Open'
    """)
    tasks = cursor.fetchall()

    cursor.execute("""
        SELECT
            e.name,
            e.skill,
            t.task_name,
            t.required_skill
        FROM assignments a
        JOIN employees e
            ON a.employee_id = e.id
        JOIN tasks t
            ON a.task_id = t.id
    """)

    assignments = cursor.fetchall()

    return render_template(
        "assign.html",
        employees=employees,
        tasks=tasks,
        assignments=assignments
    )


if __name__ == "__main__":
    app.run(debug=True)
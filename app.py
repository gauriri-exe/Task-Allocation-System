import flask
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database="task_allocation"
)

cursor = db.cursor()


@app.route("/")
def home():
    return render_template("index.html")


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

@app.route("/tasks", methods=["GET", "POST"])
def tasks():

    if request.method == "POST":

        task_name = request.form["task_name"]
        required_skill = request.form["required_skill"]

        query = """
        INSERT INTO tasks(task_name, required_skill)
        VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (task_name, required_skill)
        )

        db.commit()

    cursor.execute("SELECT * FROM tasks")
    task_list = cursor.fetchall()

    return render_template(
        "tasks.html",
        tasks=task_list
    )



@app.route("/assign")
def assign_tasks():

    cursor.execute(
        "SELECT id, name, skill FROM employees WHERE available = 1"
    )

    employees = cursor.fetchall()

    cursor.execute(
        "SELECT id, task_name, required_skill FROM tasks WHERE status='Open'"
    )

    tasks = cursor.fetchall()

    for task in tasks:

        task_id = task[0]
        required_skill = task[2]

        for employee in employees:

            employee_id = employee[0]
            employee_skill = employee[2]

            if employee_skill == required_skill:

                cursor.execute(
                    """
                    INSERT INTO assignments(employee_id, task_id)
                    VALUES(%s,%s)
                    """,
                    (employee_id, task_id)
                )

                cursor.execute(
                    """
                    UPDATE employees
                    SET available = 0
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

                break

    return "Tasks Assigned Successfully"

if __name__ == "__main__":
    app.run(debug=True)
    

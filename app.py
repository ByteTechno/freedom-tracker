from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt
import os
app = Flask(__name__)
app.secret_key = "super_secret_key_A free life"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "tracker.db")

def get_tasks(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT id, content, timestamp, is_done 
        FROM tasks 
        WHERE user_id = ? 
        ORDER BY id DESC
    """, (user_id,))
    
    results = cursor.fetchall()
    conn.close()
    return results


def add_task(task, user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (content, user_id) VALUES (?, ?)", (task, user_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def toggle_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET is_done = NOT is_done WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, new_content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET content = ? WHERE id = ?", (new_content, task_id))
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def home():
    username = session.get("username")
    if not username:
        return redirect("/login")

    if request.method == "POST":
        task = request.form["task"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_id = cursor.fetchone()[0]
        conn.close()

        add_task(task, user_id)

    tasks = get_tasks(username)
    return render_template("index.html", tasks=tasks, username=username)


@app.route("/delete", methods=["POST"])
def delete():
    task_id = request.form["id"]
    delete_task(task_id)
    return redirect("/")

@app.route("/toggle", methods=["POST"])
def toggle():
    task_id = request.form["id"]
    toggle_task(task_id)
    return redirect("/")

@app.route("/edit", methods=["POST"])
def edit():
    task_id = request.form["id"]
    new_content = request.form["new_content"]
    update_task(task_id, new_content)
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            return "❌ Username and password cannot be empty."

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = None  

        try:
            conn = sqlite3.connect(DB_PATH, timeout=10)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            if cursor.fetchone():
                return "❌ Username already exists. Please choose another."

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_pw)
            )
            conn.commit()
            return redirect("/login")

        except Exception as e:
            return f"❌ Registration error: {str(e)}"

        finally:
            if conn:  
                conn.close()

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_hashed_pw = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_pw):
                session["username"] = username
                return redirect("/")
        
        return render_template("login.html", error="The username or password is incorrect")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

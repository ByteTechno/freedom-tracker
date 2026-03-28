import sqlite3
from .config import DB_PATH

class TaskModel:
    @staticmethod
    def get_all_by_user(user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, content, timestamp, is_done 
            FROM tasks 
            WHERE user_id = ? 
            ORDER BY id DESC
        """, (user_id,))
        results = cursor.fetchall()
        conn.close()
        return results

    @staticmethod
    def add(content, user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (content, user_id) VALUES (?, ?)", (content, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(task_id, user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def toggle(task_id, user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET is_done = NOT is_done WHERE id = ? AND user_id = ?", (task_id, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def update(task_id, new_content, user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET content = ? WHERE id = ? AND user_id = ?", (new_content, task_id, user_id))
        conn.commit()
        conn.close()

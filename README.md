# 🌊 TaskFlow — Efficiency in Motion

A clean, personal task management web app built for people who want to live with intention — not distraction.

This is not just another to-do list.  
**TaskFlow** is a minimal yet powerful system for tracking what truly matters, staying accountable, and taking back control of your time.

---

## ✨ Features

- 👤 **Account system** — Secure registration, login, logout
- 🔐 **Per-user privacy** — Your tasks are completely isolated from others
- 🧾 **Full TaskFlow** — Add, edit, complete, delete tasks with ease
- 💾 **Persistent data** — Stored securely with SQLite
- 📱 **Responsive UI** — Works on desktop and mobile (Bootstrap 5)
- 🔐 **Hashed passwords** — Encrypted with bcrypt for security

---

## 🛠 Tech Stack

- 🐍 **Python 3**
- 🌐 **Flask** (Backend framework)
- 🗃 **SQLite** (Embedded database)
- 🧠 **Jinja2** (HTML templating)
- 🎨 **Bootstrap 5** (CSS framework)
- 🔐 **bcrypt** (Password hashing)

---

## 📂 Project Structure

```bash
TaskFlow/
├── models/          # Data models and database config
├── routes/          # Flask blueprints for routing
├── static/          # CSS, JS, and image assets
├── templates/       # HTML templates (Jinja2)
├── data/            # SQLite database file (generated)
├── app.py           # Application entry point
├── init_db.py       # Database initialization script
└── requirements.txt # Project dependencies
```

---

## 🖼 Screenshots

### ✅ Task Dashboard  
![Task dashboard](screenshots/dashboard.png)

### 🔐 Register Page  
![Register page](screenshots/register.png)

---

## 🚀 Live Demo

🖥️ **Live Demo** → [TaskFlow on Render](https://freedom-tracker.onrender.com)

> ⚠️ Hosted on Render free tier — it may take up to 30 seconds to cold start.

---

## 🧩 Use Cases

- ✅ Replace your paper or sticky-note task list
- ✅ Stay focused with a clean interface and no distractions
- ✅ Use it to build daily discipline and small habits
- ✅ Make it your first step toward building your own productivity stack

---

## 🧪 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/ByteTechno/TaskFlow.git
cd TaskFlow

# 2. (Optional) Create virtual env
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Init the database
python init_db.py

# 5. Run the app
python app.py
```

---

## ⚙️ Configuration

- **Secret Key**: Set in `app.py`. For production, use `os.environ.get('SECRET_KEY')`.
- **Database**: Default path is `data/TaskFlow.db`.
- **Port**: Defaults to `5000` or the value of the `PORT` environment variable.

---

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

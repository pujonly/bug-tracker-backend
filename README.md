# ⚙️ Bug Tracker - Backend (FastAPI & PostgreSQL)

The robust, high-performance backend API for the Full-Stack Bug Tracker application. Powered by FastAPI, SQLAlchemy, and automated enterprise-grade PL/pgSQL database auditing.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)

---

## 🌟 Key Features

* **Asynchronous RESTful API:** Built with FastAPI for high-speed request handling and automatic interactive documentation (`/docs`).
* **Secure Authentication & Hashing:** Implements robust user registration and login verification using industry-standard **Bcrypt** password hashing via `passlib`.
* **Database ORM Management:** Structured data models and robust session handling using SQLAlchemy.
* **Automated Database Audit Trail (Enterprise Feature):**
  * Utilizes custom **PostgreSQL PL/pgSQL Triggers**.
  * Automatically captures `INSERT`, `UPDATE`, and `DELETE` events directly at the database level.
  * Records historical data (`OLD` vs `NEW` JSONB snapshots) and timestamps without application-layer intervention.

---

## 🛠️ Tech Stack

* **Framework:** FastAPI (Python)
* **Database & ORM:** PostgreSQL, SQLAlchemy
* **Security & Hashing:** Passlib, Bcrypt
* **Server ASGI:** Uvicorn

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/username-mu/bug-tracker-backend.git](https://github.com/username-mu/bug-tracker-backend.git)
cd bug-tracker-backend
```

### 2. Create & Activate Virtual Environment 
```bash
python -m venv venv
# On Windows:
```bash
venv\Scripts\activate
# On macOS/Linux:
```bash
source venv/bin/activate

### 3. Install Dependency
```bash
pip install -r requirements.txt

### 4. Configure Database
* Set up your local PostgreSQL database, then import the database schema structure from the file located at /database/bug_tracker.sql to set up tables and audit triggers. Configure your connection string inside your database configuration file:
```bash
DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"

### 5. Run the Development Server
```bash
uvicorn main:app --reload
* The server will start at http://127.0.0.1:8000. You can access the interactive API docs at http://127.0.0.1:8000/docs.

---

## 🚀 Deployment (Railway / Render)

* Push your backend code to a dedicated GitHub repository.
* Create a new project on Railway or Render and link your repository.
* Add the required Environment Variable:
* DATABASE_URL: Your cloud PostgreSQL connection string (e.g., from Supabase or Neon).
* Ensure requirements.txt is in the root directory for automated dependency installation.

---

## 📄 License

* Distributed under the MIT License. See LICENSE for more information.


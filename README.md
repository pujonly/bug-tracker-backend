Bug Tracker - Backend (FastAPI & PostgreSQL)
The robust, high-performance backend API for the Full-Stack Bug Tracker application. Powered by FastAPI, SQLAlchemy, and automated enterprise-grade PL/pgSQL database auditing.

🌟 Key Features
Asynchronous RESTful API: Built with FastAPI for high-speed request handling and automatic interactive documentation (/docs).

Secure Authentication & Hashing: Implements robust user registration and login verification using industry-standard Bcrypt password hashing via passlib.

Database ORM Management: Structured data models and robust session handling using SQLAlchemy.

Automated Database Audit Trail (Enterprise Feature):

Utilizes custom PostgreSQL PL/pgSQL Triggers.

Automatically captures INSERT, UPDATE, and DELETE events directly at the database level.

Records historical data (OLD vs NEW JSONB snapshots) and timestamps without application-layer intervention.

🛠️ Tech Stack
Framework: FastAPI (Python)

Database & ORM: PostgreSQL, SQLAlchemy

Security & Hashing: Passlib, Bcrypt

Server ASGI: Uvicorn

⚙️ Installation & Local Setup
1. Clone the Repository
Bash
git clone https://github.com/username-mu/bug-tracker-backend.git
cd bug-tracker-backend
2. Create & Activate Virtual Environment
Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Database Connection
Set up your local PostgreSQL database, then configure your connection string inside your database configuration file (e.g., database.py):

Python
DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"
5. Run the Development Server
Bash
uvicorn main:app --reload
The server will start at [http://127.0.0.1:8000](http://127.0.0.1:8000). You can access the interactive API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Database Schema
import /database/bug_tracker.sql to your Postgresql

🚀 Deployment (Railway / Render)
Push your backend code to a dedicated GitHub repository.

Create a new project on Railway or Render and link your repository.

Add the required Environment Variable:

DATABASE_URL: Your cloud PostgreSQL connection string (e.g., from Supabase or Neon).

Ensure requirements.txt is in the root directory for automated dependency installation.

📄 License
Distributed under the MIT License. See LICENSE for more information.
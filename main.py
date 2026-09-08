from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from passlib.context import CryptContext

import model as models
from database import engine, get_db

app = FastAPI(title="Bug Tracker & Audit Trail API")

from fastapi.middleware.cors import CORSMiddleware

# Tambahkan ini agar Next.js bisa berkomunikasi dengan FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Bisa dibatasi nanti, "*" artinya mengizinkan semua asal (untuk development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Konfigurasi Hashing Password menggunakan Bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/register", status_code=201)
def register_user(data: UserRegister, db: Session = Depends(get_db)):
    # Cek apakah email sudah terdaftar
    existing_user = db.query(models.User).filter(models.User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email sudah terdaftar!")
    
    # Enkripsi password sebelum disimpan ke database
    hashed_password = get_password_hash(data.password)
    
    new_user = models.User(
        name=data.name,
        email=data.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Registrasi berhasil!", "user_id": new_user.id}

@app.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email tidak ditemukan!")
    
    # Verifikasi apakah password cocok dengan hash di database
    if not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Password salah!")
        
    return {
        "message": "Login berhasil!",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }

# --- SKEMA PYDANTIC (Untuk validasi input dari user) ---
class TaskCreate(BaseModel):
    title: str
    description: str = None
    status: str = "Open"
    priority: str = "Medium"
    assigned_to: int = None
    created_by: int = None

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    status: str = None
    priority: str = None
    assigned_to: int = None

# --- ENDPOINT UTAMA ---

@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Bug Tracker dengan PostgreSQL Audit Trail!"}

# 1. READ: Melihat semua daftar tasks
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

# 2. CREATE: Membuat task baru
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        assigned_to=task.assigned_to,
        created_by=task.created_by
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Task berhasil dibuat!", "data": new_task}

# 3. UPDATE: Mengubah task (Trigger audit trail PostgreSQL akan otomatis aktif di sini!)
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task tidak ditemukan")
    
    # Perbarui data jika dikirim oleh user
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return {"message": "Task berhasil diperbarui (Cek audit log di database!)", "data": task}

# 4. DELETE: Menghapus task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task tidak ditemukan")
    
    db.delete(task)
    db.commit()
    return {"message": "Task berhasil dihapus!"}

# 5. AUDIT LOGS: Melihat riwayat perubahan otomatis dari database
@app.get("/audit-logs")
def get_audit_logs(db: Session = Depends(get_db)):
    logs = db.query(models.AuditLog).order_by(models.AuditLog.logged_at.desc()).all()
    return logs
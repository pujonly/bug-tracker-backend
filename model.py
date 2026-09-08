from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, JSON, TIMESTAMP, text
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(String(50), server_default="Open")
    priority = Column(String(50), server_default="Medium")
    assigned_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    table_name = Column(String(50), nullable=False)
    action = Column(String(10), nullable=False)
    row_id = Column(Integer, nullable=False)
    old_data = Column(Text) # Bisa menggunakan JSONB jika didukung, disimpan sebagai teks/dict oleh SQLAlchemy
    new_data = Column(Text)
    changed_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    logged_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
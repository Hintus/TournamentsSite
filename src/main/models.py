from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
import enum
from tkinter import CASCADE

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql.annotation import Annotated

# from auth.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

from typing import List, Optional
from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import func

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(100))
    email : Mapped[str] = mapped_column(String(100), unique=True)
    password : Mapped[str] = mapped_column(String(250))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now())

class Group(Base):
    __tablename__ = "groups"
    id :Mapped[int] = mapped_column(primary_key=True)
    name :Mapped[str] = mapped_column(String(100))
    created_by :Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at :Mapped[datetime] =mapped_column(server_default=func.now())

class UserGroup(Base):
    __tablename__ = "user_groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    group_id: Mapped[int] =mapped_column(ForeignKey("groups.id"))

class Expense(Base):
    __tablename__ = "expenses"
    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    paid_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str] = mapped_column(String(100))
    amount: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

class ExpenseItems(Base):
    __tablename__ = "items_expense"
    id: Mapped[int] = mapped_column(primary_key=True)
    expense_id: Mapped[int] = mapped_column(ForeignKey("expenses.id"))
    description: Mapped[str] = mapped_column(String(100))
    amount: Mapped[float] = mapped_column(Float)

class ItemsConsumed(Base):
    __tablename__ = "items_consumed"
    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items_expense.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

class Balance(Base):
    __tablename__ = "balance"
    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    who_owes: Mapped[int] = mapped_column(ForeignKey("users.id"))
    to_whom: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(Float)
# 04. Database Integration with PostgreSQL and SQLAlchemy

## 1. What is Database Integration?

Database integration connects a FastAPI application to a database so the application can store, retrieve, update, and delete data persistently.

Unlike an in-memory Python list, database records can remain available after the application restarts.

## 2. What is PostgreSQL?

PostgreSQL is a relational database management system (RDBMS). It stores data in tables containing rows and columns.

**Example:** A `products` table might contain `id`, `name`, and `price` columns.

## 3. What is SQLAlchemy?

SQLAlchemy is a Python SQL toolkit and Object-Relational Mapper (ORM). It helps Python applications interact with relational databases using Python objects and SQL expressions.

**Purpose:** It reduces the need to write raw SQL for every database operation.

## 4. Important Database Components

| Component | Purpose |
|---|---|
| Database URL | Specifies how the application connects to the database |
| Engine | Manages database connectivity |
| Session | Provides a workspace for database operations |
| Model | Defines the structure of mapped database data |
| Table | Stores records in rows and columns |
| ORM | Connects Python objects with relational database operations |

## 5. Database Connection Flow

1. FastAPI needs to perform a database operation.
2. The application obtains a database session.
3. SQLAlchemy uses the configured engine to communicate with PostgreSQL.
4. PostgreSQL executes the requested database operation.
5. The result is returned to the application.
6. FastAPI prepares and returns the API response.
7. The session is closed or released when the operation is complete.

## 6. Example SQLAlchemy Model

A simplified example using SQLAlchemy's declarative mapping:

```python
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
```

**Explanation:**
- `Base` is the base class for mapped models.
- `Product` represents the `products` table.
- `__tablename__` specifies the table name.
- `id` and `name` define mapped columns.

This example defines a model; it does not, by itself, create the table or implement CRUD endpoints.

## 7. What is a Database Session?

A session is used to perform database operations within a unit of work.

Common operations include:
- Querying records
- Adding new records
- Updating existing records
- Deleting records
- Committing changes to the database

A session should be managed carefully so it is properly closed or released, including when errors occur.

## 8. In-Memory Data vs Database Storage

| In-memory list | PostgreSQL database |
|---|---|
| Data is stored in application memory | Data is stored in the database |
| Data normally disappears when the process restarts | Committed data persists |
| Useful for basic learning examples | Suitable for persistent application data |
| Limited database features | Supports queries, constraints, transactions, and indexes |

## 9. Database Configuration and Safety

- Store database credentials in environment variables.
- Keep `.env` out of your GitHub repository.
- Use a suitable PostgreSQL driver and database URL.
- Handle database errors appropriately.
- Manage sessions and transactions correctly.
- Use migrations or a controlled schema-management process as the project grows.

## 10. Key Takeaways

- PostgreSQL stores application data persistently.
- SQLAlchemy helps Python code communicate with relational databases.
- The engine manages connectivity, while sessions perform database operations.
- Models describe the structure of mapped data.
- Database-backed CRUD requires endpoints to actually query and modify the database.
- Creating a model or connecting an engine alone does not make existing endpoints database-backed.

**Next document:** `05-testing.md` — Automated Testing with pytest and FastAPI TestClient.


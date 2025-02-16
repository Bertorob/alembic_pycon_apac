# Workshop Database Setup

This project uses Alembic for database migrations with MySQL.

## Prerequisites

- Python 3.9 or higher
- MySQL Server
- pip (Python package installer)

## Setup Instructions

### 1. Activate Virtual Environment or install dependencies

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### 2. Database Configuration

Make sure your MySQL server is running and update the database URL in `alembic.ini` if needed:

```ini
sqlalchemy.url = mysql+pymysql://pycon:pyconapac2025@localhost/workshop
```

### 3. Create Database

Log into MySQL and create the database:

```sql
CREATE DATABASE workshop;
```

### 4. Run Migrations

```bash

# Run all pending migrations
alembic upgrade head

# Create a new migration (when needed)
alembic revision --autogenerate -m "description of changes"
```

## Common Commands

- Check current migration status:
  ```bash
  alembic current
  ```

- View migration history:
  ```bash
  alembic history
  ```

- Rollback to previous migration:
  ```bash
  alembic downgrade -1
  ```

## Troubleshooting

If you encounter any issues:

1. Ensure MySQL server is running
2. Verify database credentials in `alembic.ini`
3. Make sure all dependencies are installed
4. Check if the database exists and is accessible

## Project Structure

```
.
├── alembic/
│   ├── versions/        # Migration files
│   ├── env.py          # Alembic environment
│   └── script.py.mako  # Migration template
├── alembic.ini         # Alembic configuration
└── README.md           # This file
```

# Support

If you have any questions or issues, please contact us at [roberto.landi@axyon.com](mailto:roberto.landi@axyon.com).

from sqlalchemy import create_engine

from core.config import settings

DATABASE_URL = (
    f"mssql+pyodbc://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_SERVER}/"
    f"{settings.DB_NAME}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&TrustServerCertificate=yes"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class AuditLog(Base):

    __tablename__ = "audit_log"

    id: Mapped[int] = mapped_column(primary_key=True)

    action_name: Mapped[str] = mapped_column(String(200))

    old_value: Mapped[str]

    new_value: Mapped[str]

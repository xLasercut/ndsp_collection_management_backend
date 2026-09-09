from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from tables.common import Base


class Collection(Base):
    __tablename__ = 'collection'

    collection_id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

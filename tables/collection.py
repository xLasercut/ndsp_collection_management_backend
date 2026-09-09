from sqlalchemy.orm import Mapped, mapped_column

from tables.common import Base


class Collection(Base):
    __tablename__ = 'collection'

    collection_id: Mapped[str] = mapped_column('collection_id', primary_key=True)
    name: Mapped[str]

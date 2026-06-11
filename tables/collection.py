from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Collection(DeclarativeBase):
    __tablename__ = 'collection'

    collection_id: Mapped[str] = mapped_column('collection_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')

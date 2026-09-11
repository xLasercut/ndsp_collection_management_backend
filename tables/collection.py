from sqlmodel import SQLModel, Field


class Collection(SQLModel, table=True):
    __tablename__ = 'collection'

    collection_id: str = Field(primary_key=True)
    name: str

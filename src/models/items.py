from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.models import Base


class Items(Base):
    __tablename__ = 'items'
    table_description = 'Created to store all data about items'
    __table_args__ = {'info': {'description': table_description}}

    id = Column(Float, index=True, primary_key=True, comment='Item Id')
    name = Column(String, index=True, comment='Item name')
    tags = Column(String, comment='Item tags')
    gold_value = Column(Float, comment='Item value')
    purchasable = Column(Boolean, comment='Bool that indicates if the item is purchasable')
    png_path = Column(String, comment='Path to png')


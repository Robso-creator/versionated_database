from sqlalchemy import Column, Integer, String

from src.models import Base


class Pydicio(Base):
    __tablename__ = 'pydicio'

    table_description = 'Created to store all data from Dicio.com.br related to brazilian portuguese words'
    __table_args__ = {'info': {'description': table_description}}

    id = Column(Integer, index=True, primary_key=True, autoincrement=True, comment='Word ID')
    word = Column(String, comment='Word')
    length = Column(Integer, index=True, comment='Length of the word')

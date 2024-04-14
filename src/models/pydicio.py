from sqlalchemy import Column, Integer, String

from src.models import Base


class Pydicio(Base):
    __tablename__ = 'pydicio'

    table_description = 'Created to store all data from Dicio.com.br related to brazilian portuguese words'
    __table_args__ = {'info': {'description': table_description}}

    id = Column(Integer, index=True, primary_key=True, autoincrement=True, comment='Identificador único da palavra')
    name = Column(String, comment='Palavra do dicionário brasileiro')
    length = Column(Integer, index=True, comment='Quantidades de letras existentes na palavra')

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.models import Base


class Champions(Base):
    __tablename__ = 'champions'
    table_description = 'Created to store all data about League Of Legends champions'
    __table_args__ = {'info': {'description': table_description}}

    id = Column(Integer, index=True, primary_key=True, comment='Champion Id')
    key = Column(Integer, comment='Champion Id')
    name = Column(String, index=True, comment='Champion name')
    tags = Column(String, comment='Champion tags')
    attack = Column(Integer, comment='Champion attack value')
    defense = Column(Integer, comment='Champion defense value')
    magic = Column(Integer, comment='Champion magic value')
    difficulty = Column(Integer, comment='Champion difficulty value')
    hp = Column(Float, comment='Champion hp value')
    hpperlevel = Column(Float, comment='Champion hpperlevel value')
    mp = Column(Float, comment='Champion mp value')
    mpperlevel = Column(Float, comment='Champion mpperlevel value')
    movespeed = Column(Float, comment='Champion movespeed value')
    armor = Column(Float, comment='Champion armor value')
    armorperlevel = Column(Float, comment='Champion armorperlevel value')
    spellblock = Column(Float, comment='Champion spellblock value')
    spellblockperlevel = Column(
        Float, comment='Champion spellblockperlevel value',
    )
    attackrange = Column(Float, comment='Champion attackrange value')
    hpregen = Column(Float, comment='Champion hpregen value')
    hpregenperlevel = Column(Float, comment='Champion hpregenperlevel value')
    mpregen = Column(Float, comment='Champion mpregen value')
    mpregenperlevel = Column(Float, comment='Champion mpregenperlevel value')
    crit = Column(Float, comment='Champion crit value')
    critperlevel = Column(Float, comment='Champion critperlevel value')
    attackdamage = Column(Float, comment='Champion attackdamage value')
    attackdamageperlevel = Column(
        Float, comment='Champion attackdamageperlevel value',
    )
    attackspeedperlevel = Column(
        Float, comment='Champion attackspeedperlevel value',
    )
    attackspeed = Column(Float, comment='Champion attackspeed value')
    png_path = Column(String, comment='Path to png')


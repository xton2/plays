from sqlalchemy import Column, Integer, String

from .meta import Base

class Plays(Base):
    __tablename__ = 'plays'

    playTitle = Column(String)
    playId = Column(String, primary_key=True)

from sqlalchemy import Column, Integer, String

from .meta import Base

class HenryIV(Base):
    __tablename__ = 'henryiv'

    line_id = Column(Integer, primary_key=True)
    act = Column(Integer)
    scene = Column(Integer)
    speaker = Column(String)
    speech_number = Column(Integer)
    text = Column(String)


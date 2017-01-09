import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
import json

DBUSER  = 'playapi'
DBPASS  = 'playapi'
DB      = 'playdb'
DBHOST  = '127.0.0.1'
DBPORT  = 5432

FILENAME = 'henry_iv.json'

Base = declarative_base()

class Plays(Base):
    __tablename__ = 'plays'

    playTitle = Column(String)
    playId = Column(String, primary_key=True)

class HenryIV(Base):
    __tablename__ = 'henryiv'

    line_id = Column(Integer, primary_key=True)
    act = Column(Integer)
    scene = Column(Integer)
    speaker = Column(String)
    speech_number = Column(Integer)
    text = Column(String)

dbUrl = 'postgresql://{}:{}@{}:{}/{}'.format(DBUSER, DBPASS, DBHOST, DBPORT, DB)
engine = sqlalchemy.create_engine(dbUrl)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

playText = open(FILENAME).read()
playLines = json.loads(playText)

playAct = 0
playScene = 0

session = Session()

session.add(Plays(playTitle='Henry IV', playId='henryiv'))
for line in playLines:
    fields = {
        'line_id' : line['line_id'],
        'speaker' : line['speaker'],
        'speech_number' : line['speech_number'],
        'text' : line['text_entry'],
    }
    
    if line['text_entry'].startswith('ACT'):
        playAct += 1
        playScene = 0 
    if line['text_entry'].startswith('SCENE'):
        playScene += 1

    if line['line_number'] == '' or fields['text'] == fields['text'].upper():
        fields['speaker'] = ''
        fields['speech_number'] = None

    fields['act'] = playAct
    fields['scene'] = max(playScene, 1)

    session.add(HenryIV(**fields))

session.commit()


from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import func

from models import HenryIV
from models import Plays

playClassMap = {
    'henryiv': HenryIV,
}

filters = {
    'plays': ['playTitle', 'playId'],
    'playLines': ['text', 'speaker', 'scene', 'act'],
}

def resultFilter(queryResult, fields):
    result = []
    for item in queryResult:
        itemDict = item.__dict__
        result.append({ field: itemDict[field] for field in fields })
    return result

@view_config(route_name='plays')
def getPlays(request):
    query = request.dbsession.query(Plays)
    result = query.all()
    response = resultFilter(result, filters['plays'])
    return response

@view_config(route_name='getPlay')
def getPlay(request):
    play = request.matchdict.get('play')
    playClass = playClassMap[play]

    query = request.dbsession.query(playClass)
    result = query.all()
    response = resultFilter(result, filters['playLines'])
    return response

@view_config(route_name='getPlayAct')
def getPlayAct(request):
    play = request.matchdict.get('play')
    act = request.matchdict.get('act')
    playClass = playClassMap[play]

    query = request.dbsession.query(playClass)
    result = query.filter(playClass.act == act).all()
    response = resultFilter(result, filters['playLines'])
    return response

@view_config(route_name='getPlayActScene')
def getPlayActScene(request):
    play = request.matchdict.get('play')
    act = request.matchdict.get('act')
    scene = request.matchdict.get('scene')
    playClass = playClassMap[play]

    query = request.dbsession.query(playClass)
    result = query.filter( (playClass.act == act) & (playClass.scene == scene) ).all()
    response = resultFilter(result, filters['playLines'])
    return response
    
@view_config(route_name='getPlaySpeaker')
def getPlayActSpeaker(request):
    play = request.matchdict.get('play')
    speaker = request.matchdict.get('speaker').lower()
    playClass = playClassMap[play]

    query = request.dbsession.query(playClass)
    result = query.filter(func.lower(playClass.speaker) == speaker).all()
    response = resultFilter(result, filters['playLines'])
    return response

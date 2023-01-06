from fastapi import APIRouter, Depends, Body
from schemas.server import ServerData
from database.servers import Servers

router = APIRouter(prefix='/server')


@router.get('/')
def get(db: Servers = Depends(Servers)):
    servers = db.get_all()
    return {'servers': servers}


@router.post('/')
def post(server: ServerData = Body(), db: Servers = Depends(Servers)):
    try:
        db.add(server.server)
        status = 'ok'
    except Exception as e:
        status = e.__str__()
    return {'status': status}

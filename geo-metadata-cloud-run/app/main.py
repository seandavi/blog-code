from fastapi import FastAPI
from starlette.responses import RedirectResponse
from omicidx.geo import parser as gp


app = FastAPI(title='GEO metadata as JSON')

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def get_geo_dict(geo: str):
    res = {}
    for i in gp.geo_entity_iterator(geo, targ='self'):
        res[geo] = i.dict()
    return res

@app.get("/geo/{geo}", tags=['GEO'])
def geo_to_json(geo: str): #, token: str=Depends(oauth2_scheme)):
    return get_geo_dict(geo)

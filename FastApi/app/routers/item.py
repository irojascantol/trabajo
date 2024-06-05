from fastapi import APIRouter, Request, Response
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse

router = APIRouter()


fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class Item(BaseModel):
    name: str
    descr: str | None = None

 
@router.get("/param", response_class=PlainTextResponse, status_code = 201)
def read_root():
    json_compatible_item_data = jsonable_encoder({"Nombre": "Ivan", "Apellidos": "Rojas Carrasco", "Notas": {"Matematica": 12, "Historia": 20}})
    return JSONResponse(content=json_compatible_item_data)


@router.get("/item/", status_code=200)
async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]

@router.get("/mirror/")
def mirror(item: Item):
    return item

@router.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}


#Aqui falta enviar un status personalizado en caso no encuentre resultado
@router.get("/data/", status_code=307)
async def api_data(request: Request, response: Response):
    # try:
    params = request.query_params._dict
    url = f'https://http.cat/status/{params["status"]}'
    print(url)
    response = RedirectResponse(url=url)
    return response
    # except:
    #     response.status_code = status.HTTP_404_CREATED
    #     return response

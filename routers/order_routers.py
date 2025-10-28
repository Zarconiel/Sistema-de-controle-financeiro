from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags= ["order"]) 




#-------------------Rotas---------------------

#------------Get
@order_router.get("/")
async def home():
    return {"Menssagem": "Bem-vindo à API de Controle Financeiro!"}


@order_router.get("/transações")
def trasaçoes():
    pass

@order_router.get("/saldo")
def saldo():
    pass



#------------Post
@order_router.post("/transações")
def transaçoes():
    pass
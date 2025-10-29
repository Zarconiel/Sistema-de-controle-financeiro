from fastapi import FastAPI


app= FastAPI()

from routers.order_routers import order_router
from routers.auth_routers import auth_router

app.include_router(order_router)
app.include_router(auth_router)



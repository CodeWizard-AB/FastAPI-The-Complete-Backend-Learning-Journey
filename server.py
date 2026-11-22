from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="Product Management API",
    description="API for managing products",
    version="1.0.0",
    docs_url="/api-docs",
    redoc_url="/reference",
    openapi_url="/schema.json",
    debug=True
)


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}


@app.get('/health')
async def get_health():
    return {"status": "OK"}


class Product(BaseModel):
    id: int
    name: str
    price: float


@app.get('/products', response_model=list[Product])
async def get_products():
    products = [
        {"id": 1, "name": "Iphone 15", "price": 100},
        {"id": 2,  "name": "Iphone 16", "price": 200}
    ]
    return products


@app.post('/products')
async def create_product():
    return JSONResponse(
        content={"message": "Product created!"},
        status_code=201,
        headers={"x-secret": "secret_code"},
    )

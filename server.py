from fastapi import FastAPI

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

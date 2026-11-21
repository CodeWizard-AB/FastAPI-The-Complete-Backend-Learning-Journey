from fastapi import FastAPI

app = FastAPI(title="CodeForge Learning API",
              description="API for CodeForge Learning", version="1.0.0", docs_url="/api-docs", redoc_url="/reference", openapi_url="/schema.json", debug=True)


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}


@app.get('/health')
async def get_health():
    return {"status": "OK"}
